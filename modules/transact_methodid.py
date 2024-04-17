from web3 import Web3
import os
import re
import sys
from eth_utils import function_abi_to_4byte_selector
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.')))
from modules.my_colors import *
from config.abi_list import *
from config.addresses import *
from config.rpc_config import RPC_CONFIGURATION
from modules.extract_variables_from_file import FileExtractor
from modules.transact_get import TransactGet

#//TODO : clean the code, refactor, do additional testing and verifiy the formatting so i can use it to decode input data from transactions


def cls():
    if os.name == 'nt':
        os.system('cls')



class TransactMethodID():
    def __init__(self, *args, **kwargs):
        self.rpc = kwargs.get('rpc', None)
        self.rpc_url = self.rpc['url']
        self.rpc_chain_id = self.rpc['chain_id']
        self.rpc_network = self.rpc['network']
        self.rpc_token = self.rpc['token']
        self.rpc_explorer = self.rpc['explorer']
        self.EIP_1559 = kwargs.get('EIP_1559', False)
        self.include_thread = kwargs.get('include_thread', False)
        self.web3 = kwargs.get('web3', Web3(Web3.HTTPProvider(self.rpc_url)))
        self.thread_name = kwargs.get('thread_name','WTF')
        #self.get=None
        self.get = kwargs.get('get', TransactGet(rpc=self.rpc, web3=self.web3)) 

#//obsolete
    def extract_params_from_functionSignaturev1(self, function_signature):
        """
        Extracts and returns the list of parameter types from a function signature.
        Args:
            function_signature (str): The function signature as a string, e.g., "setValues(uint256,bool)".
        """
        # Match everything inside the outermost parentheses.
        match = re.search(r'\((.*)\)', function_signature)
        if not match:
            return None
        
        parameters_string = match.group(1)
        print(f"Parameters string: {parameters_string}")
        parameter_types = [param.strip() for param in parameters_string.split(',')]
        return parameter_types





#//complete
    def compare(self, input, expected):
        """Compares the input to the expected value and prints the result."""
        """Just use this when you have long string such as a function declaration or json object and too lazy to compare them manually."""
        if input == expected:
            print("Test passed")
        else:
            print("Test failed")

    def checksum(self, address):
        """Checks if an Ethereum address is checksummed and checksums it if it is not."""
        """Usefull when hardcoding addresses in scripts. Make sure they are checksummed."""
        checksum_address = self.web3.to_checksum_address(address)
        if checksum_address != address:
            print(f"{RED}Address was not checksummed{RESET}. Checksummed address : {checksum_address}")
        else:
            print(f"{GREEN}Address is already checksummed{RESET} : {checksum_address}")
        return checksum_address

    def abi_to_functions_dict(self, abi, debugmode=False):
        """
        Converts a contract's ABI to a dictionary of methods, including detailed tuple structure.
        """
        dict_list = []

        for item in abi:
            if item['type'] == 'function':
                function_name = item['name']
                signature = item['name'] + '('
                param_details = []
                names = []
                types = []
                for param in item['inputs']:
                    function_dict = {}
                    if param['type'] == 'tuple[]':
                        
                        tuple_components = param.get('components', [])
                        tuple_signature = '(' + ','.join(f"{c['type']}" for c in tuple_components) + ')[]'
                        param_details.append(param['name'] + tuple_signature)
                        types.append(tuple_signature) 
                    elif param['type'].startswith('tuple'):
                        
                        tuple_components = param.get('components', [])
                        tuple_signature = '(' + ','.join(f"{c['type']}" for c in tuple_components) + ')'
                        param_details.append(param['name'] + tuple_signature)
                        types.append(tuple_signature) 
                    else:
            
                        param_details.append(param['name'] + '[' + param['type'] + ']')
                        types.append(param['type']) 
                    names.append(param['name']) 
                signature += ','.join(param_details)
                signature += ')'


                
                selector = function_abi_to_4byte_selector(item).hex()
                selector = '0x' + selector
                params = self.extract_params_from_functionSignature(signature)
                function_dict = {
                    'function_name': function_name,
                    'selector': selector,
                    'signature': signature,
                    'params': params,
                    'names': names,
                    'types': types
                }
                dict_list.append(function_dict)
                
        if debugmode:
            print(f"\n\n{BOLD}Function Dictionary : {RESET}")
            for item in dict_list:
                for key, value in item.items():
                    print(f"{key} : {value}")
                print("\n")
        return dict_list
    
    def create_functions_dict_dataset(self, filename='config/abi_list.py', debugmode=False):
        """
        Creates a dataset of function dictionaries from a list of contract's ABI.
        """
        self.fileextractor = FileExtractor(filename) 
        self.variable_dict = self.fileextractor.get_variables_values() 
        all_dict_list = {}

        for key, abi in self.variable_dict.items():
            print(f"Key : {key} --> ABI : {abi}") if debugmode else None
            dict_list = self.abi_to_functions_dict(abi, debugmode)
            all_dict_list[key] = dict_list
        return all_dict_list



    def find_methodid_in_signatures(self, target_method_id='0x62c79e2e', function_signatures=None):
        """Finds the function signature that matches the target method ID."""
        """Use with get_function_signature_from_abi() to get the function signatures."""
        for signature in function_signatures:
            method_id = Web3.keccak(text=signature).hex()[:10]
            print(f"Function Signature: {signature} --> {method_id}")
            if method_id == target_method_id:
                print(f"Matching signature for {MY_GREEN}{target_method_id}: {signature}{RESET}")
                return signature

    def methodID_to_functionSignature(self,methodID,  abi, debugmode=False):
        """Gets the function signature from the method ID using the contract's ABI."""
        functionSignature = {}
        for item in abi:
            if item['type'] == 'function':
                selector = function_abi_to_4byte_selector(item).hex()
                selector = '0x' + selector
                if methodID.lower() != selector.lower():
                    continue
                else:
                    for param in item['inputs']:
                        param_name = param['name']
                        functionSignature[param_name] = param['type']
        print(f"Function Signature : {functionSignature}") if debugmode else None
        if len(functionSignature) == 0:
            print(f"{ERROR}Error{RESET} : No function signature found for method ID {INFO}{methodID}{RESET}")
            return None
        return functionSignature
    
    def function_exists(self, contract, function_name):
        # Check if the function exists in the contract's ABI
        return any(function_name == item.get('name') for item in contract.abi if item.get('type') == 'function')

    def get_runtime_bytecode(self, contract_address):
        """Fetches the runtime bytecode of a contract at the specified address."""
        
        runtime_bytecode = self.web3.eth.get_code(contract_address)
        runtime_bytecode_hex = self.web3.to_hex(runtime_bytecode)
        print(f"Runtime Bytecode: {runtime_bytecode}")
        print(f"Runtime Bytecode hex: {runtime_bytecode_hex}")
        return runtime_bytecode

    def functionDeclaration_to_functionSignature(self, function_declaration):
        """Converts a Solidity function declaration to a canonical function signature."""
        
        print(f"Function Declaration: {function_declaration}")
        # Find the function name and parameters
        match = re.search(r'function\s+(\w+)\s*\((.*?)\)\s*external', function_declaration, re.DOTALL)      
        if not match:
            return None  # or raise an exception
        
        function_name = match.group(1)
        params = match.group(2)
        
        # Mapping of Solidity types to their canonical representation
        type_mapping = {
            'SwapKind': 'uint8',  # Assuming SwapKind is an enum, represented as uint8
            # Add more mappings as necessary
        }
        
        # Convert parameter types
        converted_params = []
        for param in params.split(','):
            param_type = param.split()[0]  # Assumes type is the first word
            canonical_type = type_mapping.get(param_type, param_type)  # Map type or keep as is
            converted_params.append(canonical_type)
        
        signature = f"{function_name}({','.join(converted_params)})"
        print(f"Function Signature: {signature}")
        return signature

    def extract_params_from_functionSignature(self, function_signature, debugmode=False):
        """
        Extracts and returns the list of parameter types from a function signature, handling nested structures.
        Args:
            function_signature (str): The function signature as a string, e.g., "voteWeighted(proposalId[uint64],options(int32,string)[],metadata[string])".
        """
        # Match everything inside the outermost parentheses.
        match = re.search(r'\((.*)\)', function_signature)
        if not match:
            return None
        
        parameters_string = match.group(1)
        print(f"Parameters string: {parameters_string}") if debugmode else None

        # Use a stack to manage the splitting of parameters considering nested commas and parentheses.
        parameters = []
        temp = ''
        level = 0
        for char in parameters_string:
            if char == ',' and level == 0:
                parameters.append(temp.strip())
                temp = ''
            else:
                if char in ['(', '[']:
                    level += 1
                elif char in [')', ']']:
                    level -= 1
                temp += char
        if temp:
            parameters.append(temp.strip())  # Add last parameter if exists

        return parameters



def main():
    #region test variables
    function_declaration = """
    function swap(
        SwapKind kind,
        address poolId,
        address assetIn,
        uint256 amountIn,
        address assetOut,
        uint256 amountOut,
        uint256 deadline
    ) external payable returns (address[] memory assets, uint256[] memory amounts);
    """    
    inputs="""[{'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'address[]', 'name': 'assetsIn', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amountsIn', 'type': 'uint256[]'}], 'name': 'addLiquidity', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'enum IERC20DexModule.SwapKind', 'name': 'kind', 'type': 'uint8'}, {'components': [{'internalType': 'address', 'name': 'poolId', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'userData', 'type': 'bytes'}], 'internalType': 'struct IERC20DexModule.BatchSwapStep[]', 'name': 'swaps', 'type': 'tuple[]'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}], 'name': 'batchSwap', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'address[]', 'name': 'assetsIn', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amountsIn', 'type': 'uint256[]'}, {'internalType': 'string', 'name': 'poolType', 'type': 'string'}, {'components': [{'components': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}], 'internalType': 'struct IERC20DexModule.AssetWeight[]', 'name': 'weights', 'type': 'tuple[]'}, {'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}], 'internalType': 'struct IERC20DexModule.PoolOptions', 'name': 'options', 'type': 'tuple'}], 'name': 'createPool', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'baseAsset', 'type': 'address'}, {'internalType': 'address', 'name': 'quoteAsset', 'type': 'address'}], 'name': 'getExchangeRate', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}], 'name': 'getLiquidity', 'outputs': [{'internalType': 'address[]', 'name': 'asset', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}], 'name': 'getPoolName', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}], 'name': 'getPoolOptions', 'outputs': [{'components': [{'components': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}], 'internalType': 'struct IERC20DexModule.AssetWeight[]', 'name': 'weights', 'type': 'tuple[]'}, {'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}], 'internalType': 'struct IERC20DexModule.PoolOptions', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'name': 'getPreviewAddLiquidityNoSwap', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liqOut', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'name': 'getPreviewAddLiquidityStaticPrice', 'outputs': 
[{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liqOut', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'enum IERC20DexModule.SwapKind', 'name': 'kind', 'type': 'uint8'}, {'components': [{'internalType': 'address', 'name': 'poolId', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'userData', 'type': 'bytes'}], 'internalType': 'struct IERC20DexModule.BatchSwapStep[]', 'name': 'swaps', 'type': 'tuple[]'}], 'name': 'getPreviewBatchSwap', 'outputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'getPreviewBurnShares', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'name': 'getPreviewSharesForLiquidity', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'getPreviewSharesForSingleSidedLiquidityRequest', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'enum IERC20DexModule.SwapKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'baseAsset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'baseAssetAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'quoteAsset', 'type': 'address'}], 'name': 'getPreviewSwapExact', 'outputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'assetAmount', 'type': 'uint256'}], 'name': 'getRemoveLiquidityExactAmountOut', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'sharesIn', 'type': 'uint256'}], 'name': 'getRemoveLiquidityOneSideOut', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}], 'name': 'getTotalShares', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 
'address', 'name': 'withdrawAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}], 'name': 'removeLiquidityBurningShares', 'outputs': [{'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'withdrawAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'address', 'name': 'sharesIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'maxSharesIn', 'type': 'uint256'}], 'name': 'removeLiquidityExactAmount', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'enum IERC20DexModule.SwapKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'address', 'name': 'poolId', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}], 'name': 'swap', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}]"""
    expected = """[{'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'address[]', 'name': 'assetsIn', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amountsIn', 'type': 'uint256[]'}], 'name': 'addLiquidity', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'enum IERC20DexModule.SwapKind', 'name': 'kind', 'type': 'uint8'}, {'components': [{'internalType': 'address', 'name': 'poolId', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'userData', 'type': 'bytes'}], 'internalType': 'struct IERC20DexModule.BatchSwapStep[]', 'name': 'swaps', 'type': 'tuple[]'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}], 'name': 'batchSwap', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'address[]', 'name': 'assetsIn', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amountsIn', 'type': 'uint256[]'}, {'internalType': 'string', 'name': 'poolType', 'type': 'string'}, {'components': [{'components': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}], 'internalType': 'struct IERC20DexModule.AssetWeight[]', 'name': 'weights', 'type': 'tuple[]'}, {'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}], 'internalType': 'struct IERC20DexModule.PoolOptions', 'name': 'options', 'type': 'tuple'}], 'name': 'createPool', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'baseAsset', 'type': 'address'}, {'internalType': 'address', 'name': 'quoteAsset', 'type': 'address'}], 'name': 'getExchangeRate', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}], 'name': 'getLiquidity', 'outputs': [{'internalType': 'address[]', 'name': 'asset', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}], 'name': 'getPoolName', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}], 'name': 'getPoolOptions', 'outputs': [{'components': [{'components': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}], 'internalType': 'struct IERC20DexModule.AssetWeight[]', 'name': 'weights', 'type': 'tuple[]'}, {'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}], 'internalType': 'struct IERC20DexModule.PoolOptions', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'name': 'getPreviewAddLiquidityNoSwap', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liqOut', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'name': 'getPreviewAddLiquidityStaticPrice', 'outputs': 
    
  
[{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liqOut', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'enum IERC20DexModule.SwapKind', 'name': 'kind', 'type': 'uint8'}, {'components': [{'internalType': 'address', 'name': 'poolId', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'userData', 'type': 'bytes'}], 'internalType': 'struct IERC20DexModule.BatchSwapStep[]', 'name': 'swaps', 'type': 'tuple[]'}], 'name': 'getPreviewBatchSwap', 'outputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'getPreviewBurnShares', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'name': 'getPreviewSharesForLiquidity', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'getPreviewSharesForSingleSidedLiquidityRequest', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'enum IERC20DexModule.SwapKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'baseAsset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'baseAssetAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'quoteAsset', 'type': 'address'}], 'name': 'getPreviewSwapExact', 'outputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'assetAmount', 'type': 'uint256'}], 'name': 'getRemoveLiquidityExactAmountOut', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'sharesIn', 'type': 'uint256'}], 'name': 'getRemoveLiquidityOneSideOut', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}], 'name': 'getTotalShares', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 
'address', 'name': 'withdrawAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}], 'name': 'removeLiquidityBurningShares', 'outputs': [{'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'withdrawAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'address', 'name': 'sharesIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'maxSharesIn', 'type': 'uint256'}], 'name': 'removeLiquidityExactAmount', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'enum IERC20DexModule.SwapKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'address', 'name': 'poolId', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}], 'name': 'swap', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}]"""
    #endregion

    network_choice = 'berachain'
    rpc = RPC_CONFIGURATION[network_choice]
    cryptotest = TransactMethodID(rpc=rpc)
    cls()
    #cryptotest.compare(inputs, expected)
    #cryptotest.abi_to_functionSignatures(abi=ABI_PoolAddressProvider)
    #cryptotest.abi_to_functions_dict(ABI_ERC20, debugmode=True)
    cryptotest.create_functions_dict_dataset(debugmode=True)
    #cryptotest.methodID_to_functionSignature(methodID='0xc2eb8013', abi=SYNTHR_ABI_LEND)
    #cryptotest.checksum('0x101f52c804c1c02c0a1d33442eca30ecb6fb2434')
    #cryptotest.find_methodid_in_signatures(target_method_id='0xc2eb8013', function_signatures=signatures)
    #cryptotest.functionSignature_to_methodID(signature='batchSwap(uint8,(address,address,uint256,address,uint256,bytes)[],uint256)')
    #cryptotest.get_runtime_bytecode(contract_address='0x9261b5891d3556e829579964B38fe706D0A2D04a')
    #cryptotest.functionDeclaration_to_functionSignature(function_declaration)
    
    
if __name__ == "__main__":
    main()

