from Crypto.Hash import keccak
def keccak256(data):
    k = keccak.new(digest_bits=256)
    k.update(data.encode())
    return k.digest()[:4]  # Return the first 4 bytes of the hash

# Function to convert bytes to hexadecimal
def to_hex(data):
    return data.hex()

def calculate_interface_id(*functions):
    interface_id = 0
    for func in functions:
        hashed = int.from_bytes(keccak256(func), 'big')  # Convert bytes to int for XOR
        interface_id ^= hashed
    return hex(interface_id)
erc721_functions = [
    'balanceOf(address)',
    'ownerOf(uint256)',
    'approve(address,uint256)',
    'getApproved(uint256)',
    'setApprovalForAll(address,bool)',
    'isApprovedForAll(address,address)',
    'transferFrom(address,address,uint256)',
    'safeTransferFrom(address,address,uint256)',
    'safeTransferFrom(address,address,uint256,bytes)'
]
ERC721_INTERFACE_ID = calculate_interface_id(*erc721_functions)
print("ERC-721 Interface ID:", ERC721_INTERFACE_ID)
