
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from abi_list import *
DIVIDER = "-" * 80
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"



MAIN_DICT = {
'multichain':           {
    'token':            [
                        {
                            'name': 'DEFAULT_ERC20',
                            'address': 'DEFAULT_ERC20',
                            'abi': ABI_ERC20,
                        },
                        {
                            'name': 'ZERO_ADDRESS',
                            'address': '0x0000000000000000000000000000000000000000',
                        },
                        ],
    'nft':              [
                        {
                            'name': 'DEFAULT_ERC721',
                            'address': 'DEFAULT_ERC721',
                            'abi': ABI_ERC721,
                        }
                        ],
    'pool':             [],
    'contract':         [

                        {
                            'name': 'Multicall',
                            'address': '0xcA11bde05977b3631167028862bE2a173976CA11',
                            'abi': ABI_MULTICALL,
                        },
                        {
                            'name': 'AaveOracle',
                            'address': '0x3031fE6A015f367D675476F48499C8A9517cEc34',
                            'abi': ABI_AAVE_ORACLE,
                        },
                        {
                            'name': 'UiPoolDataProvider',
                            'address': '0xfb618D1e361C362adDE4E148A4Dc85465a0A4A22',
                            'abi': ABI_UIPOOLDATA_PROVIDER,
                        },



                        ],
                        },


            
'berachain':            {
    
            'token':    [
                        {
                            'name': 'WBERA',
                            'address': '0x5806E416dA447b267cEA759358cF22Cc41FAE80F',
                            'abi': ABI_WETH,
                            'native' : True,
                            'swap': False,
                            'lend': False,
                            'decimals': 18,
                        },
                        {
                            'name':'HONEY',
                            'address' : '0x7EeCA4205fF31f947EdBd49195a7A88E6A91161B',
                            'abi': ABI_ERC20,
                            'swap': True,
                            'lend': True,
                            'assetOut_name' : 'aHONEY',
                            'assetOut_address' : '0xc63FAb87Cb00249190577937Ab6E04dA0AE69633',
                            'decimals': 18
                        },
                        {
                            'name':'bHONEY',
                            'address' : '0x95c5B81Fb99c91D4EAE15a28302c0200607b9D4e',
                            'abi': ABI_ERC20,
                            'swap': False,
                            'lend': False,
                            'decimals': 18
                        },
                        {
                            'name':'STGUSDC',
                            'address' : '0x6581e59A1C8dA66eD0D313a0d4029DcE2F746Cc5',
                            'abi': ABI_ERC20,
                            'swap': True, #TRUE
                            'lend': False,
                            'decimals': 18
                        },
                        {
                            'name':'devUSDC',
                            'address' : '0x959723c105eD00cc51Deb67FFdeDdD42c6390B2C',
                            'abi': ABI_ERC20,
                            'swap': False,
                            'lend': False,
                            'decimals': 18
                        },
                        {
                            'name':'WETH',
                            'address' : '0x8239FBb3e3D0C2cDFd7888D8aF7701240Ac4DcA4',
                            'abi': ABI_ERC20,
                            'swap': True, #TRUE
                            'lend': True,
                            'assetOut_name' : 'aWETH',
                            'assetOut_address' : '0xa9277257eA552b2673FB02EF36F070733bB01188',
                            'decimals': 18
                        },
                        {
                            'name':'WBTC',
                            'address' : '0x9DAD8A1F64692adeB74ACa26129e0F16897fF4BB',
                            'abi': ABI_ERC20,
                            'swap': False, #TRUE
                            'lend': True,
                            'assetOut_name' : 'aWBTC',
                            'assetOut_address' : '0x6070AB34ECCD909f7C2ab8fd920Ff0eB1FCab185',
                            'decimals': 8
                            
                        },
                        {
                            'name':'aHONEY',
                            'address' : '0xc63FAb87Cb00249190577937Ab6E04dA0AE69633',
                            'abi': ABI_ERC20,
                            'swap': False,
                            'lend': False,
                            'decimals': 18
                        },
                        {
                            'name':'aWETH',
                            'address' : '0xa9277257eA552b2673FB02EF36F070733bB01188',
                            'abi': ABI_ERC20,
                            'swap': False,
                            'lend': False,
                            'decimals': 18
                        },
                        {
                            'name':'aWBTC',
                            'address' : '0x6070AB34ECCD909f7C2ab8fd920Ff0eB1FCab185',
                            'abi': ABI_ERC20,
                            'swap': False,
                            'lend': False,
                            'decimals': 8
                        },
                        {
                            'name':'BGT',
                            'address' : '0xAcD97aDBa1207dCf27d5C188455BEa8a32E80B8b',
                            'abi': ABI_ERC20,
                            'swap': False,
                            'lend': False,
                            'decimals': 18
                            
                        },
                        
                        ],
            'nft':      [
                        {
                            'name':'NFT OOGA_BOOGA',
                            'address':'0x6553444CaA1d4FA329aa9872008ca70AE6131925',
                            'abi': ABI_ERC721,
                            'buy': True,
                            'price' : 4.2
                        },
                        {
                            'name':'NFT BOBA',
                            'address':'0x1F136a43101D12F98c9887D46D7cDbEFACdd573D',
                            'abi': ABI_ERC721,
                            'buy': False,
                        },
                        {
                            'name':'NFT VALENTINE',
                            'address':'0xAd8fD889c77Ba37cECc0A4148C6917a4582c15DB',
                            'abi': ABI_ERC721,
                            'buy': False,
                        },
                        {
                            'name':'NFT LNY',
                            'address':'0xDc094eaC7CC01224E798F34543a8F9e9D2559479',
                            'abi': ABI_ERC721,
                            'buy': False,
                        },
                        {
                            'name':'NFT ZNS BERA',
                            'address':'0x01529AF16A8D73F4b9D521Bceb48d5aDA028E922',
                            'abi': ABI_DOMAIN,
                            'buy': False,

                        }
                        ],
            'pool':     [
                        {
                            'name': '50WBERA-50HONEY',
                            'address': '0xa88572F08f79D28b8f864350f122c1CC0AbB0d96',
                            'token1': '0x5806E416dA447b267cEA759358cF22Cc41FAE80F',
                            'token1_name': 'WBERA',
                            'token2': '0x7EeCA4205fF31f947EdBd49195a7A88E6A91161B',
                            'token2_name' : 'HONEY'
                        },
                        {
                            'name':'50STGUSDC-50HONEY',
                            'address' : '0x5479FbDef04302D2DEEF0Cc78f7D503d81fDFCC9',
                            'token1': '0x6581e59A1C8dA66eD0D313a0d4029DcE2F746Cc5',
                            'token1_name': 'STGUSDC',
                            'token2': '0x7EeCA4205fF31f947EdBd49195a7A88E6A91161B',
                            'token2_name': 'HONEY'
                        },
                        {
                            'name':'50WBTC-50HONEY',
                            'address' : '0x751524E7bAdd31d018A4CAF4e4924a21b0c13CD0',
                            'token1': '0x9DAD8A1F64692adeB74ACa26129e0F16897fF4BB',
                            'token1_name': 'WBTC',
                            'token2': '0x7EeCA4205fF31f947EdBd49195a7A88E6A91161B',
                            'token2_name': 'HONEY'
                            
                        },
                        {
                            'name':'50WETH-50HONEY',
                            'address' : '0x101f52c804C1C02c0A1D33442ecA30ecb6fB2434',
                            'token1': '0x8239FBb3e3D0C2cDFd7888D8aF7701240Ac4DcA4',
                            'token1_name': 'WETH',
                            'token2': '0x7EeCA4205fF31f947EdBd49195a7A88E6A91161B',
                            'token2_name' : 'HONEY'
                        }
                        ],
            'contract': [
                        {
                            'name': 'HONEY',
                            'address': '0x09ec711b81cD27A6466EC40960F2f8D85BB129D9',
                            'abi': ABI_HONEY,
                        },
                        {
                            'name': 'BEND', #BEND
                            'address': '0x9261b5891d3556e829579964B38fe706D0A2D04a',
                            'borrow': True,
                            'abi': ABI_BEND,
                        },
                        {
                            'name': 'BERADEX',
                            'address': '0x0d5862FDbdd12490f9b4De54c236cff63B038074',
                            'abi': ABI_BEX,
                            'liquiditypools': True,
                        },
                        {
                            'name': 'ZNS DOMAIN',
                            'address': '0x01529AF16A8D73F4b9D521Bceb48d5aDA028E922',
                            'abi': ABI_DOMAIN,
                        },
                        {
                            'name': 'REWARDS',
                            'reward': True,
                            'address': '0x55684e2cA2bace0aDc512C1AFF880b15b8eA7214',
                            'abi': ABI_REWARDS,
                        },
                        {
                            'name': 'BANK',
                            'address': '0x4381dC2aB14285160c808659aEe005D51255adD7',
                            'abi': ABI_BANK,
                        },
                        {
                            'name': 'GOVERNANCE',
                            'address': '0xd9A998CaC66092748FfEc7cFBD155Aae1737C2fF',
                            'abi': ABI_GOVERNANCE,
                        },
                        {
                            'name': 'VOTE',
                            'address': '0x7b5Fe22B5446f7C62Ea27B8BD71CeF94e03f3dF2',
                            'abi': ABI_VOTE,
                        },
                        {
                            'name': 'ORACLE',
                            'address': '0x3031fE6A015f367D675476F48499C8A9517cEc34',
                            'abi': ABI_ORACLE,
                        },
                        {
                            'name': 'MULTICALL',
                            'address': ['0xcA11bde05977b3631167028862bE2a173976CA11','0x9d1dB8253105b007DDDE65Ce262f701814B91125'],
                            'abi': ABI_MULTICALL,
                        },
                        {
                            'name': 'AAVE_ORACLE',
                            'address': '0x3031fE6A015f367D675476F48499C8A9517cEc34',
                            'abi': ABI_AAVE_ORACLE,
                        },
                        {
                            'name': 'EPOCH',
                            'address': '0x612Dd8a861161819A4AD8F6f3E2A0567602877c0',
                            'abi': ABI_EPOCH,
                        }

                        ]
},

#Tokens:
# 'name': The name of the token (ticker)
# 'address': The address of the token contract
# 'abi': The ABI variable of the token contract. Must be imported from abi_list.py
# 'native': True if the token is a native token of the network, False if it is an ERC20 token
# 'swap': True if the token can be swapped, False if it cannot be swapped
# 'lend': True if the token can be lent, False if it cannot be lent
# 'decimals': The number of decimals of the token
# 'assetOut_name': The name of the asset output token. To use when 'lend': True to specify the name of the asset received when lending the token
# 'assetOut_address': The address of the asset output token 


#NFT
# 'name': The name of the NFT (ticker) with NFT prefix. ex: 'NFT BOBA'
# 'address': The address of the NFT contract
# 'buy': True for NFTs that can be bought, False for NFTs that can't be bought. Random NFT to buy will be selected from the list of NFTs with 'buy': True
# 'price' is the price of the NFT in ETH or other currency. if 'buy':True, 'price' is required. If 'buy':False, 'price' is not required.





'sepolia arbitrum':     {
    'token':                    [
                                {'name' : 'USDT',        'type': 'erc20',  'claim':500, 'action':    'faucet',  'address': '0x9aA40Cc99973d8407a2AE7B2237d26E615EcaFd2', 'abi': SYNTHR_ABI_FAUCET},
                                {'name' : 'USDC',        'type': 'erc20',  'claim':500, 'action':    'faucet',  'address': '0xDbc8c016287437ce2cF69fF64c245A4D74599A40', 'abi': SYNTHR_ABI_FAUCET}, 
                                {'name' : 'WETH',        'type': 'erc20',  'claim':2,   'action':    'faucet',  'address': '0x2A1b409Cd444Be8F4388c50997e0Ff87e9e718Ad', 'abi': SYNTHR_ABI_FAUCET},
                                {'name' : 'syUSD',       'type': 'erc20',               'action':    'defi',    'address': '0xDE30D6edD20c573746758E817782e43E747d56CC', 'abi': SYNTHR_ABI_ERC20},
                                {'name' : 'syDOT',       'type': 'erc20',               'action':    'defi',    'address': '0x1EEFcdFa0bf820a975D4b6DBcA4C9469101C9b6e', 'abi': SYNTHR_ABI_ERC20},
                                {'name' : 'syBTC',       'type': 'erc20',               'action':    'defi',    'address': '0xd544C367Cf8E34C260e6785DB909ADd6210f1115', 'abi': SYNTHR_ABI_ERC20},
                                {'name' : 'syAVAX',      'type': 'erc20',               'action':    'defi',    'address': '0x3028D24aF28d7103db6f5754a1663611f6eF683E', 'abi': SYNTHR_ABI_ERC20},
                                {'name' : 'syMATIC',     'type': 'erc20',               'action':    'defi',    'address': '0x9Ef14c18f2Fd7235b902Bc5f2B88d5c754A0128A', 'abi': SYNTHR_ABI_ERC20},
                                ],
    'contract':                 [
                                {'name' : 'Collateral',  'type': 'daPP',                'action':    'defi',    'address': '0xe0875cbd144fe66c015a95e5b2d2c15c3b612179', 'abi': SYNTHR_ABI_LEND},
                                {'name' : 'Synth',       'type': 'daPP',                'action':    'defi',    'address': '0x2F1673beD3E85219E2B01BC988ABCc482261c38c', 'abi': SYNTHR_ABI_SYNTH},
                                ],
    'pool':                     [

                                ],
    'nft':                      [

                                ],
                                },




#region METIS
'metis':                        {
    'nft':                      [
                                {'name': 'NFT HELMET', 'address': '0xF29eA76d01cCfA2f8772519a3813078d267b080D'},
                                ],
},
}

#endregion













#//COMPLETE FUNCTIONS

def filter_assets(main_dict, networks, asset_types, key1='address', key2=None, key3=None, mode='dict', **kwargs):
    """
    Filter assets (tokens, pools, NFTs) based on given parameters within a specific network.

    :param main_dict: The main dictionary containing network information and assets.
    :param network: The network to filter within.
    :param asset_types: A single type or a list of the types of assets to filter ('token', 'pool', 'nft').
    :param key1: The primary key to include in the filtered asset information (default is 'address').
    :param key2: The secondary key to include in the filtered asset information, optional.
    :param key3: The tertiary key to include in the filtered asset information, optional.
    :param kwargs: Key-value pairs of parameters to filter by. ex: name=WETH to retrieve data for WETH token.
    :param mode: The mode of the output data ('dict', 'list', 'single'). Default is 'dict'.
    :return: A list of dictionaries for assets that match the filter criteria. Each dictionary contains specified keys (e.g., the asset's address, name, and/or swap data).
    """
    if not isinstance(networks, list):
        networks = [networks]
    networks.append('multichain')

    # Ensure asset_types is a list, even if a single asset type is provided
    if not isinstance(asset_types, list):
        asset_types = [asset_types]

    filtered_assets = []
    for network in networks:  # Iterate through each specified network
        for asset_type in asset_types:  # Iterate through each specified asset type
            network_info = main_dict.get(network, {})
            assets_info = network_info.get(asset_type, [])

            # Iterate through each asset in the specified type list
            for asset in assets_info:
                match = True  # Assume asset matches until proven otherwise
                for key, value in kwargs.items():
                    # Check if the asset has the attribute and if it matches the filter value
                    
                    asset_value = asset.get(key)
                    # Check if the asset value is a list and the desired value is in the list, or if they are directly equal
                    if not ((isinstance(asset_value, list) and value in asset_value) or asset_value == value):
                        match = False
                        break
                    
                    
                    #if asset.get(key) != value:
                    #    match = False
                    #    break  # Stop checking this asset if any filter does not match
                if match:
                    # If asset matches all filters, process according to the mode
                    asset_dict = {key1: asset.get(key1, None)}
                    if mode == 'dict':
                        if key2 is not None:
                            asset_dict[key2] = asset.get(key2, None)
                        if key3 is not None:
                            asset_dict[key3] = asset.get(key3, None)
                        filtered_assets.append(asset_dict)
                    elif mode == 'list':
                        temp_list = [asset.get(key1, None)]
                        if key2 is not None:
                            temp_list.append(asset.get(key2, None))
                        if key3 is not None:
                            temp_list.append(asset.get(key3, None))
                        filtered_assets.extend(temp_list)
                    elif mode == 'single':
                        return asset.get(key1, None)

                    # If mode is 'single' and a match is found, no need to continue searching
                    if mode == 'single' and filtered_assets:
                        return filtered_assets

    if len(filtered_assets) == 0:
        filtered_assets = None if mode == 'single' else []

    return filtered_assets

def create_dict(main_dict, network, asset_type):
    """
    Extracts assets by type and network from the provided main dictionary.
    """
    result_dict = {}
    if network in main_dict:
        network_dict = main_dict[network]
        if asset_type in network_dict:
            asset_list = network_dict[asset_type]
            for asset in asset_list:
                name = asset.get('name')
                address = asset.get('address')

                if name and address: 
                    result_dict[name] = address
    return result_dict

def create_abi_list(main_dict):
    """
    Creates a dictionary with details extracted from the main dictionary.
    Handles both single and multiple addresses.
    keys are the addresses and values are dictionaries with network, type, name, and abi.
    used for easy access to the ABI of a contract using the address.
    """
    result_dict = {}
    for network, categories in main_dict.items():
        for category, items in categories.items():
            for item in items:
                abi = item.get('abi', None)
                if abi is None:
                    continue
                addresses = item.get('addresses', item.get('address'))
                if addresses is None:
                    continue 
                
                if not isinstance(addresses, list):
                    addresses = [addresses]
                
                for address in addresses:
                    result_dict[address] = {
                        'network': network,
                        'type': category,
                        'name': item['name'],
                        'abi': item['abi'],
                    }
    return result_dict

def print_list_of_dicts(list_of_dicts, debugmode=False):
    """
    Pretty-prints a list of dictionaries.
    """
    abi_list = [value for key, value in list_of_dicts.items()]


    for i, d in enumerate(abi_list):
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


def main():
    MAIN_DICT_ABI_LIST = create_abi_list(MAIN_DICT)

    #print_list_of_dicts(MAIN_DICT_ABI_LIST)
    #output_token_ticker = filter_assets(main_dict=MAIN_DICT, networks='berachain', asset_types='contract', key1='name', address='0xcA11bde05977b3631167028862bE2a173976CA11', mode='single')
    #print(output_token_ticker)


if __name__ == "__main__":
    main()
