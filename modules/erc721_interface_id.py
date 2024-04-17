from Crypto.Hash import keccak



"""This module calculates the ERC721 interface ID."""
"""To be used to verify if a contract is ERC721 compliant."""


def keccak256(data):
    k = keccak.new(digest_bits=256)
    k.update(data.encode())
    return k.digest()[:4]  


def to_hex(data):
    return data.hex()

def calculate_interface_id(*functions):
    interface_id = 0
    for func in functions:
        hashed = int.from_bytes(keccak256(func), 'big')
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

