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
from modules.my_colors import *
from modules.transact_methodid import TransactMethodID
from config.rpc_config import RPC_CONFIGURATION
from modules.transact_inputdata_decoder import InputDataDecoder
from modules.extract_variables_from_file import FileExtractor
DIVIDER = '-' * 100





def cls():
    if os.name == 'nt':
        os.system('cls')

class FilterDF():
    def __init__(self, rpc=None, filename='data/events.json', abi_file_name='config/abi_list.py', debugmode=False):
        with open(filename, 'r') as f:
            data = pd.read_json(f, lines=True)

        self.df = pd.json_normalize(data.to_dict(orient="records"))
        self.df = self.df.dropna(axis=1, how='all')
        self.df.to_csv('events.csv', index=False)
        pd.set_option('display.max_colwidth', 30)
        pd.set_option('display.max_columns', None)
        self.filename = filename
        self.output_dict_filename = 'decoded_events.csv'
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
        self.dict_filename = 'web3_readcalls.csv'
        self.fileextractor = FileExtractor(filename = abi_file_name)
        self.variable_dict = self.fileextractor.get_variables_values() 

    
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
    
    def pretty_print(self, data, item=None, indent=0, count=None, debugmode=False):
        """
        Recursively prints nested dictionaries, lists, or tuples with indentation.
        """
        PADDING = " " * 30
        BRIGHT = "\033[1m"
        methodid = item.get('methodid', None) if item is not None else None
        signature = item.get('signature', None) if item is not None else None
        index = item.get('index', None) if item is not None else None
        contract_address = item.get('to', None) if item is not None else None
        method = item.get('method', None) if item is not None else None
        function_name = item.get('function_name', None) if item is not None else None
        info = item.get('details', None) if item is not None else None
        if item is not None:
            details = ''
            details += (f"\n\n{BOLD+PINK+BRIGHT}{DIVIDER}\n{BOLD}{PADDING}Parsing and decoding dictionary # {BLUE}{count}{RESET}{PINK}\n{DIVIDER}{RESET}\n") if count is not None else ''
            details += (f"{BOLD}Index{RESET} : {BOLD+CYAN}{index}{RESET}\n") if index is not None else ''
            details += (f"{BOLD}MethodID{RESET} : {BOLD+CYAN}{methodid}{RESET}\n") if methodid is not None and methodid != '' else ''
            details += (f"{BOLD}Function called{RESET} : {BOLD+CYAN}{function_name}{RESET}\n") if function_name is not None else ''
            details += (f"{BOLD}Signature{RESET} : {BOLD+CYAN}{signature}{RESET}\n") if signature is not None else ''
            details += (f"{BOLD}Method{RESET} : {BOLD+CYAN}{method}{RESET}\n") if method is not None else ''
            details += (f"{BOLD}Contract Address{RESET} : {BOLD+CYAN}{contract_address}{RESET}\n") if contract_address is not None and contract_address != '' else ''
            details += (f"{DIVIDER}")
            print(details)
            if data is None or data == '' or data == {} or data == []:
                print(f"{BOLD}Data{RESET}: {YELLOW}None{RESET}")
                print(f"{DIVIDER}\n\n")
                return
            elif contract_address == '' or contract_address is None:
                print(f"{BOLD}Eth call{RESET}: {CYAN}{method}{RESET}")
                print(f"{BOLD}Details{RESET}: {CYAN}{info}{RESET}")
                print(f"{BOLD}Data{RESET}: {CYAN}{data}{RESET}")
                print(f"{DIVIDER}\n\n")
                return
        if data is not None and data != '' and data != {} or data != []:
            spacer = ' ' * indent
            if isinstance(data, dict):
                for key, value in data.items():
                    if value is not None:
                        print(f"{spacer}{BOLD}{key}{RESET}:", end=' ')
                        if isinstance(value, (dict, list, tuple)):
                            print()
                            self.pretty_print(value, item=None, indent=indent + 4, count=None, debugmode=debugmode)
                        else:
                            print(f"{BOLD+BLUE}{value}{RESET}")
            elif isinstance(data, (list, tuple)):
                for index, entry in enumerate(data):
                    if entry is not None:
                        if isinstance(entry, (dict, list, tuple)):
                            print(f"{spacer}{BOLD}Item{RESET} {CYAN}{index}{RESET}:")
                            self.pretty_print(entry, item=None, indent = indent + 4, count=None, debugmode=debugmode)
                        else:
                            print(f"{spacer}{BOLD}Item{RESET} {CYAN}{index}{RESET}: {entry}")
            else:
                print(f"{spacer}{data}")

        if item is not None:
            print(f"{DIVIDER}\n\n")
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

    def dict_list_to_csv(self, data, filename=None):
        if filename is None:
            filename = self.output_dict_filename
        if os.path.exists(filename):
            mode='a'
        else:
            mode='w'
        with open(filename, mode=mode, newline='') as file:
            headers = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for entry in data:
                writer.writerow(entry)

        print(f"Data has been written to {GREEN}{filename}{RESET}")




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
                            
                            if (result['data'] is None or result['data'] == '') and (result['methodid'] is None or result['methodid'] == '') and (result['to'] is None or result['to'] == ''):
                                print(f"{YELLOW}Empty data, methodid and to. Skipping...{RESET}")
      
                                continue
                            if (result['data'] is not None or result['data'] != ''):
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
        time.sleep(1)
        return result_list
    


    #//INPROGRESS
    def parse_and_decode(self, debugmode=True):
        """
        Parses and decodes the data in a dictionary.
        """

        input_dict = self.csv_to_dict_list()
        output_dict = []
        all_abi_dict = self.getmeth.create_functions_dict_dataset()
        count = 0
        for item in input_dict:
            result_dict = {}
            ethcall_dict = None
            interpreted_args = None
            abi_dict = None
            #region Initialise variables
            data = item.get('data', None)
            index = item.get('index', None)
            methodid = item.get('methodid', None)
            contract_address = item.get('to', None)
            method = item.get('method', None)
            details = item.get('details', None)
            no_data_call = False

            if (details == '0x_unknown' and (methodid == '' or methodid is None)) or details == 'eth_address' or details == 'tx_hash' or details == 'methodID':
                self.pretty_print(data, item=item, count=count, debugmode=debugmode)
                continue                

                

            #region getABI Get the ABI only if the contract address has changed (optimization)
            if contract_address != self.contract_address and contract_address not in ('', None):
                self.contract_address = contract_address
                self.abi = self.get.abi(address=contract_address, debugging=debugmode)
                if self.abi is None:
                    print(f"{RED}No ABI found for contract address: {contract_address} on etherscan.{RESET}") if debugmode else None
            if self.abi is not None and self.abi != '':
                abi_dict_list = self.getmeth.abi_to_functions_dict(self.abi, debugmode)
                abi_dict_list = [abi_dict_list]
            else:
                abi_dict_list = list(all_abi_dict.values())
            #endregion
            
            
        
            ethcall_dict = find_match_in_abi(abi_dict_list, methodid)
            if ethcall_dict is None:
                input('Press Enter to continue...')

            print(f"{GREEN}ABI found for contract address: {contract_address} on dataset{RESET}") if debugmode else None
            #//TODO handle the case where multiple matches are found
            ethcall_signature = ethcall_dict[0].get('signature', None)
            ethcall_names = ethcall_dict[0].get('names', None)
            ethcall_types = ethcall_dict[0].get('types', None)
            if ethcall_signature is not None and item.get('signature', None) is None:
                item['signature'] = ethcall_signature

            count += 1
            
            
            interpreted_args = self.inputdecoder.decode_this(data, ethcall_types, ethcall_names, debugmode) #//MAIN
            
            
            if interpreted_args is None:
                print(f"{RED}Could not interpret arguments.{RESET}")
                print(item)
                return None

            self.pretty_print(interpreted_args, item=item, count=count, debugmode=debugmode) 
            result_dict['item'] = item
            result_dict['interpreted_args'] = interpreted_args
            
            output_dict.append(result_dict)
            time.sleep(2)
        self.dict_list_to_csv(output_dict)
        return
    

    def create_call_dict(self, item, type=None):
        """
        Creates a dictionary for a call.
        """
        call_dict = {}
        call_dict['index'] = item.get('index', None)
        call_dict['methodid'] = item.get('methodid', None)
        call_dict[type] = item.get('data', None)
        call_dict['details'] = item.get('details', None)
        call_dict['contract_address'] = item.get('to', None)
        call_dict['method'] = item.get('method', None)
        call_dict['ExtraParams'] = item.get('ExtraParams', None)
        return call_dict


def find_match_in_abi(abi_dict_list, methodid, debugmode=False):
    unique_entries = {}

    for abi_dict in abi_dict_list:
        for entry in abi_dict:
            if entry.get('selector') == methodid:
                function_name = entry.get('function_name')
                signature = entry.get('signature')

                if signature not in unique_entries:
                    unique_entries[function_name] = entry

    for key, value in unique_entries.items():
        print(f"{key}: {value}")  if debugmode else None  
    result = list(unique_entries.values())
    if len(result) == 1:
        return result
    elif len(result) > 1:
        print(f"{RED}Multiple matches found for methodID: {methodid}{RESET}")
        for entry in result:
            print(f"{entry.get('function_name')}")
        return result
    else:
        return None







# Demonstration of usage
def main():
    cls()
    network_choice = 'berachain'
    rpc = RPC_CONFIGURATION[network_choice]
    filter_df = FilterDF(rpc=rpc, filename='data/events.json')
    filter_df.extract_web3_readcalls(debugmode=False)
    cls()
    filter_df.parse_and_decode(debugmode=False)

    
    
    
    
    
    #filter_df.get_entry(472, debugmode=True)
    #filter_df.get_entry_keys(472)
    #filter_df.get_value(472, 'params.request.postData')
    #filter_df.parse_json_from_key(472, 'params.request.postData')
    #eth_call_df = filter_df.filter_by_method('Network.requestWillBeSent')
    #print(eth_call_df)
    #filter_df.entry_details(76)



if __name__ == '__main__':
    main()
