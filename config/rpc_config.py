from config.api_list import API_BSCSCAN, API_ETHERSCAN, API_POLYGONSCAN, API_OPTISCAN, API_ARBISCAN, API_GENERAL, API_BERACHAIN_RPC, API_BERACHAIN_RPC2

#//TODO DEPRECIATED. update with new function to build the rpc dict from dataset 
RPC_CONFIGURATION =     {
    'bsc':              {
                        'network': 'bsc',
                        'url': 'https://bsc-dataseed.bnbchain.org',
                        'chain_id': 56,
                        'token':'BNB',
                        'explorer':'https://bscscan.com/tx/',
                        'api_key': API_BSCSCAN,
                        'abi_endpoint': f"https://api-bscscan.com/api?module=contract&action=getabi&address=",
                        'geth_poa_middleware': True,
                        },
    
    'eth':              {
                        'network': 'eth',
                        'url': 'https://eth.llamarpc.com',
                        'chain_id': 1,
                        'token':'ETH',
                        'explorer':'https://etherscan.io/tx/',
                        'api_key': API_ETHERSCAN,
                        'abi_endpoint': f"https://api-etherscan.io/api?module=contract&action=getabi&address=",
                        'geth_poa_middleware': False,
                        },
    
    'matic':            {
                        'network': 'matic',
                        'url': 'https://polygon.drpc.org',
                        'chain_id': 137,
                        'token':'MATIC',
                        'explorer':'https://polygonscan.com/tx/',
                        'api_key': API_POLYGONSCAN,
                        'abi_endpoint' : f"https://api-polygonscan.com/api?module=contract&action=getabi&address=",
                        'geth_poa_middleware': True,
                        }, 
    
    'optimism':         {
                        'network': 'optimism',
                        'url': 'https://optimism.drpc.org',
                        'chain_id': 10,
                        'token':'opETH',
                        'explorer':'https://optimistic.etherscan.io/tx/',
                        'api_key': API_OPTISCAN,
                        'abi_endpoint': f"https://api-optimistic.etherscan.io/api?module=contract&action=getabi&address=",
                        'geth_poa_middleware': False,
                        },
    
    'arbitrum':         {
                        'network': 'arbitrum',
                        'url': 'https://arbitrum.drpc.org',
                        'chain_id': 42161,
                        'token':'arbETH',
                        'explorer':'https://arbiscan.io/tx/',
                        'api_key': API_ARBISCAN,
                        'abi_endpoint': f"https://api-arbiscan.io/api?module=contract&action=getabi&address=",
                        'geth_poa_middleware': False,
                        },
    
    'goerli':           {
                        'network': 'goerli',
                        'url': 'https://ethereum-goerli.publicnode.com',
                        'chain_id': 5,
                        'token':'gETH',
                        'explorer':'https://goerli.etherscan.io/tx/',
                        'api_key': API_GENERAL,
                        'abi_endpoint': f"https://api-goerli.etherscan.io/api?module=contract&action=getabi&address=",
                        'geth_poa_middleware': False,
                        },
    
    
    'mumbai' :          {
                        'network': 'mumbai',
                        'url': 'https://polygon-mumbai-bor.publicnode.com',
                        'url2':'https://endpoints.omniatech.io/v1/matic/mumbai/public',
                        'chain_id': 80001,  'token':'MATIC',
                        'explorer':'https://mumbai.polygonscan.com/tx/',
                        'api_key': API_GENERAL,
                        'abi_endpoint': f"https://api-testnet.polygonscan.com/api?module=contract&action=getabi&address=",
                        'geth_poa_middleware': True,
                        },
    
    'berachain' :       {
                        'network': 'berachain',
                        'url': f'https://frequent-maximum-dream.bera-artio.quiknode.pro/{API_BERACHAIN_RPC}/',
                        'url2':f"https://virulent-quaint-spring.bera-artio.quiknode.pro/{API_BERACHAIN_RPC2}/",
                        'url3':"https://artio.rpc.berachain.com/",
                        'chain_id': 80085,
                        'token': 'BERA', 
                        'explorer':'https://artio.beratrail.io/tx/',
                        'api_key': API_GENERAL,
                        'abi_endpoint': f"https://api.routescan.io/v2/network/testnet/evm/80085/etherscan/api?module=contract&action=getabi&address=",

                        'geth_poa_middleware': True,
                        },
    
    'sepolia arbitrum' :{
                        'network': 'sepolia arbitrum',
                        'url': 'https://arbitrum-sepolia.blockpi.network/v1/rpc/public',
                        'chain_id': 421614, 'token':'ETH',
                        'explorer':'https://sepolia.arbiscan.io//tx/',
                        'api_key': API_GENERAL,
                        'abi_endpoint': f"https://api-sepolia.arbiscan.io/api?module=contract&action=getabi&address=",
                        'geth_poa_middleware': False,
                        }
}

#Alt RPC:
ALT_RPC_ENDPOINT = {
    'mumbai' : ('https://polygon-mumbai-bor.publicnode.com',),

}
