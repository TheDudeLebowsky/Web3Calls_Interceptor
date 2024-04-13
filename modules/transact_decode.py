from web3 import Web3
import os
import re
from pprint import pformat
import sys
import json
from eth_utils import function_abi_to_4byte_selector
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from modules.my_colors import *
from config.abi_list import *
from config.addresses import *
from config.rpc_config import RPC_CONFIGURATION
from modules.transact_get import TransactGet

def save_pretty_format_to_file(data, filename, debugmode=False):
    """
    Takes a Python object (like a dictionary or list), pretty-prints it, and saves it to a text file.

    :param data: Python object to be pretty-printed and saved.
    :param filename: Name of the file to save the data to.
    """
    filename = os.path.join('json', filename)
    try:
        # Attempt to convert the Python object to a pretty-printed string using json.dumps
        pretty_data = json.dumps(data, indent=4)
    except TypeError:
        # If data is not JSON serializable, use pformat
        pretty_data = pformat(data, indent=4)

    try:
        # Write the string to a text file
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                file.write(pretty_data)
            print(f"Data successfully saved to {filename}") if debugmode else None
    except Exception as e:
        print(f"An error occurred: {e}")

class Decoder:
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
        self.thread_name = kwargs.get('thread_name','WORKER')
        self.get = kwargs.get('get', TransactGet(rpc=self.rpc, web3=self.web3))
        self.static_length = 64
        self.dynamic_types = ['string', 'bytes', 'tuple']



#BROKEN Mostly for testing purposes

    #//obsolete
    def guess_type(self, hex_arg):

        """Will guess the type of the argument based on its value."""
        """Returns a string with the type and the decoded value."""

        if hex_arg == '0000000000000000000000000000000000000000000000000000000000000000':
            return f"{BOLD}Boolean{RESET} : False"
        elif hex_arg == '0000000000000000000000000000000000000000000000000000000000000001':
            return f"{BOLD}Boolean{RESET} : True"
        try:
            decoded_string = bytes.fromhex(hex_arg).decode('utf-8').rstrip('\x00')
            if decoded_string.isprintable():
                return f"{BOLD}String{RESET} : {decoded_string}"
            else:
                return f"Could be a non-ASCII string or binary data"
        except:
            decimal_value = int(hex_arg, 16)
            value_in_eth = decimal_value / 10**18
            return f"{BOLD}Decimal{RESET} : {decimal_value:<20} | {BOLD}Ether{RESET} : {value_in_eth}"
    



    #//complete
    def set_contract(self, address, debugmode=False):
        """Fetches the ABI, the ticker and the contract."""
        """checksum the address from the contract address using web3."""
        """Requires transact_get.py"""
        filename = f"{self.rpc_network}_abi_{address}.json"
        if address is None:
            return None,None,None,None
        address = self.web3.to_checksum_address(address)
        abi = self.get.abi(address=address)
        contract = self.get.contract(address, abi)
        
        if self.function_exists(contract, 'symbol'):
            ticker = self.get.ticker(address, contract, abi)
            if ticker is not None:
                filename = f"{self.rpc_network}_abi_{ticker}.json"

        else:
            ticker = None

        save_pretty_format_to_file(abi, filename)

        if debugmode:
            summary = (f"\n{'_'*50}GETTING CONTRACT{'_'*50}\n")
            summary += (f"Network : {self.rpc_network}\n")
            summary += (f"Contract address : {address}\n")
            summary += (f"Ticker : {ticker}\n") 
            summary += (f"Saved ABI to : {filename}\n")
            summary += (f"{'_'*120}\n\n")
            print(summary)

        return address, abi, contract, ticker
    
    def methodID_to_functionParams(self,methodID,  abi, debugmode=False):
        """Gets the function signature from the method ID using the contract's ABI."""
        """From transact_methodID.py"""
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
            print(f"{ERROR}Error{RESET} : No function signature found in ABI for method ID {INFO}{methodID}{RESET}")
            return None
        return functionSignature
    
    def parse_function_signature(self, signature):

        """
        Parses a function signature with unnamed parameters into a dictionary with indexed parameter names as keys
        and their types as values.

        Parameters:
        - signature (str): The function signature in the format functionName(type1,type2,...).

        Returns:
        - dict: A dictionary mapping indexed parameter names to their types.
        """

        _, param_str = signature.split('(')
        param_str = param_str.rstrip(')')
        params = param_str.split(',')
        param_dict = {f"param{i+1}": param.strip() for i, param in enumerate(params)}
        
        return param_dict

    def checksum(self, address):
        checksum_address = self.web3.to_checksum_address(address)
        if checksum_address != address:
            print(f"Address was not checksummed. Checksummed address : {checksum_address}")
        else:
            print(f"Address is already checksummed : {checksum_address}")
        return checksum_address






    #//main
    def interpret_arguments(self, func_signature, hex_args):
        interpreted_args = []
        
        # Function to interpret a single hex argument based on the provided type
        def interpret_arg(hex_arg, arg_type):
            if arg_type == 'bool':
                return bool(int(hex_arg, 16))
            elif arg_type in ['uint256', 'uint16']:
                return int(hex_arg, 16)
            elif arg_type == 'address':
                return '0x' + hex_arg[-40:]
            elif arg_type == 'bytes32':
                try:
                    decoded_string = bytes.fromhex(hex_arg).decode('utf-8').rstrip('\x00')
                    if decoded_string.isprintable():
                        return decoded_string
                    else:
                        return "Non-ASCII or binary data"
                except:
                    return "Error decoding string"
            else:
                return "Unsupported type"
        
        # Process each argument according to its type in the function signature
        for name, arg_type in func_signature.items():
            if arg_type == 'tuple[]':
                start, end = self.find_tuple_boundaries(hex_args, 0, list(func_signature.values()))
                #//todo : Implement tuple[] interpretation  
                
            hex_arg = hex_args.pop(0) # Remove the first argument from the list for processing
            value = interpret_arg(hex_arg, arg_type)
            interpreted_args.append({
                'Argument': hex_arg,
                'Name': name,
                'Type': arg_type,
                'Value': value
            })
        
        return interpreted_args
    
    def find_tuple_boundaries(self, hex_args, current_position, element_types):
        try:
            # Calculate the initial offset where tuple data starts
            offset = int(hex_args[current_position:current_position + 64], 16) * 2
            if offset > len(hex_args):
                return None, None

            start = offset
            end = start
            for element_type in element_types:
                if start >= len(hex_args):  # Check if the current start is within bounds
                    break

                if element_type in self.dynamic_types:
                    # For dynamic types, find the length from the offset stored at 'start'
                    if start + 64 > len(hex_args):
                        break
                    element_offset = int(hex_args[start:start + 64], 16) * 2
                    if element_offset + 64 > len(hex_args):
                        break
                    length = int(hex_args[element_offset:element_offset + 64], 16) * 2
                else:
                    length = self.static_length

                start += length
                end = start

            return offset, end
        except ValueError as e:
            print(f"Error processing tuple boundaries: {e}")
            return None, None

    def decode_with_web3(self, input_data, contract_address, abi):
        contract = self.web3.eth.contract(address=contract_address, abi=abi)
        func_obj, func_params = contract.decode_function_input(input_data)


def main():
    tx_hash = '0x324bcc68c9a83aa1d5aba9b9781e1fa94d57d1e2fed19f24a9f8e1b17b9b9fdc'
    hex_args = ("0000000000000000000000000000000000000000000000000000000000000080" +
                "0000000000000000000000000000000000000000000000000000000000000001" +
                "0000000000000000000000000000000000000000000000000000000000000001" +
                "0000000000000000000000000000000000000000000000000000000000000005" +
                "48656c6c6f000000000000000000000000000000000000000000000000000000")

    element_types = ['uint256', 'bool', 'string']
    current_position = 0
    
    network_choice = 'sepolia arbitrum'
    rpc = RPC_CONFIGURATION[network_choice]
    cryptotest = Decoder(rpc=rpc)

    input_data = '00000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000001c000000000000000000000000000000000000000000000000000000000000002800000000000000000000000000000000000000000000000000000000000000340000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000004c0000000000000000000000000000000000000000000000000000000000000058000000000000000000000000000000000000000000000000000000000000006400000000000000000000000005806e416da447b267cea759358cf22cc41fae80f00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000002470a08231000000000000000000000000747001f7dd22202ccad0b070d9e7c577c8578218000000000000000000000000000000000000000000000000000000000000000000000000000000009d1db8253105b007ddde65ce262f701814b911250000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000244d2301cc000000000000000000000000747001f7dd22202ccad0b070d9e7c577c8578218000000000000000000000000000000000000000000000000000000000000000000000000000000006581e59a1c8da66ed0d313a0d4029dce2f746cc500000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000002470a08231000000000000000000000000747001f7dd22202ccad0b070d9e7c577c8578218000000000000000000000000000000000000000000000000000000000000000000000000000000007eeca4205ff31f947edbd49195a7a88e6a91161b00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000002470a08231000000000000000000000000747001f7dd22202ccad0b070d9e7c577c8578218000000000000000000000000000000000000000000000000000000000000000000000000000000009dad8a1f64692adeb74aca26129e0f16897ff4bb00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000002470a08231000000000000000000000000747001f7dd22202ccad0b070d9e7c577c8578218000000000000000000000000000000000000000000000000000000000000000000000000000000008239fbb3e3d0c2cdfd7888d8af7701240ac4dca400000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000002470a08231000000000000000000000000747001f7dd22202ccad0b070d9e7c577c8578218000000000000000000000000000000000000000000000000000000000000000000000000000000007f8e75356015fecfaff66e2b34f181a093dc451900000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000002470a08231000000000000000000000000747001f7dd22202ccad0b070d9e7c577c857821800000000000000000000000000000000000000000000000000000000000000000000000000000000c63fab87cb00249190577937ab6e04da0ae6963300000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000002470a08231000000000000000000000000747001f7dd22202ccad0b070d9e7c577c857821800000000000000000000000000000000000000000000000000000000'
    address = '0x9d1dB8253105b007DDDE65Ce262f701814B91125'
    abi = filter_assets(main_dict=MAIN_DICT, networks='berachain', asset_types='contract', key1='abi', mode='single', address=address)
    cryptotest.decode_with_web3(input_data, address, abi)
    start, end =  cryptotest.find_tuple_boundaries(hex_args, current_position, element_types)
    print(f"Start : {start} | End : {end}")
    #cryptotest.decode_input_data('0xc2eb801373555344000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004563918244f4000073424e4200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001ef384914880004c617965725a65726f000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    #                        contract_address='0xe0875cbd144fe66c015a95e5b2d2c15c3b612179', abi=None, debugmode=True)
    #cryptotest.decode_input_data_from_tx_hash(tx_hash='0x324bcc68c9a83aa1d5aba9b9781e1fa94d57d1e2fed19f24a9f8e1b17b9b9fdc')
    
if __name__ == "__main__":
    main()
