import eth_abi
from eth_utils import decode_hex, to_int, to_bytes, to_text
import codecs
import re
from hexbytes import HexBytes
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'
BLUE = '\033[94m'

#//COMPLETE Short and simple class to decode input data
#//TODO Add more patterns for different types of input data and do additional testing with different types of input data    

class InputDataDecoder:
    def __init__(self):
        self.eth_address_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')
        self.method_id_pattern = re.compile(r'^0x[a-fA-F0-9]{8}$')
        self.hash_pattern = re.compile(r'^0x[a-fA-F0-9]{64}$')
        self.method_id_from_data_pattern = re.compile(r'^(0x[a-fA-F0-9]{8})0{24,}')
        self.other_0x_pattern = re.compile(r'^0x[a-fA-F0-9]{1,6}$')
    
    #//todo
    def decode_input_data_from_tx_hash(self, tx_hash):
        """Will extract the input data from a transaction and decode it using the contract's ABI."""
        """Not completed yet."""
        tx = self.web3.eth.get_transaction(tx_hash)
        input_hex = self.web3.to_hex(tx['input'])
        r_hex = self.web3.to_hex(tx['r'])
        s_hex = self.web3.to_hex(tx['s'])
        v = tx['v']
        print(f"To : {tx['to']} Smart contract")
        print(f"From : {tx['from']}")
        print(f"Nonce : {tx['nonce']}\n")
        print(f"Input : {input_hex}")
        print(f"Value : {tx['value']}\n")
        print(f"R : {r_hex}")
        print(f"S : {s_hex}")
        print(f"V : {v}\n")
        address, abi, contract, ticker = self.set_contract(tx['to'])
        try:
            func_obj, func_params = contract.decode_function_input(tx["input"])
            #//todo : print the decoded function
        except Exception as e:
            print(f"Error decoding function input : {e}")
            return None
        input("Press Enter to continue...")
    


    
    #//COMPLETE
    def parse_input_data(self, input_data, debugmode=True):

        arguments = input_data
        argument_list = [arguments[i:i+64] for i in range(0, len(arguments), 64)]
        if debugmode:
            for arg in argument_list:
                print(f"{BOLD}Argument {RESET} : {CYAN}{arg}{RESET}")
        return argument_list




    def _decode_nested_data(self, data, debugmode=False):
        if isinstance(data, tuple):
            decoded_list = []
            for item in data:
                if debugmode:
                    print("Decoding item:", item)
                decoded_list.append(self._decode_nested_data(item, debugmode))
            return tuple(decoded_list)
        elif isinstance(data, bytes):
            return '0x' + data.hex()
        else:
            return data


    def decode_input_data(self, inputdata, types, debugmode=False):
        decoded_data_list = eth_abi.decode(types, HexBytes(inputdata))
        result_list = []

        for decoded_data in decoded_data_list:
            # Use the recursive function to handle decoding of any data type, including nested tuples
            decoded_result = self._decode_nested_data(decoded_data, debugmode)
            result_list.append(decoded_result)

            # Debugging output
            if debugmode:
                print(f"Decoded data: {decoded_result}")

        return result_list




    #//MAIN FUNCTIOn
    def decode_input_datav1(self, input, types, debugmode=False):
        decoded_data_list = eth_abi.decode(types, HexBytes(input))
        result_list = []
        for decoded_data in decoded_data_list:
            if isinstance(decoded_data, bytes):
                result_list.append('0x' + decoded_data.hex())

            #Handles tuples
            elif isinstance(decoded_data, tuple):
                tuple_list = []
                for item in decoded_data:

                    #Handles nested tuples
                    if isinstance(item, tuple):
                        nested_tuple_list = []
                        print(item) if debugmode else None
                        for entry in item:
                            if isinstance(entry, bytes):
                                nested_tuple_list.append({'0x' + entry.hex()})
                            elif isinstance(entry, tuple):

                                nested_tuple_list.append(entry)
                        tuple_list.append(tuple(nested_tuple_list))

                    #Handles bytes
                    elif isinstance(item, bytes):
                        print(f"0x{item.hex()}") if debugmode else None
                        tuple_list.append('0x' + item.hex())
                    
                    #Handles other types
                    else:
                        print(item) if debugmode else None
                        tuple_list.append(item)

                result_list.append(tuple(tuple_list))
            else:
                result_list.append(decoded_data)
        for result in result_list:
            print(f"{CYAN}Decoded data: {RESET}\n{BLUE}{result}{RESET}") if debugmode else None
        return result_list

    def create_dict(self, names, types, decoded_data, debugmode=False):
        print(f"names : {names}")
        print(f"types : {types}")
        print(f"decoded_data : {decoded_data}")
        if len(names) != len(types) or len(names) != len(decoded_data):
            if debugmode:
                print("Error: Length of names, types, and decoded data do not match")
            return None
        
        decoded_dict = {}
        for name, type_spec, data in zip(names, types, decoded_data):
            if type_spec.endswith('[]'):
                # Remove the array type and process each element in the array
                element_type = type_spec[:-2]  # Remove the '[]' from the type
                if '(' in element_type and ')' in element_type:
                    # Assuming it's a tuple type within the array
                    inner_types = element_type.strip('()').split(',')
                    array_data = []
                    for element in data:
                        tuple_data_with_types = []
                        for item, item_type in zip(element, inner_types):
                            tuple_data_with_types.append({'type': item_type.strip(), 'data': item})
                        array_data.append(tuple_data_with_types)
                    decoded_dict[name] = {'type': type_spec, 'data': array_data}
                else:
                    # Simple array
                    decoded_dict[name] = {'type': type_spec, 'data': [self._decode_nested_data(d, debugmode) for d in data]}
            else:
                # Single item processing
                decoded_dict[name] = {'type': type_spec, 'data': self._decode_nested_data(data, debugmode)}


        
        return decoded_dict
        




    def decode_this(self, input_data, types, names, debugmode=False):
        decoded_data = self.decode_input_data(input_data, types, debugmode)
        decoded_dict = self.create_dict(names, types, decoded_data, debugmode)
        return decoded_dict
            
            
        
        






def main():
    input_data='000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000a00000000000000000000000000000000000000000000000000000000066188f4b00000000000000000000000000000000000000000000000000000000000000040a00060400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000034000000000000000000000000000000000000000000000000000000000000003c0000000000000000000000000000000000000000000000000000000000000016000000000000000000000000057e114b691db790c35207b2e685d4a43181e6061000000000000000000000000ffffffffffffffffffffffffffffffffffffffff00000000000000000000000000000000000000000000000000000000664019eb00000000000000000000000000000000000000000000000000000000000000000000000000000000000000003fc91a3afd70395cd496c647d5a6cc9d4b2b7fad00000000000000000000000000000000000000000000000000000000661893f300000000000000000000000000000000000000000000000000000000000000e00000000000000000000000000000000000000000000000000000000000000041d098e33f844e91ed8bc0818548fe19bf5969c500e4197f42fa871327e34dba6914ca213f82a193515d442c989e7797becccad1aa17df8fb6dbc8c40d9fc4829f1c00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000012000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000d0b0121ae45f81000000000000000000000000000000000000000000000000000000000001457c367a00000000000000000000000000000000000000000000000000000000000000a00000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000004257e114b691db790c35207b2e685d4a43181e6061000bb8c02aaa39b223fe8d0a0e5c4f27ead9083c756cc20001f4dac17f958d2ee523a2206206994597c13d831ec70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000060000000000000000000000000dac17f958d2ee523a2206206994597c13d831ec700000000000000000000000037a8f295612602f2774d331e562be9e61b83a32700000000000000000000000000000000000000000000000000000000000000190000000000000000000000000000000000000000000000000000000000000060000000000000000000000000dac17f958d2ee523a2206206994597c13d831ec7000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000001457c367a'
    types = ["bytes","bytes[]","uint256"]
    names = ["commands","inputs","deadline"]
    function_signature = 'execute(bytes commands,bytes[] inputs,uint256 deadline)'
    
    inputdecoder = InputDataDecoder()
    decoded_data = inputdecoder.decode_input_data(input_data, types)
    decoded_dict = inputdecoder.create_dict(names, types, decoded_data)




if __name__ == "__main__":
    main()
