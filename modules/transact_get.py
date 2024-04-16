import os
import json
import requests
import sys
import time
from requests.exceptions import ConnectionError
import threading
from web3 import Web3
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from config.abi_list import *
from config.rpc_config import RPC_CONFIGURATION
from config.addresses import MAIN_DICT, create_abi_list
from modules.erc721_interface_id import ERC721_INTERFACE_ID
from modules.extract_variables_from_file import FileExtractor
from config.api_list import *
from modules.my_colors import *
RED = '\033[91m'
RESET = '\033[0m'
YELLOW = '\033[93m'
GREEN = '\033[92m'

#//COMPLETE
"""This is a heavily simplefied version of transact_get.py"""
"""Only the necessary functions are included"""

#//TOTEST
def set_explorer_endpoint(rpc_network, contract_address):
    # Mapping network names to their corresponding API variables and URL patterns
    network_info = {
        'goerli': (API_ETHERSCAN, "https://api-goerli.etherscan.io/api"),
        'mumbai': (API_POLYGONSCAN, "https://api-testnet.polygonscan.com/api"),
        'eth': (API_ETHERSCAN, "https://api-etherscan.io/api"),
        'bsc': (API_BSCSCAN, "https://api-bscscan.com/api"),
        'matic': (API_POLYGONSCAN, "https://api-polygonscan.com/api"),
        'optimism': (API_OPTISCAN, "https://api-optimistic.etherscan.io/api"),
        'arbitrum': (API_ARBISCAN, "https://api-arbiscan.io/api"),
        'berachain': (API_GENERAL, "https://api.routescan.io/v2/network/testnet/evm/80085/etherscan/api"),
        'metis': (None, "https://andromeda-explorer.metis.io/api"),  # Metis does not use an API key
        'sepolia arbitrum': (API_GENERAL, "https://api-sepolia.arbiscan.io/api")
    }

    api_key, url_pattern = network_info.get(rpc_network, (None, None))
    
    if api_key:
        rpc_explorer_endpoint = f"{url_pattern}?module=contract&action=getabi&address={contract_address}&apikey={api_key}"
    else:
        rpc_explorer_endpoint = f"{url_pattern}?module=contract&action=getabi&address={contract_address}"
    
    return rpc_explorer_endpoint

#//HELPER_FUNCTIONS
def set_explorer_endpointv1(rpc_network, contract_address):
    if rpc_network == 'goerli':
        api_explorer = API_ETHERSCAN            
        rpc_explorer_endpoint = f"https://api-goerli.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_explorer}"
    elif rpc_network == 'mumbai':
        api_explorer = API_POLYGONSCAN
        rpc_explorer_endpoint = f"https://api-testnet.polygonscan.com/api?module=contract&action=getabi&address={contract_address}&apikey={api_explorer}"
    elif rpc_network == 'eth':
        api_explorer = API_ETHERSCAN
        rpc_explorer_endpoint = f"https://api-etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_explorer}"
    elif rpc_network == 'bsc':
        api_explorer = API_BSCSCAN
        rpc_explorer_endpoint = f"https://api-bscscan.com/api?module=contract&action=getabi&address={contract_address}&apikey={api_explorer}"
    elif rpc_network == 'matic':
        api_explorer = API_POLYGONSCAN
        rpc_explorer_endpoint = f"https://api-polygonscan.com/api?module=contract&action=getabi&address={contract_address}&apikey={api_explorer}"
    elif rpc_network == 'optimism':
        api_explorer = API_OPTISCAN
        rpc_explorer_endpoint = f"https://api-optimistic.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_explorer}"
    elif rpc_network == 'arbitrum':
        api_explorer = API_ARBISCAN
        rpc_explorer_endpoint = f"https://api-arbiscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_explorer}"
    elif rpc_network == 'berachain':
        api_explorer = API_GENERAL
        rpc_explorer_endpoint = f'https://api.routescan.io/v2/network/testnet/evm/80085/etherscan/api?module=contract&action=getabi&address={contract_address}&apikey={api_explorer}'
    elif rpc_network ==  'metis':
        rpc_explorer_endpoint = f'https://andromeda-explorer.metis.io/api?module=contract&action=getabi&address={contract_address}'
    elif rpc_network == 'sepolia arbitrum':
        api_explorer = API_GENERAL
        rpc_explorer_endpoint = f"https://api-sepolia.arbiscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={API_GENERAL}"

    return rpc_explorer_endpoint


#//MAIN
class TransactGet():
    def __init__(self, **kwargs):
        self.rpc = kwargs.get('rpc', None)
        self.rpc_url = self.rpc['url']
        self.rpc_chain_id = self.rpc['chain_id']
        self.rpc_network = self.rpc['network']
        self.rpc_token = self.rpc['token']
        self.rpc_explorer = self.rpc['explorer']
        self.EIP_1559 = kwargs.get('EIP_1559', False)
        web3 = kwargs.get('web3', None)
        self.thread_name = thread_name = kwargs.get('thread_name', 'WORKER')
        self.debugmode = kwargs.get('debugmode', False)
        self.lock = kwargs.get('lock', threading.Lock())
        self.shared_lock = kwargs.get('shared_lock', self.lock)
        self.network_list = [config['network'] for config in RPC_CONFIGURATION.values()]
        self.main_dict = MAIN_DICT
        self.main_abi_dict = create_abi_list(main_dict=self.main_dict)

        with self.shared_lock:
            print(f"initializing GET for {thread_name}") if self.debugmode else None   
        
        if web3 is None:
            print(f"{YELLOW}Web3 object not found{RESET} Connecting...")
            web3 = Web3(Web3.HTTPProvider(self.rpc_url))
            if not web3.is_connected():
                print(f"{RED}Web3 object not connected{RESET}")
            else:
                print(f"{GREEN}Web3 object connected!{RESET}")
                
        self.web3 = web3

    def abi(self, address=None, search_all_network=False, debugging=False):
        """Get the ABI of a contract using the address."""
        """Will check if the address is in the default ABI list first."""
        if address in self.main_abi_dict:
            abi = self.main_abi_dict[address]['abi']
            print(F"🎯   Found ABI for : {GREEN}{address}{RESET} in config files") if debugging else None
            return abi
        else:
            explorer_endpoint = set_explorer_endpoint(self.rpc_network, address)
            while True:
                try:
                    response = requests.get(explorer_endpoint)
                    break
                except ConnectionError as e:
                    print(f"{RED}Connection error: {e}{RESET}")
                    time.sleep(60)
                except Exception as e:
                    print(f"{RED}Error fetching ABI: {e}{RESET}")
                    time.sleep(60)
            response_json = response.json()

            #Tries to fetch the ABI from the explorer
            if response_json["status"] == "1":
                response_result = response_json["result"]
                abi = json.loads(response_result)
                print(abi) if debugging else None
                return abi
                
            elif response_json["status"] == "0":
                response_result = response_json.get("result",'')
                if response_result is not None:
                    if 'Contract source code not verified' in response_result:
                        print(f"{self.thread_name} : {address} {RED}Contract source code not verified{RESET}") if debugging else None
                        if search_all_network:
                            self.try_get_abi_all_networks(address)
                    else:
                        print(f"{self.thread_name} {RED}Error fetching ABI for {address} | {response_result}") if debugging else None
                else:
                    print(f"{self.thread_name} {RED}Unknown error fetching ABI for {address} : Using default ABI{RESET}")
            else:
                print(f"{self.thread_name} {RED}Unknown error fetching ABI for {address} : Using default ABI{RESET}")
            return None
    

    def try_get_abi_all_networks(self,address, debugging=False):
        #//BROKEN this is just wrong, leaving it here for reference. function could be useful for searching through all networks
        print(f"{BOLD}Attempting to find ABI for {CYAN}{address}{RESET}{BOLD} on other networks.{RESET}\n")
        abi_found = False
        while True:
            try:
                for network in self.network_list:
                    

                    isFound = self.get_contract_type(address, network, debugging)
                    if isFound:
                            
                        explorer_endpoint = set_explorer_endpoint(self.rpc_network, address)
                        
                        response = requests.get(explorer_endpoint)
                        response_json = response.json()
                        if response_json["status"] == "1":
                            response_result = response_json["result"]
                            abi = json.loads(response_result)
                            print(abi) if debugging else None
                            return abi
                            
                        elif response_json["status"] == "0":
                            response_result = response_json.get("result",'')
                            if response_result is not None:
                                if 'Contract source code not verified' in response_result:
                                    print(f"{BOLD+BLUE}{network}{RESET}: {address} {MY_RED}Contract source not verified{RESET}")

                                else:
                                    print(f"{self.thread_name} {RED}Error fetching ABI for {address} | {response_result}") if debugging else None

            except ConnectionError as e:
                print(f"{RED}Connection error: {e}{RESET}")
                time.sleep(60)
            except Exception as e:
                print(f"{RED}Error fetching ABI: {e}{RESET}")
                time.sleep(60)
            



            
    #//INPROGRESS will attempt to retrieve the type of the address
    def is_contract(self, address, web3):
        code = web3.eth.get_code(address)
        if code == b'':
            print(f"{RED}Not a contract{RESET}") if self.debugmode else None
            return False
        
        return True
    def is_erc20(self, address, web3):
        try:
            # This will create a generic contract object with possible ERC-20 methods
            contract = web3.eth.contract(address=address, abi=ABI_ERC20)
            # If this doesn't raise an exception, it's likely an ERC-20 token
            _ = contract.functions.balanceOf(address).call()
            print(f"{GREEN}ERC20 contract found at {address}{RESET}")
            return True
        except Exception as e:
            if 'Could not transact with/call contract function' in str(e):
                print(f"{RED}Not an ERC20 contract{RESET}") if self.debugmode else None
            return False
    def is_erc721(self, address, web3):
        contract = web3.eth.contract(address=address, abi=ABI_ERC721)
        try:
            # This checks if the balanceOf and ownerOf functions can be called without reverting
            _ = contract.functions.balanceOf(address).call()
            _ = contract.functions.ownerOf(1).call()  # Assumes at least one token exists; adjust as needed
            return True
        except Exception as e:
            print(f"{RED}Not an ERC721 contract{RESET} {e}") if self.debugmode else None
            return False
    def supports_interface(self, contract_address, web3, interface_id=ERC721_INTERFACE_ID):
        contract = web3.eth.contract(address=contract_address, abi=ERC165_ABI)
        try:
            interface_id_bytes = web3.to_bytes(hexstr=interface_id)
            return contract.functions.supportsInterface(interface_id_bytes).call()
        except Exception as e:
            print(f"Error: {e}") if self.debugmode else None
            return False
    def get_contract_type(self, address, network, debugging=False):
        network = 'sepolia'
        web3 = Web3(Web3.HTTPProvider(RPC_CONFIGURATION[network]['url']))
        """Check if the address is a contract or not."""
        isFound = False
        while True:
            if not web3.is_connected():
                print(f"{RED}Web3 object not connected{RESET}")
                time.sleep(10)
            else:
                print(f"{GREEN}Web3 object connected!{RESET} : {BLUE}{network}{RESET}")
                break
        address = self.web3.to_checksum_address(address)
        nonce = self.web3.eth.get_transaction_count(address)
        print(f"Attempting to find ABI for {INFO}{address}{RESET} on other networks.| Nocne {nonce} | Checking : {BLUE}{network.upper()}{RESET}")
        isContract = self.is_contract(address, web3)
        isERC20 = self.is_erc20(address, web3)
        isERC721 = self.is_erc721(address, web3)
        interfaceIDsupported = self.supports_interface(address, web3=web3)
        if isContract or isERC20 or isERC721 or interfaceIDsupported:
            print(f"{GREEN}{address} found on {BLUE}{network} {RESET}")
            isFound = True
        return isFound
    


def main():
    network_choice = 'sepolia arbitrum'
    rpc = RPC_CONFIGURATION[network_choice]
    transact_get = TransactGet(rpc=rpc, debugmode=True)
    transact_get.abi('0xcA11bde05977b3631167028862bE2a173976CA11')
if __name__ == "__main__":
    main()
