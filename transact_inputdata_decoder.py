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
    
    


    #//MAIN FUNCTIOn
    def decode_input_data(self, input, types, debugmode=False):
        # Decode the input data
        decoded_data_list = eth_abi.decode(types, HexBytes(input))

        # Prepare the result list
        result_list = []

        # Iterate over the decoded data to format it
        for decoded_data in decoded_data_list:
            if isinstance(decoded_data, bytes):
                # Convert bytes to hex string prefixed with '0x'
                result_list.append('0x' + decoded_data.hex())
            elif isinstance(decoded_data, tuple):
                # Process tuples which can contain nested bytes
                tuple_list = []
                for item in decoded_data:
                    if isinstance(item, bytes):
                        tuple_list.append('0x' + item.hex())
                    else:
                        tuple_list.append(item)
                result_list.append(tuple(tuple_list))
            else:
                # Directly append other types (like int)
                result_list.append(decoded_data)
        for result in result_list:
            print(f"Type: {type(result)} | Value: {result}") if debugmode else None
        return result_list

    def create_dict(self, names, types, decoded_data, debugmode=False):
        # Check if all lists have the same length
        if len(names) != len(types) or len(names) != len(decoded_data):
            print("Error: Length of names, types, and decoded data do not match")
            return None
        
        # Create dictionary with the required format
        decoded_dict = {}
        for name, type, data in zip(names, types, decoded_data):
            decoded_dict[name] = {'type': type, 'data': data}
        
        print(decoded_dict) if debugmode else None
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
