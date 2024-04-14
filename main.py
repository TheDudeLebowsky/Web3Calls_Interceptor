
import os
from config.rpc_config import RPC_CONFIGURATION
from modules.filter_df import FilterDF


DIR = 'extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/11.13.1_0' #//IMPORTANT Path to the extension directory
USER_DIR = 'user_data_dir'
def cls():
    from os import system, name
    system('cls' if name == 'nt' else 'clear')


def intercept_requests():
    from pytest import main
    #, f"--user_data_dir={USER_DIR}"
    main(["modules/request_interceptor.py", "--uc", "--uc-cdp", "-s", f"--extension_dir={DIR}", f"--user_data_dir={USER_DIR}"])

def process_data(network_choice, filename, debugmode):
    cls()
    
    rpc = RPC_CONFIGURATION[network_choice]
    filter_df = FilterDF(rpc=rpc, filename=filename, debugmode=debugmode)
    filter_df.extract_web3_readcalls(debugmode=False)
    filter_df.parse_and_decode(debugmode=False)


def main(debugmode=False):
    intercept_requests()
    process_data(network_choice = 'berachain', filename = 'events.json', debugmode=debugmode)

if __name__ == "__main__":
    main()
