
import os
from config.rpc_config import RPC_CONFIGURATION
from modules.filter_df import FilterDF
from modules.request_interceptor import Interceptor

RESET = '\033[0m'
YELLOW = '\033[93m'
DIR = 'extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/11.13.1_0'

def cls():
    from os import system, name
    system('cls' if name == 'nt' else 'clear')


def process_data(network_choice, filename, debugmode):
    cls()
    rpc = RPC_CONFIGURATION[network_choice]
    filter_df = FilterDF(rpc=rpc, filename=filename, debugmode=debugmode)
    input(f"{YELLOW}Press any key to filter data...{RESET}")
    filter_df.extract_web3_readcalls(debugmode=False)
    input(f"{YELLOW}Press any key to start decoding...{RESET}")
    filter_df.parse_and_decode(debugmode=False)








def main(debugmode=False):
    #//IMPORTANT arguments
    DIR = 'extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/11.13.1_0'   #Format : f"--extension_dir={DIR}"
    USER_DIR = 'user_data_dir'                                      #Format : f"--user_data_dir={USER_DIR}"
    PROXY = 'ENTER PROXY HERE'                                      #Format : f"--proxy=USERNAME:PASSWORD@IP_ADDRESS:PORT"
    interceptor = Interceptor(initial_url="https://artio.bend.berachain.com/dashboard", output_file_path_json='events.json', network_requests=True, network_responses=True, uc=True, extension_dir=DIR, user_data_dir=None, proxy=None)
    interceptor.start_browser()
    
    process_data(network_choice = 'berachain', filename = 'data/events.json', debugmode=debugmode)

if __name__ == "__main__":
    main()
