import pandas as pd
import json
from eth_utils.abi import function_abi_to_4byte_selector
import time
from pprint import pprint
import os
import csv
import re
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.')))
#print(sys.path)
from modules.api_4bytes import get4Bytes
from modules.transact_decode import Decoder
from modules.transact_get import TransactGet
from modules.transact_methodid import TransactMethodID
from config.rpc_config import RPC_CONFIGURATION
from modules.transact_inputdata_decoder import InputDataDecoder
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BOLD = "\033[1m"
DIVIDER = '-' * 100
PINK = "\033[95m"   



#//TODO Clean the code and remove unnecessary functions
#//BROKEN : Find the issue with tuple not being decoded by eth_abi

def cls():
    if os.name == 'nt':
        os.system('cls')

class FilterDF():
    def __init__(self, rpc=None, filename='data/events.json'):
        with open(filename, 'r') as f:
            data = pd.read_json(f, lines=True)

        self.df = pd.json_normalize(data.to_dict(orient="records"))
        self.df = self.df.dropna(axis=1, how='all')
        self.df.to_csv('data/events.csv', index=False)
        pd.set_option('display.max_colwidth', 30)
        pd.set_option('display.max_columns', None)
        self.filename = filename
        self.eth_address_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')
        self.method_id_pattern = re.compile(r'^0x[a-fA-F0-9]{8}$')
        self.hash_pattern = re.compile(r'^0x[a-fA-F0-9]{64}$')
        self.method_id_from_data_pattern = re.compile(r'^(0x[a-fA-F0-9]{8})0{24,}')
        self.other_0x_pattern = re.compile(r'^0x[a-fA-F0-9]{1,6}$')
        self.rpc = rpc if rpc else None
        self.rpc_network = rpc['network'] if rpc else None
        self.rpc_url = rpc['url'] if rpc else None
        self.rpc_chain_id = rpc['chain_id'] if rpc else None
        self.get4bytes = get4Bytes()
        self.decoder = Decoder(rpc=self.rpc)
        self.get = TransactGet(rpc=self.rpc)
        self.getmeth = TransactMethodID(rpc=self.rpc, get=self.get)
        self.inputdecoder = InputDataDecoder()
        self.contract_address = None
        self.abi = None
        self.dict_filename = 'data/web3_readcalls.csv'

    
    #//HELPER_FUNCTIONS
    def get_entry(self, index, debugmode=False):
        """
        Returns the entry at a given index.
        """
        filtered_df = self.df.dropna(axis=1, how='all')
        entry = filtered_df.iloc[index].dropna()
        print(entry) if debugmode else None

        return entry
    
    def get_value(self, index, key):
        """
        Returns the value of a given key at a given index.
        """
        entry = self.get_entry(index)
        value = entry.get(key, None)
        print(value)
        return value
    
    def get_entry_keys(self, index):
        """
        Returns the keys of the entry at a given index.
        """
        entry = self.get_entry(index)
        entry_keys = entry.keys()
        #print(entry_keys)
        entry_keys = entry.index.tolist()
        print(entry_keys)
        return entry.keys()
    
    def entry_details(self, index):
        """
        Returns the details of an entry at a given index.
        """
        entry = self.get_entry(index)
        if not isinstance(entry, pd.Series):
            entry = pd.Series(entry)
            
        # Iterate over the Series as key-value pairs
        for key, value in entry.items():
            truncated_key = (str(key)[:27] + '...') if len(str(key)) > 30 else str(key)
            truncated_value = (str(value)[:97] + '...') if len(str(value)) > 100 else str(value)
            print(f"{truncated_key:<40}: {truncated_value:<110}")
        return entry
    
    def filter_by_method(self, method_value='Network.requestWillBeSentExtraInfo'):
        """
        Filters the DataFrame for entries where the 'method' equals the specified method_value.
        Network.requestWillBeSentExtraInfo
        Network.requestWillBeSent
        Network.responseReceived
        Network.responseReceivedExtraInfo
        Network.Request
        Network.Headers
        Network.Cookie
        Network.CookieParam

        """
        filtered_df = self.df[self.df['method'] == method_value]
        return filtered_df
    
    def parse_json_from_key(self, index, key):
        """
        Attempts to parse a JSON string contained in a specified key for a given entry.
        If successful, returns the parsed JSON as a dictionary or list of dictionaries.
        If the key does not contain a valid JSON string, returns None.
        """
        # Retrieve the entry
        entry = self.get_entry(index)
        if key in entry and isinstance(entry[key], str):
            try:
                # Attempt to parse the JSON string
                parsed_json = json.loads(entry[key])
                # Replace the string in the entry with the parsed JSON
                entry[key] = parsed_json
                for key, value in parsed_json.items():
                    print(f"{key}: {value}")
                return parsed_json
            except json.JSONDecodeError:
                # The string could not be parsed as JSON
                print(f"Could not parse JSON from key '{key}'.")
                return None
        else:
            print(f"Key '{key}' not found or not a string.")
            return None
        
    def save_dict_to_csv(self, result_list ):
        print(f"\n{BOLD}Saving to {self.dict_filename} in progress{RESET}...")
        df = pd.DataFrame(result_list)
        df = df.drop_duplicates(subset=['data'])
        print(f"{BOLD}Total duplicates removed: {RED}{len(result_list) - len(df)}{RESET}")
        df.to_csv(self.dict_filename, index=False)
        print(f"{BOLD}Saved to {GREEN}{self.dict_filename}{RESET}")

    def print_list_of_dicts(self, list_of_dicts, debugmode=False):
        """
        Pretty-prints a list of dictionaries.
        """
        for i, d in enumerate(list_of_dicts):
            print(f"\n{DIVIDER}\nDictionary #{i}\n{DIVIDER}")
            none_value = False
            for key, value in d.items():
                if value is None:
                    none_value = True
                    print(f"{BLUE}{BOLD}{key}{RESET}: {YELLOW}{value}{RESET}")
                else:
                    print(f"{BLUE}{BOLD}{key}{RESET}: {CYAN}{value}{RESET}")
            print(DIVIDER)
            if debugmode == True and none_value == True:
                input('Press Enter to continue...')
    
    def pretty_print(self, data, indent=0, debugmode=False):
        """
        Recursively prints nested dictionaries, lists, or tuples with indentation.
        """
        spacer = ' ' * indent
        if isinstance(data, dict):
            for key, value in data.items():
                print(f"{spacer}{BOLD}{key}{RESET}:", end=' ')
                if isinstance(value, (dict, list, tuple)):
                    print()
                    self.pretty_print(value, indent + 4, debugmode)
                else:
                    print(f"{BOLD+BLUE}{value}{RESET}")
        elif isinstance(data, (list, tuple)):
            for index, item in enumerate(data):
                if isinstance(item, (dict, list, tuple)):
                    print(f"{spacer}{BOLD}Item{RESET} {CYAN}{index}{RESET}:")
                    self.pretty_print(item, indent + 4, debugmode)
                else:
                    print(f"{spacer}{BOLD}Item{RESET} {CYAN}{index}{RESET}: {item}")
        else:
            print(f"{spacer}{data}")

        if debugmode and indent == 0:
            input('Press Enter to continue...')


    def csv_to_dict_list(self, filename=None):
        if filename is None:
            filename = self.dict_filename
        dict_list = []
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dict_list.append(row)

        return dict_list






    #//MAIN_FUNCTIONS
    def extract_web3_readcalls(self, debugmode=False):
        """
        extracts and parse data for web3 read calls
        Handles cases where postData_str might be NaN or not a string.
        Returns a list of dictionaries containing the extracted data.   
        """
        print(f"{BOLD}Extracting web3 read calls from {CYAN}{self.filename}{RESET}...{RESET}")
        result_list = []
        counter = 0 
        for _, row in self.df.iterrows():
            postData_str = row.get('params.request.postData')

            # Proceed only if postData_str is a non-empty string
            if isinstance(postData_str, str) and postData_str:
                result = {}


                try:
                    postData_json = json.loads(postData_str)
                    params_list = postData_json.get('params', [])
                    index = row.name
                    method = postData_json.get('method', None)
                    if params_list and len(params_list) > 0:
                        counter += 1
                        result['index'] = index
                        result['methodid'] = None
                        result['data'] = ''
                        result['details'] = ''
                        result['to'] = ''
                        result['method'] = method
                        result['ExtraParams'] = None

                        if isinstance(params_list, list):
                            first_param = params_list[0]
                            result['ExtraParams'] = params_list[1] if len(params_list) > 1 else None  
                            
                            if len(params_list) > 2: #//todo remove. for debugging only
                                print(f"{RED}More than 2 params:{RESET} {params_list}") 
                                input('Press Enter to continue...')
                            if isinstance(first_param, dict):
                                #In practice if first_param is a dict, it is a call. There will be a methodID.
                                #We expect the first_param to have a 'data' and 'to' key
                                data = first_param.get('data',None)
                                to = first_param.get('to',None)
                                if data and to: 
                                    if self.method_id_from_data_pattern.match(data):
                                        result['methodid'] = self.method_id_from_data_pattern.match(data).group(1)
                                        result['data'] = data[10:]
                                    elif self.method_id_pattern.match(data):
                                        result['methodid'] = self.method_id_pattern.match(data).group()
                                        result['data'] = ''
                                    result['to'] = to
                                    result['details'] = 'call'

                            elif isinstance(first_param, str):
                                #In practice if first_param is a string, it is either an eth_address, tx_hash or unknown. There will be no methodID.
                                #If will not remove the regex checks for methodID in case of future changes.
                                if self.method_id_from_data_pattern.match(first_param):
                                    result['methodid'] = self.method_id_from_data_pattern.match(first_param).group(1)
                                    result['data'] = first_param[10:]
                                    result['details'] = 'methodID'
                                elif self.method_id_pattern.match(first_param):
                                    result['methodid'] = self.method_id_pattern.match(first_param).group(1)
                                    result['data'] = first_param
                                    result['details'] = 'methodID'
                                elif self.eth_address_pattern.match(first_param):
                                    result['data'] = first_param
                                    result['details'] = 'eth_address'
                                elif self.hash_pattern.match(first_param):
                                    result['data'] = first_param
                                    result['details'] = 'tx_hash'
                                elif self.other_0x_pattern.match(first_param):
                                    result['data'] = first_param
                                    result['details'] = '0x_unknown'
                                else:
                                    result['data'] = ''
                                    result['details'] = first_param

                                
                            else:
                                print(f"{YELLOW}Could not parse param: {first_param}{RESET}")  

                            #Exclude empty data
                            if result['data'] is not None or result['data'] != '':
                                #Exclude eth_getTransactionReceipt, eth_getBalance, eth_getTransactionCount to focus on contract calls
                                if result['method'] not in ['eth_getTransactionReceipt', 'eth_getBalance', 'eth_getTransactionCount']:
                                    result_list.append(result)



                except json.JSONDecodeError:
                    print(f"Could not parse JSON from postData_str: {postData_str}")
                    continue
        list_count = len(result_list)
        excluded_count = counter - list_count
        print(f"{BOLD}Total https requests analysed: {CYAN}{counter}{RESET}")
        print(f"{BOLD}Removed entries:{YELLOW}{excluded_count}{RESET}")
        print(f"{BOLD}Total web3 read calls extracted:{GREEN}{list_count}{RESET}")
        if debugmode:
            print(f"Total length of result_list: {CYAN}{len(result_list)}{RESET}")
            self.print_list_of_dicts(result_list)
        self.save_dict_to_csv(result_list)
        return result_list
    


    #//INPROGRESS
    def parse_and_decode(self, debugmode=True):
        """
        Parses and decodes the data in a dictionary.
        """

        input_dict = self.csv_to_dict_list()
        count = 0
        for item in input_dict:

            #region Initialise variables
            data = item.get('data', None)
            index = item.get('index', None)
            methodid = item.get('methodid', None)
            contract_address = item.get('to', None)

            print(f"\n{PINK}{DIVIDER}\n{BOLD}  Parsing and decoding dictionary # {BLUE}{count}{RESET}{PINK}\n{DIVIDER}{RESET}")
            count += 1
            if contract_address is None or contract_address == '':
                print(f"{RED}No contract address found in the dictionary.{RESET}")
                print(item)
            #endregion
            
            #region getABI Get the ABI only if the contract address has changed (optimization)
            if contract_address != self.contract_address:
                self.contract_address = contract_address
                self.abi = self.get.abi(address=contract_address, debugging=debugmode)
                if self.abi is None:
                    print(f"{RED}No ABI found for contract address: {contract_address}{RESET}")
                    print(input_dict)
                    return None
                abi_dict = self.getmeth.abi_to_functions_dict(self.abi, debugmode)
            #endregion
            
            
            
            
            if data is None or data == '' and methodid is not None:
                print(f"{RED}No data found in the dictionary.{RESET}")
                print(item)
                #todo : attempt to get signature from methodID
                continue
            for item in abi_dict:
                if item['selector'] == methodid:
                    print(f"{GREEN}Found methodID in ABI{RESET} : {CYAN}{methodid}{RESET} | Signature : {CYAN+BOLD}{item['signature']}{RESET}")
                    ethcall_dict = item
                    break
            if ethcall_dict is None:
                input('Press Enter to continue...')
            ethcall_params = ethcall_dict.get('params', None)
            ethcall_signature = ethcall_dict.get('signature', None)
            ethcall_names = ethcall_dict.get('names', None)
            ethcall_types = ethcall_dict.get('types', None)
            
            
            

            #functionParam = self.decoder.methodID_to_functionParams(methodID=methodID, abi=self.abi, debugmode=debugmode)
            #functionSignature = self.get4bytes.get_functionSignature_from_methodID(methodID, debugmode=debugmode)
            
            
            
            
            
            if 1==2:
                if functionParam is None:
                    print(f"{RED}Cant find corresponding signature{RESET} : {CYAN}{methodid}{RESET}. Please check ABI{RESET}")
                    print(item)
                    return None
                else:
                    functionParam = self.decoder.parse_function_signature(functionParam)
            
            #Decode baby!
            argumentsList = self.inputdecoder.parse_input_data(data, debugmode) #//DEBUG
            interpreted_args = self.inputdecoder.decode_this(data, ethcall_types, ethcall_names, debugmode)
            
            
            if interpreted_args is None:
                print(f"{RED}Could not interpret arguments.{RESET}")
                print(item)
                return None
            print(f"\n{DIVIDER}\n{CYAN}Index: {index}{RESET}\n{DIVIDER}")
            self.pretty_print(interpreted_args)
            print(f"{DIVIDER}")

        return









# Demonstration of usage
def main():
    cls()
    network_choice = 'berachain'
    rpc = RPC_CONFIGURATION[network_choice]
    filter_df = FilterDF(rpc=rpc, filename='data/events.json')
    filter_df.extract_web3_readcalls(debugmode=True)
    #time.sleep(1)
    cls()
    filter_df.parse_and_decode(debugmode=True)

    
    
    
    
    
    #filter_df.get_entry(472, debugmode=True)
    #filter_df.get_entry_keys(472)
    #filter_df.get_value(472, 'params.request.postData')
    #filter_df.parse_json_from_key(472, 'params.request.postData')
    #eth_call_df = filter_df.filter_by_method('Network.requestWillBeSent')
    #print(eth_call_df)
    #filter_df.entry_details(76)



if __name__ == '__main__':
    main()
