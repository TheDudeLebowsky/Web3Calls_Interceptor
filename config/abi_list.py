# pylint: skip-file




# This is just an example of how the ABI list can be structured.
#//MAIN MULTICHAIN ABI :
#region multichain abi
#Add ABIs that are not network specific here
ABI_MY_FAUCET = [
    {"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_address","type":"address"}],"name":"AddressAdded","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_address","type":"address"},{"indexed":False,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"FundsDeposited","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_address","type":"address"},{"indexed":False,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"FundsWithdrawn","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_address","type":"address"}],"name":"PoweruserAdded","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_address","type":"address"}],"name":"PoweruserRemoved","type":"event"},{"inputs":[{"internalType":"address","name":"_newAddress","type":"address"}],"name":"addAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_newAddresses","type":"address[]"}],"name":"addAddresses","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newPoweruser","type":"address"}],"name":"addPoweruser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"checkPoweruser","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getBalanceInEther","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPowerusers","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getWhitelist","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"isWhitelisted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_addressToRemove","type":"address"}],"name":"removeAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_poweruserToRemove","type":"address"}],"name":"removePoweruser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawAsOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawAsPoweruser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawAsUser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]

ABI_AAVE_ORACLE = [
  {
    "inputs": [
      {
        "internalType": "contract IPoolAddressesProvider",
        "name": "provider",
        "type": "address"
      },
      {
        "internalType": "address[]",
        "name": "assets",
        "type": "address[]"
      },
      {
        "internalType": "address[]",
        "name": "sources",
        "type": "address[]"
      },
      {
        "internalType": "address",
        "name": "fallbackOracle",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "baseCurrency",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "baseCurrencyUnit",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "asset",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "source",
        "type": "address"
      }
    ],
    "name": "AssetSourceUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "baseCurrency",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "baseCurrencyUnit",
        "type": "uint256"
      }
    ],
    "name": "BaseCurrencySet",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "fallbackOracle",
        "type": "address"
      }
    ],
    "name": "FallbackOracleUpdated",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "ADDRESSES_PROVIDER",
    "outputs": [
      {
        "internalType": "contract IPoolAddressesProvider",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "BASE_CURRENCY",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "BASE_CURRENCY_UNIT",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "asset",
        "type": "address"
      }
    ],
    "name": "getAssetPrice",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address[]",
        "name": "assets",
        "type": "address[]"
      }
    ],
    "name": "getAssetsPrices",
    "outputs": [
      {
        "internalType": "uint256[]",
        "name": "",
        "type": "uint256[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getFallbackOracle",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "asset",
        "type": "address"
      }
    ],
    "name": "getSourceOfAsset",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address[]",
        "name": "assets",
        "type": "address[]"
      },
      {
        "internalType": "address[]",
        "name": "sources",
        "type": "address[]"
      }
    ],
    "name": "setAssetSources",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "fallbackOracle",
        "type": "address"
      }
    ],
    "name": "setFallbackOracle",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]

ABI_ERC721 = [
    
    
    {"status":"1","message":"OK","result":"[{\"inputs\":[{\"internalType\":\"bytes32\",\"name\":\"allowlist_\",\"type\":\"bytes32\"},{\"internalType\":\"string\",\"name\":\"name_\",\"type\":\"string\"},{\"internalType\":\"string\",\"name\":\"symbol_\",\"type\":\"string\"},{\"internalType\":\"contract IERC20\",\"name\":\"paymentToken_\",\"type\":\"address\"},{\"components\":[{\"internalType\":\"uint256\",\"name\":\"native\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"erc20\",\"type\":\"uint256\"}],\"internalType\":\"struct Ticket.MintCost\",\"name\":\"mintCost_\",\"type\":\"tuple\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"inputs\":[],\"name\":\"AccountBalanceOverflow\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"AlreadyClaimed\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"BalanceQueryForZeroAddress\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"InvalidProof\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"NotOwnerNorApproved\",\"type\":\"error\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"}],\"name\":\"OwnableInvalidOwner\",\"type\":\"error\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"}],\"name\":\"OwnableUnauthorizedAccount\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"TokenAlreadyExists\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"TokenDoesNotExist\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"TransferFromIncorrectOwner\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"TransferToNonERC721ReceiverImplementer\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"TransferToZeroAddress\",\"type\":\"error\"},{\"inputs\":[],\"name\":\"URIQueryForNonexistentToken\",\"type\":\"error\"},{\"anonymous\":False,\"inputs\":[{\"indexed\":True,\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"indexed\":True,\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"},{\"indexed\":True,\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"}],\"name\":\"Approval\",\"type\":\"event\"},{\"anonymous\":False,\"inputs\":[{\"indexed\":True,\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"indexed\":True,\"internalType\":\"address\",\"name\":\"operator\",\"type\":\"address\"},{\"indexed\":False,\"internalType\":\"bool\",\"name\":\"isApproved\",\"type\":\"bool\"}],\"name\":\"ApprovalForAll\",\"type\":\"event\"},{\"anonymous\":False,\"inputs\":[{\"indexed\":False,\"internalType\":\"string\",\"name\":\"uri\",\"type\":\"string\"}],\"name\":\"BaseURISet\",\"type\":\"event\"},{\"anonymous\":False,\"inputs\":[{\"indexed\":True,\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"indexed\":False,\"internalType\":\"bytes32\",\"name\":\"root\",\"type\":\"bytes32\"},{\"indexed\":False,\"internalType\":\"uint256\",\"name\":\"index\",\"type\":\"uint256\"}],\"name\":\"Claimed\",\"type\":\"event\"},{\"anonymous\":False,\"inputs\":[{\"indexed\":True,\"internalType\":\"address\",\"name\":\"previousOwner\",\"type\":\"address\"},{\"indexed\":True,\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"OwnershipTransferred\",\"type\":\"event\"},{\"anonymous\":False,\"inputs\":[{\"indexed\":False,\"internalType\":\"bool\",\"name\":\"generated\",\"type\":\"bool\"}],\"name\":\"SetGenerated\",\"type\":\"event\"},{\"anonymous\":False,\"inputs\":[{\"indexed\":True,\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"indexed\":True,\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"indexed\":True,\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"}],\"name\":\"Transfer\",\"type\":\"event\"},{\"inputs\":[],\"name\":\"allowlist\",\"outputs\":[{\"internalType\":\"bytes32\",\"name\":\"\",\"type\":\"bytes32\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"}],\"name\":\"approve\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"}],\"name\":\"balanceOf\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"result\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"buy\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"index_\",\"type\":\"uint256\"},{\"internalType\":\"bytes32[]\",\"name\":\"proof_\",\"type\":\"bytes32[]\"}],\"name\":\"claim\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"claimAmount\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"index_\",\"type\":\"uint256\"}],\"name\":\"claimed\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"}],\"name\":\"getApproved\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"result\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"hasMinted\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"operator\",\"type\":\"address\"}],\"name\":\"isApprovedForAll\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"result\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"isGenerated\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"mintCost\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"native\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"erc20\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"name\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"}],\"name\":\"ownerOf\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"result\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"paymentToken\",\"outputs\":[{\"internalType\":\"contract IERC20\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"realOwner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"}],\"name\":\"safeTransferFrom\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"data\",\"type\":\"bytes\"}],\"name\":\"safeTransferFrom\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bytes32\",\"name\":\"allowlist_\",\"type\":\"bytes32\"}],\"name\":\"setAllowList\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"operator\",\"type\":\"address\"},{\"internalType\":\"bool\",\"name\":\"isApproved\",\"type\":\"bool\"}],\"name\":\"setApprovalForAll\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"string\",\"name\":\"baseURI_\",\"type\":\"string\"}],\"name\":\"setBaseURI\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"claimAmount_\",\"type\":\"uint256\"}],\"name\":\"setClaimAmount\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bool\",\"name\":\"generated_\",\"type\":\"bool\"}],\"name\":\"setGenerated\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"components\":[{\"internalType\":\"uint256\",\"name\":\"native\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"erc20\",\"type\":\"uint256\"}],\"internalType\":\"struct Ticket.MintCost\",\"name\":\"mintCost_\",\"type\":\"tuple\"}],\"name\":\"setMintCost\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"contract IERC20\",\"name\":\"paymentToken_\",\"type\":\"address\"}],\"name\":\"setPaymentToken\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bytes4\",\"name\":\"interfaceId\",\"type\":\"bytes4\"}],\"name\":\"supportsInterface\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"result\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"symbol\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"tokenId\",\"type\":\"uint256\"}],\"name\":\"tokenURI\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"}],\"name\":\"transferFrom\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"transferLowerOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"transferOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newRealOwner\",\"type\":\"address\"}],\"name\":\"transferRealOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"withdraw\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"stateMutability\":\"payable\",\"type\":\"receive\"}]"}]

ABI_MULTICALL = [
                {
                    "inputs": [
                    {
                        "components": [
                        {
                            "internalType": "address",
                            "name": "target",
                            "type": "address"
                        },
                        {
                            "internalType": "bytes",
                            "name": "callData",
                            "type": "bytes"
                        }
                        ],
                        "internalType": "struct Multicall3.Call[]",
                        "name": "calls",
                        "type": "tuple[]"
                    }
                    ],
                    "name": "aggregate",
                    "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "blockNumber",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bytes[]",
                        "name": "returnData",
                        "type": "bytes[]"
                    }
                    ],
                    "stateMutability": "payable",
                    "type": "function"
                },
                {
                    "inputs": [
                    {
                        "components": [
                        {
                            "internalType": "address",
                            "name": "target",
                            "type": "address"
                        },
                        {
                            "internalType": "bool",
                            "name": "allowFailure",
                            "type": "bool"
                        },
                        {
                            "internalType": "bytes",
                            "name": "callData",
                            "type": "bytes"
                        }
                        ],
                        "internalType": "struct Multicall3.Call3[]",
                        "name": "calls",
                        "type": "tuple[]"
                    }
                    ],
                    "name": "aggregate3",
                    "outputs": [
                    {
                        "components": [
                        {
                            "internalType": "bool",
                            "name": "success",
                            "type": "bool"
                        },
                        {
                            "internalType": "bytes",
                            "name": "returnData",
                            "type": "bytes"
                        }
                        ],
                        "internalType": "struct Multicall3.Result[]",
                        "name": "returnData",
                        "type": "tuple[]"
                    }
                    ],
                    "stateMutability": "payable",
                    "type": "function"
                },
                {
                    "inputs": [
                    {
                        "components": [
                        {
                            "internalType": "address",
                            "name": "target",
                            "type": "address"
                        },
                        {
                            "internalType": "bool",
                            "name": "allowFailure",
                            "type": "bool"
                        },
                        {
                            "internalType": "uint256",
                            "name": "value",
                            "type": "uint256"
                        },
                        {
                            "internalType": "bytes",
                            "name": "callData",
                            "type": "bytes"
                        }
                        ],
                        "internalType": "struct Multicall3.Call3Value[]",
                        "name": "calls",
                        "type": "tuple[]"
                    }
                    ],
                    "name": "aggregate3Value",
                    "outputs": [
                    {
                        "components": [
                        {
                            "internalType": "bool",
                            "name": "success",
                            "type": "bool"
                        },
                        {
                            "internalType": "bytes",
                            "name": "returnData",
                            "type": "bytes"
                        }
                        ],
                        "internalType": "struct Multicall3.Result[]",
                        "name": "returnData",
                        "type": "tuple[]"
                    }
                    ],
                    "stateMutability": "payable",
                    "type": "function"
                },
                {
                    "inputs": [
                    {
                        "components": [
                        {
                            "internalType": "address",
                            "name": "target",
                            "type": "address"
                        },
                        {
                            "internalType": "bytes",
                            "name": "callData",
                            "type": "bytes"
                        }
                        ],
                        "internalType": "struct Multicall3.Call[]",
                        "name": "calls",
                        "type": "tuple[]"
                    }
                    ],
                    "name": "blockAndAggregate",
                    "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "blockNumber",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bytes32",
                        "name": "blockHash",
                        "type": "bytes32"
                    },
                    {
                        "components": [
                        {
                            "internalType": "bool",
                            "name": "success",
                            "type": "bool"
                        },
                        {
                            "internalType": "bytes",
                            "name": "returnData",
                            "type": "bytes"
                        }
                        ],
                        "internalType": "struct Multicall3.Result[]",
                        "name": "returnData",
                        "type": "tuple[]"
                    }
                    ],
                    "stateMutability": "payable",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "getBasefee",
                    "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "basefee",
                        "type": "uint256"
                    }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [
                    {
                        "internalType": "uint256",
                        "name": "blockNumber",
                        "type": "uint256"
                    }
                    ],
                    "name": "getBlockHash",
                    "outputs": [
                    {
                        "internalType": "bytes32",
                        "name": "blockHash",
                        "type": "bytes32"
                    }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "getBlockNumber",
                    "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "blockNumber",
                        "type": "uint256"
                    }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "getChainId",
                    "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "chainid",
                        "type": "uint256"
                    }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "getCurrentBlockCoinbase",
                    "outputs": [
                    {
                        "internalType": "address",
                        "name": "coinbase",
                        "type": "address"
                    }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "getCurrentBlockDifficulty",
                    "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "difficulty",
                        "type": "uint256"
                    }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "getCurrentBlockGasLimit",
                    "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "gaslimit",
                        "type": "uint256"
                    }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "getCurrentBlockTimestamp",
                    "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "timestamp",
                        "type": "uint256"
                    }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [
                    {
                        "internalType": "address",
                        "name": "addr",
                        "type": "address"
                    }
                    ],
                    "name": "getEthBalance",
                    "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "balance",
                        "type": "uint256"
                    }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "getLastBlockHash",
                    "outputs": [
                    {
                        "internalType": "bytes32",
                        "name": "blockHash",
                        "type": "bytes32"
                    }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [
                    {
                        "internalType": "bool",
                        "name": "requireSuccess",
                        "type": "bool"
                    },
                    {
                        "components": [
                        {
                            "internalType": "address",
                            "name": "target",
                            "type": "address"
                        },
                        {
                            "internalType": "bytes",
                            "name": "callData",
                            "type": "bytes"
                        }
                        ],
                        "internalType": "struct Multicall3.Call[]",
                        "name": "calls",
                        "type": "tuple[]"
                    }
                    ],
                    "name": "tryAggregate",
                    "outputs": [
                    {
                        "components": [
                        {
                            "internalType": "bool",
                            "name": "success",
                            "type": "bool"
                        },
                        {
                            "internalType": "bytes",
                            "name": "returnData",
                            "type": "bytes"
                        }
                        ],
                        "internalType": "struct Multicall3.Result[]",
                        "name": "returnData",
                        "type": "tuple[]"
                    }
                    ],
                    "stateMutability": "payable",
                    "type": "function"
                },
                {
                    "inputs": [
                    {
                        "internalType": "bool",
                        "name": "requireSuccess",
                        "type": "bool"
                    },
                    {
                        "components": [
                        {
                            "internalType": "address",
                            "name": "target",
                            "type": "address"
                        },
                        {
                            "internalType": "bytes",
                            "name": "callData",
                            "type": "bytes"
                        }
                        ],
                        "internalType": "struct Multicall3.Call[]",
                        "name": "calls",
                        "type": "tuple[]"
                    }
                    ],
                    "name": "tryBlockAndAggregate",
                    "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "blockNumber",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bytes32",
                        "name": "blockHash",
                        "type": "bytes32"
                    },
                    {
                        "components": [
                        {
                            "internalType": "bool",
                            "name": "success",
                            "type": "bool"
                        },
                        {
                            "internalType": "bytes",
                            "name": "returnData",
                            "type": "bytes"
                        }
                        ],
                        "internalType": "struct Multicall3.Result[]",
                        "name": "returnData",
                        "type": "tuple[]"
                    }
                    ],
                    "stateMutability": "payable",
                    "type": "function"
                }
                ]

ABI_ERC20 = [
    {'inputs': [{'internalType': 'string', 'name': '_name', 'type': 'string'}, {'internalType': 'string', 'name': '_symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': '_initialSupply', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}], 'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint8', 'name': 'decimals_', 'type': 'uint8'}], 'name': 'setupDecimals', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}]

ABI_WETH = [
    {'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': '_account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'BridgeBurn', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'l1Token', 'type': 'address'}, {'indexed': False, 'internalType': 'string', 'name': 'name', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'indexed': False, 'internalType': 'uint8', 'name': 'decimals', 'type': 'uint8'}], 'name': 'BridgeInitialize', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': '_account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'BridgeMint', 'type': 'event'}, {'anonymous': False, 'inputs': [], 'name': 'EIP712DomainChanged', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'name', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'indexed': False, 'internalType': 'uint8', 'name': 'decimals', 'type': 'uint8'}], 'name': 'Initialize', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint8', 'name': 'version', 'type': 'uint8'}], 'name': 'Initialized', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'inputs': [], 'name': 'DOMAIN_SEPARATOR', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_from', 'type': 'address'}, {'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'bridgeBurn', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'bridgeMint', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}], 'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'deposit', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_to', 'type': 'address'}], 'name': 'depositTo', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'eip712Domain', 'outputs': [{'internalType': 'bytes1', 'name': 'fields', 'type': 'bytes1'}, {'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'string', 'name': 'version', 'type': 'string'}, {'internalType': 'uint256', 'name': 'chainId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'verifyingContract', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'internalType': 'uint256[]', 'name': 'extensions', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'string', 'name': 'name_', 'type': 'string'}, {'internalType': 'string', 'name': 'symbol_', 'type': 'string'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'l1Address', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'l2Bridge', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'nonces', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'v', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'r', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}], 'name': 'permit', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'withdraw', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_to', 'type': 'address'}, {'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'withdrawTo', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'stateMutability': 'payable', 'type': 'receive'}]

ABI_UIPOOLDATA_PROVIDER = [
  {
    "inputs": [
      {
        "internalType": "contract IReserveOracleGetter",
        "name": "_reserveOracle",
        "type": "address"
      },
      {
        "internalType": "contract INFTOracleGetter",
        "name": "_nftOracle",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [
      {
        "internalType": "contract ILendPoolAddressesProvider",
        "name": "provider",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "user",
        "type": "address"
      }
    ],
    "name": "getNftsData",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "underlyingAsset",
            "type": "address"
          },
          {
            "internalType": "string",
            "name": "name",
            "type": "string"
          },
          {
            "internalType": "string",
            "name": "symbol",
            "type": "string"
          },
          {
            "internalType": "uint256",
            "name": "ltv",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "liquidationThreshold",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "liquidationBonus",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "redeemDuration",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "auctionDuration",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "redeemFine",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "redeemThreshold",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "minBidFine",
            "type": "uint256"
          },
          {
            "internalType": "bool",
            "name": "isActive",
            "type": "bool"
          },
          {
            "internalType": "bool",
            "name": "isFrozen",
            "type": "bool"
          },
          {
            "internalType": "address",
            "name": "bNftAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "priceInEth",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "totalCollateral",
            "type": "uint256"
          }
        ],
        "internalType": "struct IUiPoolDataProvider.AggregatedNftData[]",
        "name": "",
        "type": "tuple[]"
      },
      {
        "components": [
          {
            "internalType": "address",
            "name": "underlyingAsset",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "bNftAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "totalCollateral",
            "type": "uint256"
          }
        ],
        "internalType": "struct IUiPoolDataProvider.UserNftData[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ILendPoolAddressesProvider",
        "name": "provider",
        "type": "address"
      }
    ],
    "name": "getNftsList",
    "outputs": [
      {
        "internalType": "address[]",
        "name": "",
        "type": "address[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ILendPoolAddressesProvider",
        "name": "provider",
        "type": "address"
      },
      #{
      #  "internalType": "address",
      #  "name": "user",
      #  "type": "address"
      #}
    ],
    "name": "getReservesData",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "underlyingAsset",
            "type": "address"
          },
          {
            "internalType": "string",
            "name": "name",
            "type": "string"
          },
          {
            "internalType": "string",
            "name": "symbol",
            "type": "string"
          },
          {
            "internalType": "uint256",
            "name": "decimals",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "reserveFactor",
            "type": "uint256"
          },
          {
            "internalType": "bool",
            "name": "borrowingEnabled",
            "type": "bool"
          },
          {
            "internalType": "bool",
            "name": "isActive",
            "type": "bool"
          },
          {
            "internalType": "bool",
            "name": "isFrozen",
            "type": "bool"
          },
          {
            "internalType": "uint128",
            "name": "liquidityIndex",
            "type": "uint128"
          },
          {
            "internalType": "uint128",
            "name": "variableBorrowIndex",
            "type": "uint128"
          },
          {
            "internalType": "uint128",
            "name": "liquidityRate",
            "type": "uint128"
          },
          {
            "internalType": "uint128",
            "name": "variableBorrowRate",
            "type": "uint128"
          },
          {
            "internalType": "uint40",
            "name": "lastUpdateTimestamp",
            "type": "uint40"
          },
          {
            "internalType": "address",
            "name": "bTokenAddress",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "debtTokenAddress",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "interestRateAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "availableLiquidity",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "totalVariableDebt",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "priceInEth",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "variableRateSlope1",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "variableRateSlope2",
            "type": "uint256"
          }
        ],
        "internalType": "struct IUiPoolDataProvider.AggregatedReserveData[]",
        "name": "",
        "type": "tuple[]"
      },
      {
        "components": [
          {
            "internalType": "address",
            "name": "underlyingAsset",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "bTokenBalance",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "variableDebt",
            "type": "uint256"
          }
        ],
        "internalType": "struct IUiPoolDataProvider.UserReserveData[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ILendPoolAddressesProvider",
        "name": "provider",
        "type": "address"
      }
    ],
    "name": "getReservesList",
    "outputs": [
      {
        "internalType": "address[]",
        "name": "",
        "type": "address[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ILendPoolAddressesProvider",
        "name": "provider",
        "type": "address"
      },
      {
        "internalType": "address[]",
        "name": "nftAssets",
        "type": "address[]"
      },
      {
        "internalType": "uint256[]",
        "name": "nftTokenIds",
        "type": "uint256[]"
      }
    ],
    "name": "getSimpleLoansData",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "loanId",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "state",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "reserveAsset",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "totalCollateralInReserve",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "totalDebtInReserve",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "availableBorrowsInReserve",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "healthFactor",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "liquidatePrice",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "bidderAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "bidPrice",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "bidBorrowAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "bidFine",
            "type": "uint256"
          }
        ],
        "internalType": "struct IUiPoolDataProvider.AggregatedLoanData[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ILendPoolAddressesProvider",
        "name": "provider",
        "type": "address"
      }
    ],
    "name": "getSimpleNftsData",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "underlyingAsset",
            "type": "address"
          },
          {
            "internalType": "string",
            "name": "name",
            "type": "string"
          },
          {
            "internalType": "string",
            "name": "symbol",
            "type": "string"
          },
          {
            "internalType": "uint256",
            "name": "ltv",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "liquidationThreshold",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "liquidationBonus",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "redeemDuration",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "auctionDuration",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "redeemFine",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "redeemThreshold",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "minBidFine",
            "type": "uint256"
          },
          {
            "internalType": "bool",
            "name": "isActive",
            "type": "bool"
          },
          {
            "internalType": "bool",
            "name": "isFrozen",
            "type": "bool"
          },
          {
            "internalType": "address",
            "name": "bNftAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "priceInEth",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "totalCollateral",
            "type": "uint256"
          }
        ],
        "internalType": "struct IUiPoolDataProvider.AggregatedNftData[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ILendPoolAddressesProvider",
        "name": "provider",
        "type": "address"
      }
    ],
    "name": "getSimpleReservesData",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "underlyingAsset",
            "type": "address"
          },
          {
            "internalType": "string",
            "name": "name",
            "type": "string"
          },
          {
            "internalType": "string",
            "name": "symbol",
            "type": "string"
          },
          {
            "internalType": "uint256",
            "name": "decimals",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "reserveFactor",
            "type": "uint256"
          },
          {
            "internalType": "bool",
            "name": "borrowingEnabled",
            "type": "bool"
          },
          {
            "internalType": "bool",
            "name": "isActive",
            "type": "bool"
          },
          {
            "internalType": "bool",
            "name": "isFrozen",
            "type": "bool"
          },
          {
            "internalType": "uint128",
            "name": "liquidityIndex",
            "type": "uint128"
          },
          {
            "internalType": "uint128",
            "name": "variableBorrowIndex",
            "type": "uint128"
          },
          {
            "internalType": "uint128",
            "name": "liquidityRate",
            "type": "uint128"
          },
          {
            "internalType": "uint128",
            "name": "variableBorrowRate",
            "type": "uint128"
          },
          {
            "internalType": "uint40",
            "name": "lastUpdateTimestamp",
            "type": "uint40"
          },
          {
            "internalType": "address",
            "name": "bTokenAddress",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "debtTokenAddress",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "interestRateAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "availableLiquidity",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "totalVariableDebt",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "priceInEth",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "variableRateSlope1",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "variableRateSlope2",
            "type": "uint256"
          }
        ],
        "internalType": "struct IUiPoolDataProvider.AggregatedReserveData[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ILendPoolAddressesProvider",
        "name": "provider",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "user",
        "type": "address"
      }
    ],
    "name": "getUserNftsData",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "underlyingAsset",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "bNftAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "totalCollateral",
            "type": "uint256"
          }
        ],
        "internalType": "struct IUiPoolDataProvider.UserNftData[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ILendPoolAddressesProvider",
        "name": "provider",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "user",
        "type": "address"
      }
    ],
    "name": "getUserReservesData",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "underlyingAsset",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "bTokenBalance",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "variableDebt",
            "type": "uint256"
          }
        ],
        "internalType": "struct IUiPoolDataProvider.UserReserveData[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "nftOracle",
    "outputs": [
      {
        "internalType": "contract INFTOracleGetter",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "reserveOracle",
    "outputs": [
      {
        "internalType": "contract IReserveOracleGetter",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]

ABI_PoolAddressProvider = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "marketId",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "ACLAdminUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "ACLManagerUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "AddressSet",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "proxyAddress",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "oldImplementationAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newImplementationAddress",
                "type": "address"
            }
        ],
        "name": "AddressSetAsProxy",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "string",
                "name": "oldMarketId",
                "type": "string"
            },
            {
                "indexed": True,
                "internalType": "string",
                "name": "newMarketId",
                "type": "string"
            }
        ],
        "name": "MarketIdSet",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "PoolConfiguratorUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "PoolDataProviderUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "PoolUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "PriceOracleSentinelUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "oldAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "PriceOracleUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "proxyAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "implementationAddress",
                "type": "address"
            }
        ],
        "name": "ProxyCreated",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "getACLAdmin",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getACLManager",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            }
        ],
        "name": "getAddress",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getMarketId",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getPool",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getPoolConfigurator",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getPoolDataProvider",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getPriceOracle",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getPriceOracleSentinel",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newAclAdmin",
                "type": "address"
            }
        ],
        "name": "setACLAdmin",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newAclManager",
                "type": "address"
            }
        ],
        "name": "setACLManager",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            }
        ],
        "name": "setAddress",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "newImplementationAddress",
                "type": "address"
            }
        ],
        "name": "setAddressAsProxy",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "newMarketId",
                "type": "string"
            }
        ],
        "name": "setMarketId",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newPoolConfiguratorImpl",
                "type": "address"
            }
        ],
        "name": "setPoolConfiguratorImpl",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newDataProvider",
                "type": "address"
            }
        ],
        "name": "setPoolDataProvider",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newPoolImpl",
                "type": "address"
            }
        ],
        "name": "setPoolImpl",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newPriceOracle",
                "type": "address"
            }
        ],
        "name": "setPriceOracle",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newPriceOracleSentinel",
                "type": "address"
            }
        ],
        "name": "setPriceOracleSentinel",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]


#endregion

#//COMPLETE BERACHAIN ABI
#region berachain demo

ABI_DEFAULT =  [
                {
                    "constant": True,
                    "inputs": [],
                    "name": "name",
                    "outputs": [{"name": "", "type": "string"}],
                    "payable": False,
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "constant": True,
                    "inputs": [],
                    "name": "symbol",
                    "outputs": [{"name": "", "type": "string"}],
                    "payable": False,
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "constant": True,
                    "inputs": [],
                    "name": "decimals",
                    "outputs": [{"name": "", "type": "uint8"}],
                    "payable": False,
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "constant": True,
                    "inputs": [],
                    "name": "totalSupply",
                    "outputs": [{"name": "", "type": "uint256"}],
                    "payable": False,
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "constant": True,
                    "inputs": [{"name": "_owner", "type": "address"}],
                    "name": "balanceOf",
                    "outputs": [{"name": "balance", "type": "uint256"}],
                    "payable": False,
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "constant": False,
                    "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
                    "name": "transfer",
                    "outputs": [{"name": "", "type": "bool"}],
                    "payable": False,
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "constant": False,
                    "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}],
                    "name": "approve",
                    "outputs": [{"name": "", "type": "bool"}],
                    "payable": False,
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "constant": True,
                    "inputs": [{"name": "_owner", "type": "address"}, {"name": "_spender", "type": "address"}],
                    "name": "allowance",
                    "outputs": [{"name": "remaining", "type": "uint256"}],
                    "payable": False,
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "constant": True,
                    "inputs": [
                        {"name": "_owner", "type": "address"},
                        {"name": "_index", "type": "uint256"}
                    ],
                    "name": "tokenOfOwnerByIndex",
                    "outputs": [{"name": "", "type": "uint256"}],
                    "payable": False,
                    "stateMutability": "view",
                    "type": "function",
                },
                {
                "constant": False,
                "inputs": [
                    {
                    "name": "_to",
                    "type": "address"
                    },
                    {
                    "name": "_amount",
                    "type": "uint256"
                    },
                    {
                    "name": "_tokenAddress",
                    "type": "address"
                    }
                ],
                "name": "redeem",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
                }
            ]

ABI_BERA_ERC20_DEX =    [
                        {
                            "type": "function",
                            "name": "addLiquidity",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "receiver",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "assetsIn",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amountsIn",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "shares",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "shareAmounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            },
                            {
                                "name": "liquidity",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "liquidityAmounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "payable"
                        },
                        {
                            "type": "function",
                            "name": "batchSwap",
                            "inputs": [
                            {
                                "name": "kind",
                                "type": "uint8",
                                "internalType": "enum IERC20DexModule.SwapKind"
                            },
                            {
                                "name": "swaps",
                                "type": "tuple[]",
                                "internalType": "struct IERC20DexModule.BatchSwapStep[]",
                                "components": [
                                {
                                    "name": "poolId",
                                    "type": "address",
                                    "internalType": "address"
                                },
                                {
                                    "name": "assetIn",
                                    "type": "address",
                                    "internalType": "address"
                                },
                                {
                                    "name": "amountIn",
                                    "type": "uint256",
                                    "internalType": "uint256"
                                },
                                {
                                    "name": "assetOut",
                                    "type": "address",
                                    "internalType": "address"
                                },
                                {
                                    "name": "amountOut",
                                    "type": "uint256",
                                    "internalType": "uint256"
                                },
                                {
                                    "name": "userData",
                                    "type": "bytes",
                                    "internalType": "bytes"
                                }
                                ]
                            },
                            {
                                "name": "deadline",
                                "type": "uint256",
                                "internalType": "uint256"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "assets",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "payable"
                        },
                        {
                            "type": "function",
                            "name": "createPool",
                            "inputs": [
                            {
                                "name": "name",
                                "type": "string",
                                "internalType": "string"
                            },
                            {
                                "name": "assetsIn",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amountsIn",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            },
                            {
                                "name": "poolType",
                                "type": "string",
                                "internalType": "string"
                            },
                            {
                                "name": "options",
                                "type": "tuple",
                                "internalType": "struct IERC20DexModule.PoolOptions",
                                "components": [
                                {
                                    "name": "weights",
                                    "type": "tuple[]",
                                    "internalType": "struct IERC20DexModule.AssetWeight[]",
                                    "components": [
                                    {
                                        "name": "asset",
                                        "type": "address",
                                        "internalType": "address"
                                    },
                                    {
                                        "name": "weight",
                                        "type": "uint256",
                                        "internalType": "uint256"
                                    }
                                    ]
                                },
                                {
                                    "name": "swapFee",
                                    "type": "uint256",
                                    "internalType": "uint256"
                                }
                                ]
                            }
                            ],
                            "outputs": [
                            {
                                "name": "",
                                "type": "address",
                                "internalType": "address"
                            }
                            ],
                            "stateMutability": "payable"
                        },
                        {
                            "type": "function",
                            "name": "getExchangeRate",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "baseAsset",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "quoteAsset",
                                "type": "address",
                                "internalType": "address"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "",
                                "type": "uint256",
                                "internalType": "uint256"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getLiquidity",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "asset",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getPoolName",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "",
                                "type": "string",
                                "internalType": "string"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getPoolOptions",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "",
                                "type": "tuple",
                                "internalType": "struct IERC20DexModule.PoolOptions",
                                "components": [
                                {
                                    "name": "weights",
                                    "type": "tuple[]",
                                    "internalType": "struct IERC20DexModule.AssetWeight[]",
                                    "components": [
                                    {
                                        "name": "asset",
                                        "type": "address",
                                        "internalType": "address"
                                    },
                                    {
                                        "name": "weight",
                                        "type": "uint256",
                                        "internalType": "uint256"
                                    }
                                    ]
                                },
                                {
                                    "name": "swapFee",
                                    "type": "uint256",
                                    "internalType": "uint256"
                                }
                                ]
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getPreviewAddLiquidityNoSwap",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "assets",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "shares",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "shareAmounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            },
                            {
                                "name": "liqOut",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "liquidityAmounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getPreviewAddLiquidityStaticPrice",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "liquidity",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "shares",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "shareAmounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            },
                            {
                                "name": "liqOut",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "liquidityAmounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getPreviewBatchSwap",
                            "inputs": [
                            {
                                "name": "kind",
                                "type": "uint8",
                                "internalType": "enum IERC20DexModule.SwapKind"
                            },
                            {
                                "name": "swaps",
                                "type": "tuple[]",
                                "internalType": "struct IERC20DexModule.BatchSwapStep[]",
                                "components": [
                                {
                                    "name": "poolId",
                                    "type": "address",
                                    "internalType": "address"
                                },
                                {
                                    "name": "assetIn",
                                    "type": "address",
                                    "internalType": "address"
                                },
                                {
                                    "name": "amountIn",
                                    "type": "uint256",
                                    "internalType": "uint256"
                                },
                                {
                                    "name": "assetOut",
                                    "type": "address",
                                    "internalType": "address"
                                },
                                {
                                    "name": "amountOut",
                                    "type": "uint256",
                                    "internalType": "uint256"
                                },
                                {
                                    "name": "userData",
                                    "type": "bytes",
                                    "internalType": "bytes"
                                }
                                ]
                            }
                            ],
                            "outputs": [
                            {
                                "name": "asset",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "amount",
                                "type": "uint256",
                                "internalType": "uint256"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getPreviewBurnShares",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "asset",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "amount",
                                "type": "uint256",
                                "internalType": "uint256"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "assets",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getPreviewSharesForLiquidity",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "assets",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "shares",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "shareAmounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            },
                            {
                                "name": "liquidity",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "liquidityAmounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getPreviewSharesForSingleSidedLiquidityRequest",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "asset",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "amount",
                                "type": "uint256",
                                "internalType": "uint256"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "assets",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getPreviewSwapExact",
                            "inputs": [
                            {
                                "name": "kind",
                                "type": "uint8",
                                "internalType": "enum IERC20DexModule.SwapKind"
                            },
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "baseAsset",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "baseAssetAmount",
                                "type": "uint256",
                                "internalType": "uint256"
                            },
                            {
                                "name": "quoteAsset",
                                "type": "address",
                                "internalType": "address"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "asset",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "amount",
                                "type": "uint256",
                                "internalType": "uint256"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getRemoveLiquidityExactAmountOut",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "assetIn",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "assetAmount",
                                "type": "uint256",
                                "internalType": "uint256"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "assets",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getRemoveLiquidityOneSideOut",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "assetOut",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "sharesIn",
                                "type": "uint256",
                                "internalType": "uint256"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "assets",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "getTotalShares",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "assets",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "view"
                        },
                        {
                            "type": "function",
                            "name": "removeLiquidityBurningShares",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "withdrawAddress",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "assetIn",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "amountIn",
                                "type": "uint256",
                                "internalType": "uint256"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "liquidity",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "liquidityAmounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "payable"
                        },
                        {
                            "type": "function",
                            "name": "removeLiquidityExactAmount",
                            "inputs": [
                            {
                                "name": "pool",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "withdrawAddress",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "assetOut",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "amountOut",
                                "type": "uint256",
                                "internalType": "uint256"
                            },
                            {
                                "name": "sharesIn",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "maxSharesIn",
                                "type": "uint256",
                                "internalType": "uint256"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "shares",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "shareAmounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            },
                            {
                                "name": "liquidity",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "liquidityAmounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "payable"
                        },
                        {
                            "type": "function",
                            "name": "swap",
                            "inputs": [
                            {
                                "name": "kind",
                                "type": "uint8",
                                "internalType": "enum IERC20DexModule.SwapKind"
                            },
                            {
                                "name": "poolId",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "assetIn",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "amountIn",
                                "type": "uint256",
                                "internalType": "uint256"
                            },
                            {
                                "name": "assetOut",
                                "type": "address",
                                "internalType": "address"
                            },
                            {
                                "name": "amountOut",
                                "type": "uint256",
                                "internalType": "uint256"
                            },
                            {
                                "name": "deadline",
                                "type": "uint256",
                                "internalType": "uint256"
                            }
                            ],
                            "outputs": [
                            {
                                "name": "assets",
                                "type": "address[]",
                                "internalType": "address[]"
                            },
                            {
                                "name": "amounts",
                                "type": "uint256[]",
                                "internalType": "uint256[]"
                            }
                            ],
                            "stateMutability": "payable"
                        }
                        ]

ABI_BEX = [
  {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'address[]', 'name': 'assetsIn', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amountsIn', 'type': 'uint256[]'}], 'name': 'addLiquidity', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'},                                                                                                                                                                                                                                                                                                                                                      {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'enum IERC20DexModule.SwapKind', 'name': 'kind', 'type': 'uint8'}, {'components': [{'internalType': 'address', 'name': 'poolId', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'userData', 'type': 'bytes'}], 'internalType': 'struct IERC20DexModule.BatchSwapStep[]', 'name': 'swaps', 'type': 'tuple[]'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}], 'name': 'batchSwap', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'address[]', 'name': 'assetsIn', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amountsIn', 'type': 'uint256[]'}, {'internalType': 'string', 'name': 'poolType', 'type': 'string'}, {'components': [{'components': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}], 'internalType': 'struct IERC20DexModule.AssetWeight[]', 'name': 'weights', 'type': 'tuple[]'}, {'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}], 'internalType': 'struct IERC20DexModule.PoolOptions', 'name': 'options', 'type': 'tuple'}], 'name': 'createPool', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'baseAsset', 'type': 'address'}, {'internalType': 'address', 'name': 'quoteAsset', 'type': 'address'}], 'name': 'getExchangeRate', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}], 'name': 'getLiquidity', 'outputs': [{'internalType': 'address[]', 'name': 'asset', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}], 'name': 'getPoolName', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}], 'name': 'getPoolOptions', 'outputs': [{'components': [{'components': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'weight', 'type': 'uint256'}], 'internalType': 'struct IERC20DexModule.AssetWeight[]', 'name': 'weights', 'type': 'tuple[]'}, {'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}], 'internalType': 'struct IERC20DexModule.PoolOptions', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'name': 'getPreviewAddLiquidityNoSwap', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liqOut', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'name': 'getPreviewAddLiquidityStaticPrice', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liqOut', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'enum IERC20DexModule.SwapKind', 'name': 'kind', 'type': 'uint8'}, {'components': [{'internalType': 'address', 'name': 'poolId', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'userData', 'type': 'bytes'}], 'internalType': 'struct IERC20DexModule.BatchSwapStep[]', 'name': 'swaps', 'type': 'tuple[]'}], 'name': 'getPreviewBatchSwap', 'outputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'getPreviewBurnShares', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'name': 'getPreviewSharesForLiquidity', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'getPreviewSharesForSingleSidedLiquidityRequest', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'enum IERC20DexModule.SwapKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'baseAsset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'baseAssetAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'quoteAsset', 'type': 'address'}], 'name': 'getPreviewSwapExact', 'outputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'assetAmount', 'type': 'uint256'}], 'name': 'getRemoveLiquidityExactAmountOut', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'sharesIn', 'type': 'uint256'}], 'name': 'getRemoveLiquidityOneSideOut', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}], 'name': 'getTotalShares', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'withdrawAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}], 'name': 'removeLiquidityBurningShares', 'outputs': [{'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'address', 'name': 'withdrawAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'address', 'name': 'sharesIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'maxSharesIn', 'type': 'uint256'}], 'name': 'removeLiquidityExactAmount', 'outputs': [{'internalType': 'address[]', 'name': 'shares', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'shareAmounts', 'type': 'uint256[]'}, {'internalType': 'address[]', 'name': 'liquidity', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'liquidityAmounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'enum IERC20DexModule.SwapKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'address', 'name': 'poolId', 'type': 'address'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}], 'name': 'swap', 'outputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}], 'stateMutability': 'payable', 'type': 'function'}]

ABI_HONEY = [
    {'inputs': [{'internalType': 'contract IERC20', 'name': '_honey', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'inputs': [], 'name': 'erc20Module', 'outputs': [{'internalType': 'contract IERC20Module', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'string', 'name': 'amoType', 'type': 'string'}, {'internalType': 'address', 'name': 'amoAddr', 'type': 'address'}], 'name': 'getAMOCurrentLimit', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getExchangable', 'outputs': [{'components': [{'internalType': 'contract IERC20', 'name': 'collateral', 'type': 'address'}, {'internalType': 'bool', 'name': 'enabled', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'mintRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'redemptionRate', 'type': 'uint256'}], 'internalType': 'struct ERC20Honey.ERC20Exchangable[]', 'name': '', 'type': 'tuple[]'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'getTotalCollateral', 'outputs': [{'internalType': 'address[]', 'name': '', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'honey', 'outputs': [{'internalType': 'contract IERC20', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'honeyModule', 'outputs': [{'internalType': 'contract IHoneyModule', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'contract IERC20', 'name': 'collateral', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'mint', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'amountOut', 'type': 'uint256'}, {'internalType': 'address', 'name': 'assetOut', 'type': 'address'}], 'name': 'previewExactOutCollateral', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20', 'name': 'collateral', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'previewMint', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20', 'name': 'collateral', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'previewRedeem', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'honeyOut', 'type': 'uint256'}, {'internalType': 'address', 'name': 'assetIn', 'type': 'address'}], 'name': 'previewRequiredCollateral', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'contract IERC20', 'name': 'collateral', 'type': 'address'}], 'name': 'redeem', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}]

ABI_BEND = [
            {'inputs': [{'internalType': 'contract IPoolAddressesProvider', 'name': 'provider', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'inputs': [{'internalType': 'address', 'name': 'reserve', 'type': 'address'}, {'internalType': 'address', 'name': 'backer', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'fee', 'type': 'uint256'}], 'name': 'BackUnbacked', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'reserve', 'type': 'address'}, {'internalType': 'address', 'name': 'user', 'type': 'address'}, {'internalType': 'address', 'name': 'onBehalfOf', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'enum DataTypes.InterestRateMode', 'name': 'interestRateMode', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'borrowRate', 'type': 'uint256'}, {'internalType': 'uint16', 'name': 'referralCode', 'type': 'uint16'}], 'name': 'Borrow', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'address', 'name': 'initiator', 'type': 'address'}, {'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'enum DataTypes.InterestRateMode', 'name': 'interestRateMode', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'premium', 'type': 'uint256'}, {'internalType': 'uint16', 'name': 'referralCode', 'type': 'uint16'}], 'name': 'FlashLoan', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'totalDebt', 'type': 'uint256'}], 'name': 'IsolationModeTotalDebtUpdated', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'collateralAsset', 'type': 'address'}, {'internalType': 'address', 'name': 'debtAsset', 'type': 'address'}, {'internalType': 'address', 'name': 'user', 'type': 'address'}, {'internalType': 'uint256', 'name': 'debtToCover', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'liquidatedCollateralAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'liquidator', 'type': 'address'}, {'internalType': 'bool', 'name': 'receiveAToken', 'type': 'bool'}], 'name': 'LiquidationCall', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'reserve', 'type': 'address'}, {'internalType': 'address', 'name': 'user', 'type': 'address'}, {'internalType': 'address', 'name': 'onBehalfOf', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint16', 'name': 'referralCode', 'type': 'uint16'}], 'name': 'MintUnbacked', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'reserve', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amountMinted', 'type': 'uint256'}], 'name': 'MintedToTreasury', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'reserve', 'type': 'address'}, {'internalType': 'address', 'name': 'user', 'type': 'address'}], 'name': 'RebalanceStableBorrowRate', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'reserve', 'type': 'address'}, {'internalType': 'address', 'name': 'user', 'type': 'address'}, {'internalType': 'address', 'name': 'repayer', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'useATokens', 'type': 'bool'}], 'name': 'Repay', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'reserve', 'type': 'address'}, {'internalType': 'uint256', 'name': 'liquidityRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'stableBorrowRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'variableBorrowRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'liquidityIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'variableBorrowIndex', 'type': 'uint256'}], 'name': 'ReserveDataUpdated', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'reserve', 'type': 'address'}, {'internalType': 'address', 'name': 'user', 'type': 'address'}], 'name': 'ReserveUsedAsCollateralDisabled', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'reserve', 'type': 'address'}, {'internalType': 'address', 'name': 'user', 'type': 'address'}], 'name': 'ReserveUsedAsCollateralEnabled', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'reserve', 'type': 'address'}, {'internalType': 'address', 'name': 'user', 'type': 'address'}, {'internalType': 'address', 'name': 'onBehalfOf', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint16', 'name': 'referralCode', 'type': 'uint16'}], 'name': 'Supply', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'reserve', 'type': 'address'}, {'internalType': 'address', 'name': 'user', 'type': 'address'}, {'internalType': 'enum DataTypes.InterestRateMode', 'name': 'interestRateMode', 'type': 'uint8'}], 'name': 'SwapBorrowRateMode', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'user', 'type': 'address'}, {'internalType': 'uint8', 'name': 'categoryId', 'type': 'uint8'}], 'name': 'UserEModeSet', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'reserve', 'type': 'address'}, {'internalType': 'address', 'name': 'user', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Withdraw', 'type': 'event'}, {'inputs': [], 'name': 'ADDRESSES_PROVIDER', 'outputs': [{'internalType': 'contract IPoolAddressesProvider', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'BRIDGE_PROTOCOL_FEE', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'FLASHLOAN_PREMIUM_TOTAL', 'outputs': [{'internalType': 'uint128', 'name': '', 'type': 'uint128'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'FLASHLOAN_PREMIUM_TO_PROTOCOL', 'outputs': [{'internalType': 'uint128', 'name': '', 'type': 'uint128'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'MAX_NUMBER_RESERVES', 'outputs': [{'internalType': 'uint16', 'name': '', 'type': 'uint16'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'MAX_STABLE_RATE_BORROW_SIZE_PERCENT', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'POOL_REVISION', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'fee', 'type': 'uint256'}], 'name': 'backUnbacked', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestRateMode', 'type': 'uint256'}, {'internalType': 'uint16', 'name': 'referralCode', 'type': 'uint16'}, {'internalType': 'address', 'name': 'onBehalfOf', 'type': 'address'}], 'name': 'borrow', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint8', 'name': 'id', 'type': 'uint8'}, {'components': [{'internalType': 'uint16', 'name': 'ltv', 'type': 'uint16'}, {'internalType': 'uint16', 'name': 'liquidationThreshold', 'type': 'uint16'}, {'internalType': 'uint16', 'name': 'liquidationBonus', 'type': 'uint16'}, {'internalType': 'address', 'name': 'priceSource', 'type': 'address'}, {'internalType': 'string', 'name': 'label', 'type': 'string'}], 'internalType': 'struct DataTypes.EModeCategory', 'name': 'category', 'type': 'tuple'}], 'name': 'configureEModeCategory', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'onBehalfOf', 'type': 'address'}, {'internalType': 'uint16', 'name': 'referralCode', 'type': 'uint16'}], 'name': 'deposit', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}], 'name': 'dropReserve', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'balanceFromBefore', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'balanceToBefore', 'type': 'uint256'}], 'name': 'finalizeTransfer', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'receiverAddress', 'type': 'address'}, {'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}, {'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}, {'internalType': 'uint256[]', 'name': 'interestRateModes', 'type': 'uint256[]'}, {'internalType': 'address', 'name': 'onBehalfOf', 'type': 'address'}, {'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}, {'internalType': 'uint16', 'name': 'referralCode', 'type': 'uint16'}], 'name': 'flashLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'receiverAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}, {'internalType': 'uint16', 'name': 'referralCode', 'type': 'uint16'}], 'name': 'flashLoanSimple', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}], 'name': 'getConfiguration', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'data', 'type': 'uint256'}], 'internalType': 'struct DataTypes.ReserveConfigurationMap', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint8', 'name': 'id', 'type': 'uint8'}], 'name': 'getEModeCategoryData', 'outputs': [{'components': [{'internalType': 'uint16', 'name': 'ltv', 'type': 'uint16'}, {'internalType': 'uint16', 'name': 'liquidationThreshold', 'type': 'uint16'}, {'internalType': 'uint16', 'name': 'liquidationBonus', 'type': 'uint16'}, {'internalType': 'address', 'name': 'priceSource', 'type': 'address'}, {'internalType': 'string', 'name': 'label', 'type': 'string'}], 'internalType': 'struct DataTypes.EModeCategory', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint16', 'name': 'id', 'type': 'uint16'}], 'name': 'getReserveAddressById', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}], 'name': 'getReserveData', 'outputs': [{'components': [{'components': [{'internalType': 'uint256', 'name': 'data', 'type': 'uint256'}], 'internalType': 'struct DataTypes.ReserveConfigurationMap', 'name': 'configuration', 'type': 'tuple'}, {'internalType': 'uint128', 'name': 'liquidityIndex', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'currentLiquidityRate', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'variableBorrowIndex', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'currentVariableBorrowRate', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'currentStableBorrowRate', 'type': 'uint128'}, {'internalType': 'uint40', 'name': 'lastUpdateTimestamp', 'type': 'uint40'}, {'internalType': 'uint16', 'name': 'id', 'type': 'uint16'}, {'internalType': 'address', 'name': 'aTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'stableDebtTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'variableDebtTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'interestRateStrategyAddress', 'type': 'address'}, {'internalType': 'uint128', 'name': 'accruedToTreasury', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'unbacked', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'isolationModeTotalDebt', 'type': 'uint128'}], 'internalType': 'struct DataTypes.ReserveData', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}], 'name': 'getReserveNormalizedIncome', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}], 'name': 'getReserveNormalizedVariableDebt', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getReservesList', 'outputs': [{'internalType': 'address[]', 'name': '', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'user', 'type': 'address'}], 'name': 'getUserAccountData', 'outputs': [{'internalType': 'uint256', 'name': 'totalCollateralBase', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'totalDebtBase', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'availableBorrowsBase', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'currentLiquidationThreshold', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ltv', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'healthFactor', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'user', 'type': 'address'}], 'name': 'getUserConfiguration', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'data', 'type': 'uint256'}], 'internalType': 'struct DataTypes.UserConfigurationMap', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'user', 'type': 'address'}], 'name': 'getUserEMode', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'address', 'name': 'aTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'stableDebtAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'variableDebtAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'interestRateStrategyAddress', 'type': 'address'}], 'name': 'initReserve', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'contract IPoolAddressesProvider', 'name': 'provider', 'type': 'address'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'collateralAsset', 'type': 'address'}, {'internalType': 'address', 'name': 'debtAsset', 'type': 'address'}, {'internalType': 'address', 'name': 'user', 'type': 'address'}, {'internalType': 'uint256', 'name': 'debtToCover', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'receiveAToken', 'type': 'bool'}], 'name': 'liquidationCall', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address[]', 'name': 'assets', 'type': 'address[]'}], 'name': 'mintToTreasury', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'onBehalfOf', 'type': 'address'}, {'internalType': 'uint16', 'name': 'referralCode', 'type': 'uint16'}], 'name': 'mintUnbacked', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'address', 'name': 'user', 'type': 'address'}], 'name': 'rebalanceStableBorrowRate', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestRateMode', 'type': 'uint256'}, {'internalType': 'address', 'name': 'onBehalfOf', 'type': 'address'}], 'name': 'repay', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestRateMode', 'type': 'uint256'}], 'name': 'repayWithATokens', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestRateMode', 'type': 'uint256'}, {'internalType': 'address', 'name': 'onBehalfOf', 'type': 'address'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'permitV', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'permitR', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'permitS', 'type': 'bytes32'}], 'name': 'repayWithPermit', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'token', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'rescueTokens', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}], 'name': 'resetIsolationModeTotalDebt', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'components': [{'internalType': 'uint256', 'name': 'data', 'type': 'uint256'}], 'internalType': 'struct DataTypes.ReserveConfigurationMap', 'name': 'configuration', 'type': 'tuple'}], 'name': 'setConfiguration', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'address', 'name': 'rateStrategyAddress', 'type': 'address'}], 'name': 'setReserveInterestRateStrategyAddress', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint8', 'name': 'categoryId', 'type': 'uint8'}], 'name': 'setUserEMode', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'bool', 'name': 'useAsCollateral', 'type': 'bool'}], 'name': 'setUserUseReserveAsCollateral', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'onBehalfOf', 'type': 'address'}, {'internalType': 'uint16', 'name': 'referralCode', 'type': 'uint16'}], 'name': 'supply', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'onBehalfOf', 'type': 'address'}, {'internalType': 'uint16', 'name': 'referralCode', 'type': 'uint16'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'permitV', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'permitR', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'permitS', 'type': 'bytes32'}], 'name': 'supplyWithPermit', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'interestRateMode', 'type': 'uint256'}], 'name': 'swapBorrowRateMode', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'protocolFee', 'type': 'uint256'}], 'name': 'updateBridgeProtocolFee', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint128', 'name': 'flashLoanPremiumTotal', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'flashLoanPremiumToProtocol', 'type': 'uint128'}], 'name': 'updateFlashloanPremiums', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'asset', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'withdraw', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}
            ]

ABI_DOMAIN =[
            {
                "inputs": [
                    {"internalType": "address", "name": "token", "type": "address"},
                    {"internalType": "address[]", "name": "owners", "type": "address[]"},
                    {"internalType": "string[]", "name": "domainNames", "type": "string[]"},
                    {"internalType": "uint256[]", "name": "expiries", "type": "uint256[]"},
                    {"internalType": "address", "name": "referral", "type": "address"}
                ],
                "name": "registerDomains",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                    "constant": True,
                    "inputs": [{"name": "_owner", "type": "address"}],
                    "name": "balanceOf",
                    "outputs": [{"name": "balance", "type": "uint256"}],
                    "payable": False,
                    "stateMutability": "view",
                    "type": "function"
                },
            ]

ABI_DEVUSDC =   [
                {
                    "inputs": [],
                    "stateMutability": "nonpayable",
                    "type": "constructor"
                },
                {
                    "anonymous": False,
                    "inputs": [
                        {
                            "indexed": True,
                            "internalType": "address",
                            "name": "owner",
                            "type": "address"
                        },
                        {
                            "indexed": True,
                            "internalType": "address",
                            "name": "spender",
                            "type": "address"
                        },
                        {
                            "indexed": False,
                            "internalType": "uint256",
                            "name": "value",
                            "type": "uint256"
                        }
                    ],
                    "name": "Approval",
                    "type": "event"
                },
                {
                    "anonymous": False,
                    "inputs": [
                        {
                            "indexed": True,
                            "internalType": "address",
                            "name": "from",
                            "type": "address"
                        },
                        {
                            "indexed": True,
                            "internalType": "address",
                            "name": "to",
                            "type": "address"
                        },
                        {
                            "indexed": False,
                            "internalType": "uint256",
                            "name": "value",
                            "type": "uint256"
                        }
                    ],
                    "name": "Transfer",
                    "type": "event"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "owner",
                            "type": "address"
                        },
                        {
                            "internalType": "address",
                            "name": "spender",
                            "type": "address"
                        }
                    ],
                    "name": "allowance",
                    "outputs": [
                        {
                            "internalType": "uint256",
                            "name": "",
                            "type": "uint256"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "spender",
                            "type": "address"
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256"
                        }
                    ],
                    "name": "approve",
                    "outputs": [
                        {
                            "internalType": "bool",
                            "name": "",
                            "type": "bool"
                        }
                    ],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "account",
                            "type": "address"
                        }
                    ],
                    "name": "balanceOf",
                    "outputs": [
                        {
                            "internalType": "uint256",
                            "name": "",
                            "type": "uint256"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "decimals",
                    "outputs": [
                        {
                            "internalType": "uint8",
                            "name": "",
                            "type": "uint8"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "spender",
                            "type": "address"
                        },
                        {
                            "internalType": "uint256",
                            "name": "subtractedValue",
                            "type": "uint256"
                        }
                    ],
                    "name": "decreaseAllowance",
                    "outputs": [
                        {
                            "internalType": "bool",
                            "name": "",
                            "type": "bool"
                        }
                    ],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "spender",
                            "type": "address"
                        },
                        {
                            "internalType": "uint256",
                            "name": "addedValue",
                            "type": "uint256"
                        }
                    ],
                    "name": "increaseAllowance",
                    "outputs": [
                        {
                            "internalType": "bool",
                            "name": "",
                            "type": "bool"
                        }
                    ],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "to",
                            "type": "address"
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256"
                        }
                    ],
                    "name": "mint",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "name",
                    "outputs": [
                        {
                            "internalType": "string",
                            "name": "",
                            "type": "string"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "symbol",
                    "outputs": [
                        {
                            "internalType": "string",
                            "name": "",
                            "type": "string"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "totalSupply",
                    "outputs": [
                        {
                            "internalType": "uint256",
                            "name": "",
                            "type": "uint256"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "to",
                            "type": "address"
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256"
                        }
                    ],
                    "name": "transfer",
                    "outputs": [
                        {
                            "internalType": "bool",
                            "name": "",
                            "type": "bool"
                        }
                    ],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "from",
                            "type": "address"
                        },
                        {
                            "internalType": "address",
                            "name": "to",
                            "type": "address"
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256"
                        }
                    ],
                    "name": "transferFrom",
                    "outputs": [
                        {
                            "internalType": "bool",
                            "name": "",
                            "type": "bool"
                        }
                    ],
                    "stateMutability": "nonpayable",
                    "type": "function"
                }
            ]

ABI_LEND_ERC20 = [
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "admin",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "implementation",
        "type": "address"
      }
    ],
    "name": "Upgraded",
    "type": "event"
  },
  {
    "stateMutability": "payable",
    "type": "fallback"
  },
  {
    "inputs": [],
    "name": "admin",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "implementation",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_logic",
        "type": "address"
      },
      {
        "internalType": "bytes",
        "name": "_data",
        "type": "bytes"
      }
    ],
    "name": "initialize",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "newImplementation",
        "type": "address"
      }
    ],
    "name": "upgradeTo",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "newImplementation",
        "type": "address"
      },
      {
        "internalType": "bytes",
        "name": "data",
        "type": "bytes"
      }
    ],
    "name": "upgradeToAndCall",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  }
]

ABI_GET_ASSET_PRICE = [
  {
    "inputs": [
      {
        "internalType": "contract IPoolAddressesProvider",
        "name": "provider",
        "type": "address"
      },
      {
        "internalType": "address[]",
        "name": "assets",
        "type": "address[]"
      },
      {
        "internalType": "address[]",
        "name": "sources",
        "type": "address[]"
      },
      {
        "internalType": "address",
        "name": "fallbackOracle",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "baseCurrency",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "baseCurrencyUnit",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "asset",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "source",
        "type": "address"
      }
    ],
    "name": "AssetSourceUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "baseCurrency",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "baseCurrencyUnit",
        "type": "uint256"
      }
    ],
    "name": "BaseCurrencySet",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "fallbackOracle",
        "type": "address"
      }
    ],
    "name": "FallbackOracleUpdated",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "ADDRESSES_PROVIDER",
    "outputs": [
      {
        "internalType": "contract IPoolAddressesProvider",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "BASE_CURRENCY",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "BASE_CURRENCY_UNIT",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "asset",
        "type": "address"
      }
    ],
    "name": "getAssetPrice",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address[]",
        "name": "assets",
        "type": "address[]"
      }
    ],
    "name": "getAssetsPrices",
    "outputs": [
      {
        "internalType": "uint256[]",
        "name": "",
        "type": "uint256[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getFallbackOracle",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "asset",
        "type": "address"
      }
    ],
    "name": "getSourceOfAsset",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address[]",
        "name": "assets",
        "type": "address[]"
      },
      {
        "internalType": "address[]",
        "name": "sources",
        "type": "address[]"
      }
    ],
    "name": "setAssetSources",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "fallbackOracle",
        "type": "address"
      }
    ],
    "name": "setFallbackOracle",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]

ABI_ORACLE = [
  {
    "inputs": [
      {
        "internalType": "contract IPoolAddressesProvider",
        "name": "provider",
        "type": "address"
      },
      {
        "internalType": "address[]",
        "name": "assets",
        "type": "address[]"
      },
      {
        "internalType": "address[]",
        "name": "sources",
        "type": "address[]"
      },
      {
        "internalType": "address",
        "name": "fallbackOracle",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "baseCurrency",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "baseCurrencyUnit",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "asset",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "source",
        "type": "address"
      }
    ],
    "name": "AssetSourceUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "baseCurrency",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "baseCurrencyUnit",
        "type": "uint256"
      }
    ],
    "name": "BaseCurrencySet",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "fallbackOracle",
        "type": "address"
      }
    ],
    "name": "FallbackOracleUpdated",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "ADDRESSES_PROVIDER",
    "outputs": [
      {
        "internalType": "contract IPoolAddressesProvider",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "BASE_CURRENCY",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "BASE_CURRENCY_UNIT",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "asset",
        "type": "address"
      }
    ],
    "name": "getAssetPrice",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address[]",
        "name": "assets",
        "type": "address[]"
      }
    ],
    "name": "getAssetsPrices",
    "outputs": [
      {
        "internalType": "uint256[]",
        "name": "",
        "type": "uint256[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getFallbackOracle",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "asset",
        "type": "address"
      }
    ],
    "name": "getSourceOfAsset",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address[]",
        "name": "assets",
        "type": "address[]"
      },
      {
        "internalType": "address[]",
        "name": "sources",
        "type": "address[]"
      }
    ],
    "name": "setAssetSources",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "fallbackOracle",
        "type": "address"
      }
    ],
    "name": "setFallbackOracle",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]

ABI_REWARDS = [
              {
                "type": "function",
                "name": "getCurrentRewards",
                "inputs": [
                  {
                    "name": "depositor",
                    "type": "address",
                    "internalType": "address"
                  },
                  {
                    "name": "receiver",
                    "type": "address",
                    "internalType": "address"
                  }
                ],
                "outputs": [
                  {
                    "name": "",
                    "type": "tuple[]",
                    "internalType": "struct Cosmos.Coin[]",
                    "components": [
                      {
                        "name": "amount",
                        "type": "uint256",
                        "internalType": "uint256"
                      },
                      {
                        "name": "denom",
                        "type": "string",
                        "internalType": "string"
                      }
                    ]
                  }
                ],
                "stateMutability": "view"
              },
              {
                "type": "function",
                "name": "getDepositorWithdrawAddress",
                "inputs": [
                  {
                    "name": "depositor",
                    "type": "address",
                    "internalType": "address"
                  }
                ],
                "outputs": [
                  {
                    "name": "",
                    "type": "address",
                    "internalType": "address"
                  }
                ],
                "stateMutability": "view"
              },
              {
                "type": "function",
                "name": "getOutstandingRewards",
                "inputs": [
                  {
                    "name": "receiver",
                    "type": "address",
                    "internalType": "address"
                  }
                ],
                "outputs": [
                  {
                    "name": "",
                    "type": "tuple[]",
                    "internalType": "struct Cosmos.Coin[]",
                    "components": [
                      {
                        "name": "amount",
                        "type": "uint256",
                        "internalType": "uint256"
                      },
                      {
                        "name": "denom",
                        "type": "string",
                        "internalType": "string"
                      }
                    ]
                  }
                ],
                "stateMutability": "view"
              },
              {
                "type": "function",
                "name": "setDepositorWithdrawAddress",
                "inputs": [
                  {
                    "name": "withdrawAddress",
                    "type": "address",
                    "internalType": "address"
                  }
                ],
                "outputs": [
                  {
                    "name": "",
                    "type": "bool",
                    "internalType": "bool"
                  }
                ],
                "stateMutability": "nonpayable"
              },
              {
                "type": "function",
                "name": "withdrawAllDepositorRewards",
                "inputs": [
                  {
                    "name": "receiver",
                    "type": "address",
                    "internalType": "address"
                  }
                ],
                "outputs": [
                  {
                    "name": "",
                    "type": "tuple[]",
                    "internalType": "struct Cosmos.Coin[]",
                    "components": [
                      {
                        "name": "amount",
                        "type": "uint256",
                        "internalType": "uint256"
                      },
                      {
                        "name": "denom",
                        "type": "string",
                        "internalType": "string"
                      }
                    ]
                  }
                ],
                "stateMutability": "nonpayable"
              },
              {
                "type": "function",
                "name": "withdrawDepositorRewards",
                "inputs": [
                  {
                    "name": "receiver",
                    "type": "address",
                    "internalType": "address"
                  },
                  {
                    "name": "amount",
                    "type": "uint256",
                    "internalType": "uint256"
                  }
                ],
                "outputs": [
                  {
                    "name": "",
                    "type": "tuple[]",
                    "internalType": "struct Cosmos.Coin[]",
                    "components": [
                      {
                        "name": "amount",
                        "type": "uint256",
                        "internalType": "uint256"
                      },
                      {
                        "name": "denom",
                        "type": "string",
                        "internalType": "string"
                      }
                    ]
                  }
                ],
                "stateMutability": "nonpayable"
              },
              {
                "type": "function",
                "name": "withdrawDepositorRewardsTo",
                "inputs": [
                  {
                    "name": "receiver",
                    "type": "address",
                    "internalType": "address"
                  },
                  {
                    "name": "recipient",
                    "type": "address",
                    "internalType": "address"
                  },
                  {
                    "name": "amount",
                    "type": "uint256",
                    "internalType": "uint256"
                  }
                ],
                "outputs": [
                  {
                    "name": "",
                    "type": "tuple[]",
                    "internalType": "struct Cosmos.Coin[]",
                    "components": [
                      {
                        "name": "amount",
                        "type": "uint256",
                        "internalType": "uint256"
                      },
                      {
                        "name": "denom",
                        "type": "string",
                        "internalType": "string"
                      }
                    ]
                  }
                ],
                "stateMutability": "nonpayable"
              },
              {
                "type": "event",
                "name": "InitializeDeposit",
                "inputs": [
                  {
                    "name": "caller",
                    "type": "address",
                    "indexed": True,
                    "internalType": "address"
                  },
                  {
                    "name": "depositor",
                    "type": "address",
                    "indexed": True,
                    "internalType": "address"
                  },
                  {
                    "name": "assets",
                    "type": "tuple[]",
                    "indexed": False,
                    "internalType": "struct Cosmos.Coin[]",
                    "components": [
                      {
                        "name": "amount",
                        "type": "uint256",
                        "internalType": "uint256"
                      },
                      {
                        "name": "denom",
                        "type": "string",
                        "internalType": "string"
                      }
                    ]
                  },
                  {
                    "name": "shares",
                    "type": "tuple",
                    "indexed": False,
                    "internalType": "struct Cosmos.Coin",
                    "components": [
                      {
                        "name": "amount",
                        "type": "uint256",
                        "internalType": "uint256"
                      },
                      {
                        "name": "denom",
                        "type": "string",
                        "internalType": "string"
                      }
                    ]
                  }
                ],
                "anonymous": False
              },
              {
                "type": "event",
                "name": "SetDepositorWithdrawAddress",
                "inputs": [
                  {
                    "name": "depositor",
                    "type": "address",
                    "indexed": True,
                    "internalType": "address"
                  },
                  {
                    "name": "withdrawAddress",
                    "type": "address",
                    "indexed": True,
                    "internalType": "address"
                  }
                ],
                "anonymous": False
              },
              {
                "type": "event",
                "name": "WithdrawDepositRewards",
                "inputs": [
                  {
                    "name": "rewardReceiver",
                    "type": "address",
                    "indexed": True,
                    "internalType": "address"
                  },
                  {
                    "name": "withdrawer",
                    "type": "address",
                    "indexed": True,
                    "internalType": "address"
                  },
                  {
                    "name": "rewardRecipient",
                    "type": "address",
                    "indexed": True,
                    "internalType": "address"
                  },
                  {
                    "name": "rewardAmount",
                    "type": "tuple[]",
                    "indexed": False,
                    "internalType": "struct Cosmos.Coin[]",
                    "components": [
                      {
                        "name": "amount",
                        "type": "uint256",
                        "internalType": "uint256"
                      },
                      {
                        "name": "denom",
                        "type": "string",
                        "internalType": "string"
                      }
                    ]
                  }
                ],
                "anonymous": False
              }
            ]

ABI_GOVERNANCE = [
  {
    "type": "function",
    "name": "beginRedelegate",
    "inputs": [
      {
        "name": "srcValidator",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "dstValidator",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "bool",
        "internalType": "bool"
      }
    ],
    "stateMutability": "payable"
  },
  {
    "type": "function",
    "name": "cancelUnbondingDelegation",
    "inputs": [
      {
        "name": "validatorAddress",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "uint256",
        "internalType": "uint256"
      },
      {
        "name": "creationHeight",
        "type": "int64",
        "internalType": "int64"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "bool",
        "internalType": "bool"
      }
    ],
    "stateMutability": "payable"
  },
  {
    "type": "function",
    "name": "delegate",
    "inputs": [
      {
        "name": "validatorAddress",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "bool",
        "internalType": "bool"
      }
    ],
    "stateMutability": "payable"
  },
  {
    "type": "function",
    "name": "getBondedValidators",
    "inputs": [
      {
        "name": "pagination",
        "type": "tuple",
        "internalType": "struct Cosmos.PageRequest",
        "components": [
          {
            "name": "key",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "offset",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "limit",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "countTotal",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "reverse",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct IStakingModule.Validator[]",
        "components": [
          {
            "name": "operatorAddr",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "consAddr",
            "type": "bytes",
            "internalType": "bytes"
          },
          {
            "name": "jailed",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "status",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "tokens",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "delegatorShares",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "description",
            "type": "tuple",
            "internalType": "struct IStakingModule.Description",
            "components": [
              {
                "name": "moniker",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "identity",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "website",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "securityContact",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "details",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "unbondingHeight",
            "type": "int64",
            "internalType": "int64"
          },
          {
            "name": "unbondingTime",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "commission",
            "type": "tuple",
            "internalType": "struct IStakingModule.Commission",
            "components": [
              {
                "name": "commissionRates",
                "type": "tuple",
                "internalType": "struct IStakingModule.CommissionRates",
                "components": [
                  {
                    "name": "rate",
                    "type": "uint256",
                    "internalType": "uint256"
                  },
                  {
                    "name": "maxRate",
                    "type": "uint256",
                    "internalType": "uint256"
                  },
                  {
                    "name": "maxChangeRate",
                    "type": "uint256",
                    "internalType": "uint256"
                  }
                ]
              },
              {
                "name": "updateTime",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "minSelfDelegation",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "unbondingOnHoldRefCount",
            "type": "int64",
            "internalType": "int64"
          },
          {
            "name": "unbondingIds",
            "type": "uint64[]",
            "internalType": "uint64[]"
          }
        ]
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct Cosmos.PageResponse",
        "components": [
          {
            "name": "nextKey",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "total",
            "type": "uint64",
            "internalType": "uint64"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getBondedValidatorsByPower",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "address[]",
        "internalType": "address[]"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getDelegation",
    "inputs": [
      {
        "name": "delegatorAddress",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "validatorAddress",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getDelegatorUnbondingDelegations",
    "inputs": [
      {
        "name": "delegatorAddress",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "pagination",
        "type": "tuple",
        "internalType": "struct Cosmos.PageRequest",
        "components": [
          {
            "name": "key",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "offset",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "limit",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "countTotal",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "reverse",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct IStakingModule.UnbondingDelegation[]",
        "components": [
          {
            "name": "delegatorAddress",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "validatorAddress",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "entries",
            "type": "tuple[]",
            "internalType": "struct IStakingModule.UnbondingDelegationEntry[]",
            "components": [
              {
                "name": "creationHeight",
                "type": "int64",
                "internalType": "int64"
              },
              {
                "name": "completionTime",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "initialBalance",
                "type": "uint256",
                "internalType": "uint256"
              },
              {
                "name": "balance",
                "type": "uint256",
                "internalType": "uint256"
              },
              {
                "name": "unbondingId",
                "type": "uint64",
                "internalType": "uint64"
              }
            ]
          }
        ]
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct Cosmos.PageResponse",
        "components": [
          {
            "name": "nextKey",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "total",
            "type": "uint64",
            "internalType": "uint64"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getDelegatorValidators",
    "inputs": [
      {
        "name": "delegatorAddress",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "pagination",
        "type": "tuple",
        "internalType": "struct Cosmos.PageRequest",
        "components": [
          {
            "name": "key",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "offset",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "limit",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "countTotal",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "reverse",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct IStakingModule.Validator[]",
        "components": [
          {
            "name": "operatorAddr",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "consAddr",
            "type": "bytes",
            "internalType": "bytes"
          },
          {
            "name": "jailed",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "status",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "tokens",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "delegatorShares",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "description",
            "type": "tuple",
            "internalType": "struct IStakingModule.Description",
            "components": [
              {
                "name": "moniker",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "identity",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "website",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "securityContact",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "details",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "unbondingHeight",
            "type": "int64",
            "internalType": "int64"
          },
          {
            "name": "unbondingTime",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "commission",
            "type": "tuple",
            "internalType": "struct IStakingModule.Commission",
            "components": [
              {
                "name": "commissionRates",
                "type": "tuple",
                "internalType": "struct IStakingModule.CommissionRates",
                "components": [
                  {
                    "name": "rate",
                    "type": "uint256",
                    "internalType": "uint256"
                  },
                  {
                    "name": "maxRate",
                    "type": "uint256",
                    "internalType": "uint256"
                  },
                  {
                    "name": "maxChangeRate",
                    "type": "uint256",
                    "internalType": "uint256"
                  }
                ]
              },
              {
                "name": "updateTime",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "minSelfDelegation",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "unbondingOnHoldRefCount",
            "type": "int64",
            "internalType": "int64"
          },
          {
            "name": "unbondingIds",
            "type": "uint64[]",
            "internalType": "uint64[]"
          }
        ]
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct Cosmos.PageResponse",
        "components": [
          {
            "name": "nextKey",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "total",
            "type": "uint64",
            "internalType": "uint64"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getRedelegations",
    "inputs": [
      {
        "name": "delegatorAddress",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "srcValidator",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "dstValidator",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "pagination",
        "type": "tuple",
        "internalType": "struct Cosmos.PageRequest",
        "components": [
          {
            "name": "key",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "offset",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "limit",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "countTotal",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "reverse",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct IStakingModule.RedelegationEntry[]",
        "components": [
          {
            "name": "creationHeight",
            "type": "int64",
            "internalType": "int64"
          },
          {
            "name": "completionTime",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "initialBalance",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "sharesDst",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "unbondingId",
            "type": "uint64",
            "internalType": "uint64"
          }
        ]
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct Cosmos.PageResponse",
        "components": [
          {
            "name": "nextKey",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "total",
            "type": "uint64",
            "internalType": "uint64"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getUnbondingDelegation",
    "inputs": [
      {
        "name": "delegatorAddress",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "validatorAddress",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct IStakingModule.UnbondingDelegationEntry[]",
        "components": [
          {
            "name": "creationHeight",
            "type": "int64",
            "internalType": "int64"
          },
          {
            "name": "completionTime",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "initialBalance",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "balance",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "unbondingId",
            "type": "uint64",
            "internalType": "uint64"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getValAddressFromConsAddress",
    "inputs": [
      {
        "name": "consAddr",
        "type": "bytes",
        "internalType": "bytes"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "address",
        "internalType": "address"
      }
    ],
    "stateMutability": "pure"
  },
  {
    "type": "function",
    "name": "getValidator",
    "inputs": [
      {
        "name": "validatorAddress",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct IStakingModule.Validator",
        "components": [
          {
            "name": "operatorAddr",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "consAddr",
            "type": "bytes",
            "internalType": "bytes"
          },
          {
            "name": "jailed",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "status",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "tokens",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "delegatorShares",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "description",
            "type": "tuple",
            "internalType": "struct IStakingModule.Description",
            "components": [
              {
                "name": "moniker",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "identity",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "website",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "securityContact",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "details",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "unbondingHeight",
            "type": "int64",
            "internalType": "int64"
          },
          {
            "name": "unbondingTime",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "commission",
            "type": "tuple",
            "internalType": "struct IStakingModule.Commission",
            "components": [
              {
                "name": "commissionRates",
                "type": "tuple",
                "internalType": "struct IStakingModule.CommissionRates",
                "components": [
                  {
                    "name": "rate",
                    "type": "uint256",
                    "internalType": "uint256"
                  },
                  {
                    "name": "maxRate",
                    "type": "uint256",
                    "internalType": "uint256"
                  },
                  {
                    "name": "maxChangeRate",
                    "type": "uint256",
                    "internalType": "uint256"
                  }
                ]
              },
              {
                "name": "updateTime",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "minSelfDelegation",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "unbondingOnHoldRefCount",
            "type": "int64",
            "internalType": "int64"
          },
          {
            "name": "unbondingIds",
            "type": "uint64[]",
            "internalType": "uint64[]"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getValidatorDelegations",
    "inputs": [
      {
        "name": "validatorAddress",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "pagination",
        "type": "tuple",
        "internalType": "struct Cosmos.PageRequest",
        "components": [
          {
            "name": "key",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "offset",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "limit",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "countTotal",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "reverse",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct IStakingModule.Delegation[]",
        "components": [
          {
            "name": "delegator",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "balance",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "shares",
            "type": "uint256",
            "internalType": "uint256"
          }
        ]
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct Cosmos.PageResponse",
        "components": [
          {
            "name": "nextKey",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "total",
            "type": "uint64",
            "internalType": "uint64"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getValidators",
    "inputs": [
      {
        "name": "pagination",
        "type": "tuple",
        "internalType": "struct Cosmos.PageRequest",
        "components": [
          {
            "name": "key",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "offset",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "limit",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "countTotal",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "reverse",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct IStakingModule.Validator[]",
        "components": [
          {
            "name": "operatorAddr",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "consAddr",
            "type": "bytes",
            "internalType": "bytes"
          },
          {
            "name": "jailed",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "status",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "tokens",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "delegatorShares",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "description",
            "type": "tuple",
            "internalType": "struct IStakingModule.Description",
            "components": [
              {
                "name": "moniker",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "identity",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "website",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "securityContact",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "details",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "unbondingHeight",
            "type": "int64",
            "internalType": "int64"
          },
          {
            "name": "unbondingTime",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "commission",
            "type": "tuple",
            "internalType": "struct IStakingModule.Commission",
            "components": [
              {
                "name": "commissionRates",
                "type": "tuple",
                "internalType": "struct IStakingModule.CommissionRates",
                "components": [
                  {
                    "name": "rate",
                    "type": "uint256",
                    "internalType": "uint256"
                  },
                  {
                    "name": "maxRate",
                    "type": "uint256",
                    "internalType": "uint256"
                  },
                  {
                    "name": "maxChangeRate",
                    "type": "uint256",
                    "internalType": "uint256"
                  }
                ]
              },
              {
                "name": "updateTime",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "minSelfDelegation",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "unbondingOnHoldRefCount",
            "type": "int64",
            "internalType": "int64"
          },
          {
            "name": "unbondingIds",
            "type": "uint64[]",
            "internalType": "uint64[]"
          }
        ]
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct Cosmos.PageResponse",
        "components": [
          {
            "name": "nextKey",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "total",
            "type": "uint64",
            "internalType": "uint64"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "undelegate",
    "inputs": [
      {
        "name": "validatorAddress",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "bool",
        "internalType": "bool"
      }
    ],
    "stateMutability": "payable"
  },
  {
    "type": "event",
    "name": "CancelUnbondingDelegation",
    "inputs": [
      {
        "name": "validator",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      },
      {
        "name": "delegator",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "tuple[]",
        "indexed": False,
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      },
      {
        "name": "creationHeight",
        "type": "int64",
        "indexed": False,
        "internalType": "int64"
      }
    ],
    "anonymous": False
  },
  {
    "type": "event",
    "name": "CreateValidator",
    "inputs": [
      {
        "name": "validator",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "tuple[]",
        "indexed": False,
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "anonymous": False
  },
  {
    "type": "event",
    "name": "Delegate",
    "inputs": [
      {
        "name": "validator",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "tuple[]",
        "indexed": False,
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "anonymous": False
  },
  {
    "type": "event",
    "name": "Redelegate",
    "inputs": [
      {
        "name": "sourceValidator",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      },
      {
        "name": "destinationValidator",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "tuple[]",
        "indexed": False,
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "anonymous": False
  },
  {
    "type": "event",
    "name": "Unbond",
    "inputs": [
      {
        "name": "validator",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "tuple[]",
        "indexed": False,
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "anonymous": False
  }
]

ABI_VOTE = [
  {
    "type": "function",
    "name": "cancelProposal",
    "inputs": [
      {
        "name": "proposalId",
        "type": "uint64",
        "internalType": "uint64"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "uint64",
        "internalType": "uint64"
      },
      {
        "name": "",
        "type": "uint64",
        "internalType": "uint64"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "getConstitution",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "string",
        "internalType": "string"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getDepositParams",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct IGovernanceModule.DepositParams",
        "components": [
          {
            "name": "minDeposit",
            "type": "tuple[]",
            "internalType": "struct Cosmos.Coin[]",
            "components": [
              {
                "name": "amount",
                "type": "uint256",
                "internalType": "uint256"
              },
              {
                "name": "denom",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "maxDepositPeriod",
            "type": "uint64",
            "internalType": "uint64"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getParams",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct IGovernanceModule.Params",
        "components": [
          {
            "name": "minDeposit",
            "type": "tuple[]",
            "internalType": "struct Cosmos.Coin[]",
            "components": [
              {
                "name": "amount",
                "type": "uint256",
                "internalType": "uint256"
              },
              {
                "name": "denom",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "maxDepositPeriod",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "votingPeriod",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "quorum",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "threshold",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "vetoThreshold",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "minInitialDepositRatio",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "proposalCancelRatio",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "proposalCancelDest",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "expeditedVotingPeriod",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "expeditedThreshold",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "expeditedMinDeposit",
            "type": "tuple[]",
            "internalType": "struct Cosmos.Coin[]",
            "components": [
              {
                "name": "amount",
                "type": "uint256",
                "internalType": "uint256"
              },
              {
                "name": "denom",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "burnVoteQuorum",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "burnProposalDepositPrevote",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "burnVoteVeto",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getProposal",
    "inputs": [
      {
        "name": "proposalId",
        "type": "uint64",
        "internalType": "uint64"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct IGovernanceModule.Proposal",
        "components": [
          {
            "name": "id",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "messages",
            "type": "tuple[]",
            "internalType": "struct Cosmos.CodecAny[]",
            "components": [
              {
                "name": "typeURL",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "value",
                "type": "bytes",
                "internalType": "bytes"
              }
            ]
          },
          {
            "name": "status",
            "type": "int32",
            "internalType": "int32"
          },
          {
            "name": "finalTallyResult",
            "type": "tuple",
            "internalType": "struct IGovernanceModule.TallyResult",
            "components": [
              {
                "name": "yesCount",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "abstainCount",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "noCount",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "noWithVetoCount",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "submitTime",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "depositEndTime",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "totalDeposit",
            "type": "tuple[]",
            "internalType": "struct Cosmos.Coin[]",
            "components": [
              {
                "name": "amount",
                "type": "uint256",
                "internalType": "uint256"
              },
              {
                "name": "denom",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "votingStartTime",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "votingEndTime",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "metadata",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "title",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "summary",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "proposer",
            "type": "address",
            "internalType": "address"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getProposalDeposits",
    "inputs": [
      {
        "name": "proposalId",
        "type": "uint64",
        "internalType": "uint64"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getProposalDepositsByDepositor",
    "inputs": [
      {
        "name": "proposalId",
        "type": "uint64",
        "internalType": "uint64"
      },
      {
        "name": "depositor",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getProposalTallyResult",
    "inputs": [
      {
        "name": "proposalId",
        "type": "uint64",
        "internalType": "uint64"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct IGovernanceModule.TallyResult",
        "components": [
          {
            "name": "yesCount",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "abstainCount",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "noCount",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "noWithVetoCount",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getProposalVotes",
    "inputs": [
      {
        "name": "proposalId",
        "type": "uint64",
        "internalType": "uint64"
      },
      {
        "name": "pagination",
        "type": "tuple",
        "internalType": "struct Cosmos.PageRequest",
        "components": [
          {
            "name": "key",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "offset",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "limit",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "countTotal",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "reverse",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct IGovernanceModule.Vote[]",
        "components": [
          {
            "name": "proposalId",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "voter",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "options",
            "type": "tuple[]",
            "internalType": "struct IGovernanceModule.WeightedVoteOption[]",
            "components": [
              {
                "name": "voteOption",
                "type": "int32",
                "internalType": "int32"
              },
              {
                "name": "weight",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "metadata",
            "type": "string",
            "internalType": "string"
          }
        ]
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct Cosmos.PageResponse",
        "components": [
          {
            "name": "nextKey",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "total",
            "type": "uint64",
            "internalType": "uint64"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getProposalVotesByVoter",
    "inputs": [
      {
        "name": "proposalId",
        "type": "uint64",
        "internalType": "uint64"
      },
      {
        "name": "voter",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct IGovernanceModule.Vote",
        "components": [
          {
            "name": "proposalId",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "voter",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "options",
            "type": "tuple[]",
            "internalType": "struct IGovernanceModule.WeightedVoteOption[]",
            "components": [
              {
                "name": "voteOption",
                "type": "int32",
                "internalType": "int32"
              },
              {
                "name": "weight",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "metadata",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getProposals",
    "inputs": [
      {
        "name": "proposalStatus",
        "type": "int32",
        "internalType": "int32"
      },
      {
        "name": "pagination",
        "type": "tuple",
        "internalType": "struct Cosmos.PageRequest",
        "components": [
          {
            "name": "key",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "offset",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "limit",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "countTotal",
            "type": "bool",
            "internalType": "bool"
          },
          {
            "name": "reverse",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct IGovernanceModule.Proposal[]",
        "components": [
          {
            "name": "id",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "messages",
            "type": "tuple[]",
            "internalType": "struct Cosmos.CodecAny[]",
            "components": [
              {
                "name": "typeURL",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "value",
                "type": "bytes",
                "internalType": "bytes"
              }
            ]
          },
          {
            "name": "status",
            "type": "int32",
            "internalType": "int32"
          },
          {
            "name": "finalTallyResult",
            "type": "tuple",
            "internalType": "struct IGovernanceModule.TallyResult",
            "components": [
              {
                "name": "yesCount",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "abstainCount",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "noCount",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "noWithVetoCount",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "submitTime",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "depositEndTime",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "totalDeposit",
            "type": "tuple[]",
            "internalType": "struct Cosmos.Coin[]",
            "components": [
              {
                "name": "amount",
                "type": "uint256",
                "internalType": "uint256"
              },
              {
                "name": "denom",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "votingStartTime",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "votingEndTime",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "metadata",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "title",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "summary",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "proposer",
            "type": "address",
            "internalType": "address"
          }
        ]
      },
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct Cosmos.PageResponse",
        "components": [
          {
            "name": "nextKey",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "total",
            "type": "uint64",
            "internalType": "uint64"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getTallyParams",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct IGovernanceModule.TallyParams",
        "components": [
          {
            "name": "quorum",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "threshold",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "vetoThreshold",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getVotingParams",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "tuple",
        "internalType": "struct IGovernanceModule.VotingParams",
        "components": [
          {
            "name": "votingPeriod",
            "type": "uint64",
            "internalType": "uint64"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "submitProposal",
    "inputs": [
      {
        "name": "proposal",
        "type": "tuple",
        "internalType": "struct IGovernanceModule.MsgSubmitProposal",
        "components": [
          {
            "name": "messages",
            "type": "tuple[]",
            "internalType": "struct Cosmos.CodecAny[]",
            "components": [
              {
                "name": "typeURL",
                "type": "string",
                "internalType": "string"
              },
              {
                "name": "value",
                "type": "bytes",
                "internalType": "bytes"
              }
            ]
          },
          {
            "name": "initialDeposit",
            "type": "tuple[]",
            "internalType": "struct Cosmos.Coin[]",
            "components": [
              {
                "name": "amount",
                "type": "uint256",
                "internalType": "uint256"
              },
              {
                "name": "denom",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "proposer",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "metadata",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "title",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "summary",
            "type": "string",
            "internalType": "string"
          },
          {
            "name": "expedited",
            "type": "bool",
            "internalType": "bool"
          }
        ]
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "uint64",
        "internalType": "uint64"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "vote",
    "inputs": [
      {
        "name": "proposalId",
        "type": "uint64",
        "internalType": "uint64"
      },
      {
        "name": "option",
        "type": "int32",
        "internalType": "int32"
      },
      {
        "name": "metadata",
        "type": "string",
        "internalType": "string"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "bool",
        "internalType": "bool"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "function",
    "name": "voteWeighted",
    "inputs": [
      {
        "name": "proposalId",
        "type": "uint64",
        "internalType": "uint64"
      },
      {
        "name": "options",
        "type": "tuple[]",
        "internalType": "struct IGovernanceModule.WeightedVoteOption[]",
        "components": [
          {
            "name": "voteOption",
            "type": "int32",
            "internalType": "int32"
          },
          {
            "name": "weight",
            "type": "string",
            "internalType": "string"
          }
        ]
      },
      {
        "name": "metadata",
        "type": "string",
        "internalType": "string"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "bool",
        "internalType": "bool"
      }
    ],
    "stateMutability": "nonpayable"
  },
  {
    "type": "event",
    "name": "CancelProposal",
    "inputs": [
      {
        "name": "proposalId",
        "type": "uint64",
        "indexed": True,
        "internalType": "uint64"
      },
      {
        "name": "sender",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      }
    ],
    "anonymous": False
  },
  {
    "type": "event",
    "name": "ProposalDeposit",
    "inputs": [
      {
        "name": "proposalId",
        "type": "uint64",
        "indexed": True,
        "internalType": "uint64"
      },
      {
        "name": "amount",
        "type": "tuple[]",
        "indexed": False,
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "anonymous": False
  },
  {
    "type": "event",
    "name": "ProposalSubmitted",
    "inputs": [
      {
        "name": "proposalId",
        "type": "uint64",
        "indexed": True,
        "internalType": "uint64"
      },
      {
        "name": "proposalSender",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      }
    ],
    "anonymous": False
  },
  {
    "type": "event",
    "name": "ProposalVoted",
    "inputs": [
      {
        "name": "proposalVote",
        "type": "tuple",
        "indexed": False,
        "internalType": "struct IGovernanceModule.Vote",
        "components": [
          {
            "name": "proposalId",
            "type": "uint64",
            "internalType": "uint64"
          },
          {
            "name": "voter",
            "type": "address",
            "internalType": "address"
          },
          {
            "name": "options",
            "type": "tuple[]",
            "internalType": "struct IGovernanceModule.WeightedVoteOption[]",
            "components": [
              {
                "name": "voteOption",
                "type": "int32",
                "internalType": "int32"
              },
              {
                "name": "weight",
                "type": "string",
                "internalType": "string"
              }
            ]
          },
          {
            "name": "metadata",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "anonymous": False
  }
]

ABI_BANK = [
  {
    "type": "function",
    "name": "getAllBalances",
    "inputs": [
      {
        "name": "accountAddress",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getAllSpendableBalances",
    "inputs": [
      {
        "name": "accountAddress",
        "type": "address",
        "internalType": "address"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getAllSupply",
    "inputs": [],
    "outputs": [
      {
        "name": "",
        "type": "tuple[]",
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getBalance",
    "inputs": [
      {
        "name": "accountAddress",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "denom",
        "type": "string",
        "internalType": "string"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getSpendableBalance",
    "inputs": [
      {
        "name": "accountAddress",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "denom",
        "type": "string",
        "internalType": "string"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "getSupply",
    "inputs": [
      {
        "name": "denom",
        "type": "string",
        "internalType": "string"
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "uint256",
        "internalType": "uint256"
      }
    ],
    "stateMutability": "view"
  },
  {
    "type": "function",
    "name": "send",
    "inputs": [
      {
        "name": "toAddress",
        "type": "address",
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "tuple[]",
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "outputs": [
      {
        "name": "",
        "type": "bool",
        "internalType": "bool"
      }
    ],
    "stateMutability": "payable"
  },
  {
    "type": "event",
    "name": "Burn",
    "inputs": [
      {
        "name": "burner",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "tuple[]",
        "indexed": False,
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "anonymous": False
  },
  {
    "type": "event",
    "name": "CoinReceived",
    "inputs": [
      {
        "name": "receiver",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "tuple[]",
        "indexed": False,
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "anonymous": False
  },
  {
    "type": "event",
    "name": "CoinSpent",
    "inputs": [
      {
        "name": "spender",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "tuple[]",
        "indexed": False,
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "anonymous": False
  },
  {
    "type": "event",
    "name": "Coinbase",
    "inputs": [
      {
        "name": "minter",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "tuple[]",
        "indexed": False,
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "anonymous": False
  },
  {
    "type": "event",
    "name": "Message",
    "inputs": [
      {
        "name": "sender",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      }
    ],
    "anonymous": False
  },
  {
    "type": "event",
    "name": "Transfer",
    "inputs": [
      {
        "name": "recipient",
        "type": "address",
        "indexed": True,
        "internalType": "address"
      },
      {
        "name": "amount",
        "type": "tuple[]",
        "indexed": False,
        "internalType": "struct Cosmos.Coin[]",
        "components": [
          {
            "name": "amount",
            "type": "uint256",
            "internalType": "uint256"
          },
          {
            "name": "denom",
            "type": "string",
            "internalType": "string"
          }
        ]
      }
    ],
    "anonymous": False
  }
]

DEFAULT_ABI_LIST=   {
                    'WBERA' :        {'type': 'ETH',          'address':    '0x5806E416dA447b267cEA759358cF22Cc41FAE80F',    'abi': ABI_WETH},
                    'HONEY' :        {'type': 'ERC20',        'address':    '0x7EeCA4205fF31f947EdBd49195a7A88E6A91161B',    'abi': ABI_DEFAULT},
                    'stgUSDC' :      {'type': 'ERC20',        'address':    '0x6581e59A1C8dA66eD0D313a0d4029DcE2F746Cc5',    'abi': ABI_WETH},
                    'devUSDC' :      {'type': 'ERC20',        'address':    '0x959723c105eD00cc51Deb67FFdeDdD42c6390B2C',    'abi': ABI_DEVUSDC},
                    'WETH' :         {'type': 'ERC20',        'address':    '0x8239FBb3e3D0C2cDFd7888D8aF7701240Ac4DcA4',    'abi': ABI_ERC20},
                    'WBTC' :         {'type': 'ERC20',        'address':    '0x9DAD8A1F64692adeB74ACa26129e0F16897fF4BB',    'abi': ABI_ERC20},
                    'aHONEY' :       {'type': 'sERC20',       'address':    '0xc63FAb87Cb00249190577937Ab6E04dA0AE69633',    'abi': ABI_ERC20},
                    'aWETH' :        {'type': 'sERC20',       'address':    '0xa9277257eA552b2673FB02EF36F070733bB01188',    'abi': ABI_ERC20},
                    'aWBTC' :        {'type': 'sERC20',       'address':    '0x6070AB34ECCD909f7C2ab8fd920Ff0eB1FCab185',    'abi': ABI_ERC20},
                    'bHONEY' :       {'type': 'sERC20',       'address':    '0x95c5B81Fb99c91D4EAE15a28302c0200607b9D4e',    'abi': ABI_ERC20},
                    'vdHONEY' :      {'type': 'borrowERC20',  'address':    '0x782a1709b987F2C80c03c95560BBB6D27103a2a7',    'abi': ABI_ERC20},
                    'HONEY dAPP' :   {'type': 'dAPP',         'address':    '0x09ec711b81cD27A6466EC40960F2f8D85BB129D9',    'abi': ABI_HONEY},
                    'BEND' :         {'type': 'dAPP',         'address':    '0x9261b5891d3556e829579964B38fe706D0A2D04a',    'abi': ABI_BEND},
                    'BERADEX' :      {'type': 'DEX',          'address':    '0x0d5862FDbdd12490f9b4De54c236cff63B038074',    'abi': ABI_BEX},
                    'ZNS DOMAIN' :   {'type': 'DOMAIN',       'address':    '0x01529AF16A8D73F4b9D521Bceb48d5aDA028E922',    'abi': ABI_DOMAIN},
                    'MULTICALL' :    {'type': 'Contract',     'address':    '0xcA11bde05977b3631167028862bE2a173976CA11',    'abi': ABI_MULTICALL},
                    'ORACLE' :       {'type': 'Contract',     'address':    '0x3031fE6A015f367D675476F48499C8A9517cEc34',    'abi': ABI_ORACLE},
                    'REWARDS':       {'type': 'Contract',     'address':    '0x55684e2cA2bace0aDc512C1AFF880b15b8eA7214',    'abi': ABI_REWARDS},
                    'GOVERNANCE':    {'type': 'Contract',     'address':    '0xd9A998CaC66092748FfEc7cFBD155Aae1737C2fF',    'abi': ABI_GOVERNANCE},
                    'VOTE':          {'type': 'Contract',     'address':    '0x7b5Fe22B5446f7C62Ea27B8BD71CeF94e03f3dF2',    'abi': ABI_VOTE},
                    'BANK':          {'type': 'Contract',     'address':    '0x4381dC2aB14285160c808659aEe005D51255adD7',    'abi': ABI_BANK}
                    }

#endregion

#//COMPLETE ABI SYNTHR
#region synthr demo

SYNTHR_ABI_ERC20 = [{'inputs': [{'internalType': 'address', 'name': '_owner', 'type': 'address'}, {'internalType': 'address', 'name': '_resolver', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Burn', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': 'name', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'address', 'name': 'destination', 'type': 'address'}], 'name': 'CacheUpdated', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'authorizedToSnapshot', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'authorized', 'type': 'bool'}], 'name': 'ChangeAuthorizedToSnapshot', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Mint', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'oldOwner', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'newOwner', 'type': 'address'}], 'name': 'OwnerChanged', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'newOwner', 'type': 'address'}], 'name': 'OwnerNominated', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'inputs': [], 'name': 'CONTRACT_NAME', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'acceptOwnership', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'addAuthorizedToSnapshot', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'authorizedToSnapshot', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'periodId', 'type': 'uint256'}], 'name': 'balanceOfOnPeriod', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'balances', 'outputs': [{'internalType': 'uint128', 'name': 'amount', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'periodId', 'type': 'uint128'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'burnShare', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'currentPeriodId', 'outputs': [{'internalType': 'uint128', 'name': '', 'type': 'uint128'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'debtRatio', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'isResolverCached', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'mintShare', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_owner', 'type': 'address'}], 'name': 'nominateNewOwner', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'nominatedOwner', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'owner', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'rebuildCache', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'removeAuthorizedToSnapshot', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'resolver', 'outputs': [{'internalType': 'contract AddressResolver', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'resolverAddressesRequired', 'outputs': [{'internalType': 'bytes32[]', 'name': 'addresses', 'type': 'bytes32[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'sharePercent', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'periodId', 'type': 'uint256'}], 'name': 'sharePercentOnPeriod', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint128', 'name': 'id', 'type': 'uint128'}], 'name': 'takeSnapshot', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'totalSupplyOnPeriod', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}]

SYNTHR_ABI_FAUCET = [{'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'previousOwner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'newOwner', 'type': 'address'}], 'name': 'OwnershipTransferred', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}], 'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'faucetLimit', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'faucetToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'owner', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'renounceOwnership', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'newOwner', 'type': 'address'}], 'name': 'transferOwnership', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}]

SYNTHR_ABI_LEND = [{'inputs': [{'internalType': 'contract ExternWrappedStateToken', 'name': '_extTokenState', 'type': 'address'}, {'internalType': 'address', 'name': '_owner', 'type': 'address'}, {'internalType': 'address', 'name': '_resolver', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'synthRedeemed', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amountLiquidated', 'type': 'uint256'}, {'indexed': False, 'internalType': 'address', 'name': 'liquidator', 'type': 'address'}], 'name': 'AccountLiquidated', 'type': 'event'}, {'anonymous': 
False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': 'name', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'address', 'name': 'destination', 'type': 'address'}], 'name': 'CacheUpdated', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'currencyKey', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'synthAmount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'debtShare', 'type': 'uint256'}], 'name': 'DestBurn', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 
'address'}, {'indexed': False, 'internalType': 'string', 'name': 'message', 'type': 'string'}], 'name': 'DestBurnFailed', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': True, 'internalType': 'bytes32', 'name': 'marketKey', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'marginDelta', 'type': 'uint256'}], 'name': 'DestTransferMargin', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': False, 'internalType': 'string', 'name': 'message', 'type': 'string'}], 'name': 'DestTransferMarginFailed', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'oldOwner', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'newOwner', 'type': 'address'}], 'name': 'OwnerChanged', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'newOwner', 'type': 'address'}], 'name': 'OwnerNominated', 'type': 
'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'collateralKey', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}], 'name': 'StakeCollateral', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'collateralKey', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'address', 'name': 'collateralCurrency', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint16', 'name': 'destChainId', 'type': 'uint16'}], 'name': 'WithdrawCollateral', 'type': 'event'}, {'inputs': [], 'name': 'CONTRACT_NAME', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'acceptOwnership', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'synthKey', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'bridgeName', 'type': 'bytes32'}], 'name': 'burnSynths', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': 'synthKey', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'bridgeName', 'type': 'bytes32'}], 'name': 'burnSynthsToTarget', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_account', 'type': 'address'}, {'internalType': 'uint16', 'name': '_destChainId', 'type': 'uint16'}], 'name': 'chainBalanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_account', 'type': 'address'}, {'internalType': 'bytes32', 'name': '_collateralKey', 'type': 'bytes32'}, {'internalType': 'uint16', 'name': '_destChainId', 'type': 'uint16'}], 'name': 'chainBalanceOfPerKey', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': '_collateralKey', 'type': 'bytes32'}], 'name': 'collateralCurrency', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_account', 'type': 'address'}, {'internalType': 'bytes32', 'name': '_synthKey', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': '_synthAmount', 'type': 'uint256'}], 'name': 'destBurn', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_account', 'type': 'address'}, {'internalType': 'uint256', 'name': '_marginDelta', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': '_marketKey', 'type': 'bytes32'}], 'name': 'destTransferMargin', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': 'sourceCurrencyKey', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'sourceAmount', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'destinationCurrencyKey', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'bridgeName', 'type': 'bytes32'}, {'internalType': 'uint16', 'name': 'destChainId', 'type': 'uint16'}, {'internalType': 
'bool', 'name': 'erc20Payment', 'type': 'bool'}], 'name': 'exchange', 'outputs': [{'internalType': 'uint256', 'name': 'amountReceived', 'type': 'uint256'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': 'sourceCurrencyKey', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'sourceAmount', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'destinationCurrencyKey', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'minAmount', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'bridgeName', 'type': 'bytes32'}, {'internalType': 'uint16', 'name': 'destChainId', 'type': 'uint16'}, {'internalType': 'bool', 'name': 'erc20Payment', 'type': 'bool'}], 'name': 'exchangeAtomically', 
'outputs': [{'internalType': 'uint256', 'name': 'amountReceived', 'type': 'uint256'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'getAvailableCollaterals', 'outputs': [{'internalType': 'bytes32[]', 'name': '', 'type': 'bytes32[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_account', 'type': 'address'}, {'internalType': 'bytes32', 'name': '_collateralKey', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': '_collateralAmount', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': '_bridgeName', 'type': 'bytes32'}, {'internalType': 'uint16', 'name': '_destChainId', 'type': 'uint16'}], 'name': 'getSendWithdrawGasFee', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'initializeLiquidatorRewardsRestitution', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'isResolverCached', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': 'currencyKey', 'type': 'bytes32'}], 'name': 'isWaitingPeriod', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': '_bridgeName', 'type': 'bytes32'}, {'internalType': 'uint16', 'name': '_destChainId', 'type': 'uint16'}, {'internalType': 'bool', 'name': 'erc20Payment', 'type': 'bool'}], 'name': 'issueMaxSynths', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': '_collateralKey', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': '_collateralAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_synthToMint', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': '_bridgeName', 'type': 'bytes32'}, {'internalType': 'uint16', 'name': '_destChainId', 'type': 'uint16'}, {'internalType': 'bool', 'name': 'erc20Payment', 'type': 'bool'}], 'name': 'issueSynths', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'collateralKey', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'bridgeName', 'type': 'bytes32'}, {'internalType': 'uint16', 'name': 'destChainId', 'type': 'uint16'}, {'internalType': 'bool', 'name': 'erc20Payment', 'type': 'bool'}], 'name': 'liquidateDelinquentAccount', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': 'collateralKey', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'bridgeName', 'type': 'bytes32'}, {'internalType': 'uint16', 'name': 'destChainId', 'type': 'uint16'}, {'internalType': 'bool', 'name': 'erc20Payment', 'type': 'bool'}], 'name': 'liquidateSelf', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_owner', 'type': 'address'}], 'name': 'nominateNewOwner', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'nominatedOwner', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': 'sourceCurrencyKey', 'type': 
'bytes32'}, {'internalType': 'uint256', 'name': 'sourceAmount', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'destinationCurrencyKey', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'bridgeName', 'type': 'bytes32'}, {'internalType': 'bytes[]', 'name': 'priceUpdateData', 'type': 'bytes[]'}, {'internalType': 'uint16', 'name': 'destChainId', 'type': 'uint16'}, {'internalType': 'bool', 'name': 'erc20Payment', 'type': 'bool'}], 'name': 'offChainExchange', 'outputs': [{'internalType': 'uint256', 'name': 'amountReceived', 'type': 'uint256'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'owner', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'rebuildCache', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'resolver', 'outputs': [{'internalType': 'contract AddressResolver', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'resolverAddressesRequired', 'outputs': [{'internalType': 'bytes32[]', 'name': 'addresses', 'type': 'bytes32[]'}], 'stateMutability': 'pure', 'type': 'function'}, {'inputs': [], 'name': 'restituted', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'sUSD', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': 'currencyKey', 'type': 'bytes32'}], 'name': 'settle', 'outputs': [{'internalType': 'uint256', 'name': 'reclaimed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'refunded', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'numEntriesSettled', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': '_collateralKey', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': '_collateralAmount', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': '_bridgeName', 'type': 'bytes32'}, {'internalType': 'uint16', 'name': '_destChainId', 'type': 'uint16'}, {'internalType': 'bool', 'name': '_erc20Payment', 'type': 'bool'}], 'name': 'withdrawCollateral', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'stateMutability': 'payable', 'type': 'receive'}]

SYNTHR_ABI_SYNTH = [{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_resolver","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"uint256","name":"synthAmount","type":"uint256"}],"name":"BurnSynthForBridge","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"name","type":"bytes32"},{"indexed":False,"internalType":"address","name":"destination","type":"address"}],"name":"CacheUpdated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"uint256","name":"synthAmount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"debtShare","type":"uint256"}],"name":"DestBurn","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"uint256","name":"synthAmount","type":"uint256"}],"name":"DestIssue","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":False,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerNominated","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"address","name":"synth","type":"address"}],"name":"SynthAdded","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"bytes32","name":"synthKey","type":"bytes32"},{"indexed":False,"internalType":"uint256","name":"synthAmount","type":"uint256"}],"name":"SynthIssueFromSynthrSwap","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"address","name":"synth","type":"address"}],"name":"SynthRemoved","type":"event"},{"inputs":[],"name":"CIRCUIT_BREAKER_SUSPENSION_REASON","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"CONTRACT_NAME","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"acceptOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract ISynth","name":"synth","type":"address"}],"name":"addSynth","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"allNetworksDebtInfo","outputs":[{"internalType":"uint256","name":"debt","type":"uint256"},{"internalType":"uint256","name":"sharesSupply","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"availableCurrencyKeys","outputs":[{"internalType":"bytes32[]","name":"","type":"bytes32[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"availableSynthCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"availableSynths","outputs":[{"internalType":"contract ISynth","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_synthKey","type":"bytes32"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes32","name":"_bridgeName","type":"bytes32"},{"internalType":"uint16","name":"_destChainId","type":"uint16"},{"internalType":"bool","name":"_erc20Payment","type":"bool"}],"name":"bridgeSynth","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"deprecatedSynth","type":"address"},{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"balance","type":"uint256"}],"name":"burnForRedemption","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"bytes32","name":"synthKey","type":"bytes32"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnSynths","outputs":[{"internalType":"uint256","name":"synthAmount","type":"uint256"},{"internalType":"uint256","name":"debtShare","type":"uint256"},{"internalType":"uint256","name":"reclaimed","type":"uint256"},{"internalType":"uint256","name":"refunded","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"bytes32","name":"synthKey","type":"bytes32"}],"name":"burnSynthsToTarget","outputs":[{"internalType":"uint256","name":"synthAmount","type":"uint256"},{"internalType":"uint256","name":"debtShare","type":"uint256"},{"internalType":"uint256","name":"reclaimed","type":"uint256"},{"internalType":"uint256","name":"refunded","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnSynthsWithoutDebt","outputs":[{"internalType":"uint256","name":"burnAmount","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"canBurnSynths","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"},{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"uint16","name":"_chainId","type":"uint16"}],"name":"checkFreeCollateral","outputs":[{"internalType":"uint256","name":"withdrawableSynthr","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"collateral","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"}],"name":"collateralisationRatio","outputs":[{"internalType":"uint256","name":"cratio","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"}],"name":"collateralisationRatioAndAnyRatesInvalid","outputs":[{"internalType":"uint256","name":"cratio","type":"uint256"},{"internalType":"bool","name":"anyRateIsInvalid","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"}],"name":"debtBalanceOf","outputs":[{"internalType":"uint256","name":"debtBalance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_synthKey","type":"bytes32"},{"internalType":"uint256","name":"_synthAmount","type":"uint256"}],"name":"destBurn","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_synthKey","type":"bytes32"},{"internalType":"uint256","name":"_synthAmount","type":"uint256"}],"name":"destIssue","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_synthKey","type":"bytes32"},{"internalType":"uint256","name":"_synthAmount","type":"uint256"},{"internalType":"bytes32","name":"_bridgeName","type":"bytes32"},{"internalType":"uint16","name":"_destChainId","type":"uint16"}],"name":"getSendBridgeSynthGasFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"bytes32","name":"_bridgeName","type":"bytes32"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"bool","name":"_isSelf","type":"bool"}],"name":"getSendLiquidateGasFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256","name":"_synthToMint","type":"uint256"},{"internalType":"bytes32","name":"_bridgeName","type":"bytes32"},{"internalType":"uint16","name":"_destChainId","type":"uint16"},{"internalType":"bool","name":"_issueMax","type":"bool"}],"name":"getSendMintGasFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32[]","name":"currencyKeys","type":"bytes32[]"}],"name":"getSynths","outputs":[{"internalType":"contract ISynth[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isResolverCached","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"},{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"uint256","name":"_collateralAmount","type":"uint256"},{"internalType":"uint256","name":"_cRatio","type":"uint256"}],"name":"issuableSynthExpected","outputs":[{"internalType":"uint256","name":"maxIssuable","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"issuanceRatio","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256","name":"destChainId","type":"uint256"}],"name":"issueMaxSynths","outputs":[{"internalType":"uint256","name":"synthAmount","type":"uint256"},{"internalType":"uint256","name":"debtShare","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"destChainId","type":"uint256"}],"name":"issueSynths","outputs":[{"internalType":"uint256","name":"synthAmount","type":"uint256"},{"internalType":"uint256","name":"debtShare","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"lastDebtRatio","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"lastIssueEvent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"bool","name":"isSelfLiquidation","type":"bool"}],"name":"liquidateAccount","outputs":[{"internalType":"uint256","name":"totalRedeemed","type":"uint256"},{"internalType":"uint256","name":"amountToLiquidate","type":"uint256"},{"internalType":"uint256","name":"sharesToRemove","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"bool","name":"_isSelfLiquidation","type":"bool"}],"name":"liquidateAmount","outputs":[{"internalType":"uint256","name":"totalRedeemed","type":"uint256"},{"internalType":"uint256","name":"amountToLiquidate","type":"uint256"},{"internalType":"bool","name":"removeFlag","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"}],"name":"maxIssuableSynths","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minimumStakeTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"nominateNewOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"nominatedOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rebuildCache","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"}],"name":"remainingIssuableSynths","outputs":[{"internalType":"uint256","name":"maxIssuable","type":"uint256"},{"internalType":"uint256","name":"alreadyIssued","type":"uint256"},{"internalType":"uint256","name":"totalSystemDebt","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"removeSynth","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"resolver","outputs":[{"internalType":"contract AddressResolver","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"resolverAddressesRequired","outputs":[{"internalType":"bytes32[]","name":"addresses","type":"bytes32[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint128","name":"periodId","type":"uint128"}],"name":"setCurrentPeriodId","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"ratio","type":"uint256"}],"name":"setLastDebtRatio","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_synthKey","type":"bytes32"},{"internalType":"uint256","name":"_synthAmount","type":"uint256"}],"name":"synthIssueFromSynthrSwap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"synths","outputs":[{"internalType":"contract ISynth","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"synthsByAddress","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"totalIssuedSynths","outputs":[{"internalType":"uint256","name":"totalIssued","type":"uint256"}],"stateMutability":"view","type":"function"}]


#endregion

def main():
  pass
if __name__ == '__main__':
    main()
