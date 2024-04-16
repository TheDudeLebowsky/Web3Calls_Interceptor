from pprint import pformat
from seleniumbase import BaseCase
from seleniumbase import SB
import pandas as pd
import threading
import os
import json


RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PADDING = " " * 50


#TODO: Pretty much working, could need some more testing and add user data directory option. Small issue when closing tabs
#TODO Need to find how to replace the use of BaseCase to SB

def cls():
    if os.name == 'nt':
        os.system('cls')




class CDPTests(BaseCase):
    def setUp(self):

        
        super(CDPTests, self).setUp()
        self.initial_url = "https://rinkeby.orbiter.finance/?source=Berachain%20Artio&dest=Sepolia&token=BERA"
        self.requests_counter = 0
        self.tab_counter = 0
        self.event_data = []
        self.events_df = None
        self.output_file_path_json = 'events.json'
        self.network_requests = True
        self.network_responses = True
        if not os.path.exists(self.output_file_path_json):
            self.write_mode = 'w'
        else:
            print(f"{YELLOW}File already exists. Will be appending to file{RESET}")
            self.write_mode = 'a'
    #HELPER FUNCTIONS
    def save_to_json(self):
        #//TODO: Handle large files and do not save duplicates

        self.events_df.to_json( self.output_file_path_json, orient='records', lines=True, date_format='iso', mode=self.write_mode)



    def switch_to_latest_tab_periodically(self, interval=5):
        """
        Periodically checks for new tabs and switches to the latest one.
        :param interval: Time in seconds between checks.
        """
        while self.keep_checking_tabs:
            try:
                window_handles = self.driver.window_handles
                self.tab_counter = len(window_handles)
                self.current_window_title = self.get_title() 
                
                if window_handles:
                    self.driver.switch_to.window(window_handles[-1])
            except Exception as e:
                print(f"Error switching to the latest tab: {e}")
            self.sleep(interval)
    
    def add_cdp_listener(self):

        #To print everything, use "*". Otherwise select specific headers.
        def capture_datav1(data, save_to_file=True):
            print(f"{BLUE}{self.current_window_title}{RESET} | Tabs opened {CYAN}{self.tab_counter}{RESET} | Intercepted request # {CYAN}{self.requests_counter}{RESET}{PADDING}")
            self.requests_counter += 1
            if data not in self.event_data:
                self.event_data.append(data)
            else:
                print(f"{RED}Duplicate request{RESET}")
            self.events_df = pd.DataFrame(self.event_data)
            if save_to_file:
                self.save_to_json()
            else:
                print(pformat(data))
        def capture_data(data, save_to_file=True):
            data_string = json.dumps(data, sort_keys=True)
            if data_string not in [json.dumps(d, sort_keys=True) for d in self.event_data]:
                print(f"{BLUE}{self.current_window_title}{RESET} | Tabs opened {CYAN}{self.tab_counter}{RESET} | Intercepted request # {CYAN}{self.requests_counter}{RESET}{PADDING}", end="\r")
                self.event_data.append(data)
                self.requests_counter += 1
                self.events_df = pd.DataFrame(self.event_data)
                if save_to_file:
                    self.save_to_json()
            else:
                print(f"{RED}Duplicate request{RESET}")
        #Add the CDP listeners according to the options
        if self.network_requests is True:
            self.driver.add_cdp_listener(
                "Network.requestWillBeSent", capture_data)
            self.driver.add_cdp_listener(
                "Network.requestWillBeSentExtraInfo", capture_data)

        if self.network_responses is True:
            self.driver.add_cdp_listener(
                "Network.responseReceived", capture_data)
            self.driver.add_cdp_listener(
                "Network.responseReceivedExtraInfo", capture_data)


    #//MAIN        
    def test_main(self):


        #//TODO: Add the path to the user data directory to use existing cookies and sessions
        #options = webdriver.ChromeOptions() 
        #options.add_argument("user-data-dir=PATH")

        #Initialize the driver
        if not (self.undetectable and self.uc_cdp_events):
            print("Warning: The undetectable and uc_cdp_events options are required for this test.")
            self.get_new_driver(undetectable=True, uc_cdp_events=True)
        self.open(self.initial_url)
        self.add_cdp_listener()

        #initiate the tab checking thread
        self.keep_checking_tabs = True
        tab_checking_thread = threading.Thread(target=self.switch_to_latest_tab_periodically, args=(5,))
        tab_checking_thread.start()

        #Wait for user input to exit, avoid closing the browser before the test is done
        cls()
        input(f'{YELLOW}Press any key to exit') 
        self.keep_checking_tabs = False 
        tab_checking_thread.join()  

        #if browser is closed:
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    #interceptor = CDPTests()
    #interceptor.start_browser()
    #interceptor.test_main()
    
    from pytest import main





    #//MAIN FUNCTION

    USER_DIR = 'user_data_dir' #f"--user_data_dir={USER_DIR}"
    #PROXY = 'ENTER PROXY HERE'      #Format : --proxy=USERNAME:PASSWORD@IP_ADDRESS:PORT
    DIR = 'extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/11.13.1_0' # Metamask Format : --extension-dir="dir1,dir2"
    DIR1 = 'extensions/jifpbeccnghkjeaalbbjmodiffmgedin/1.7.0_0' # Chrome extension source viewer

    main([__file__, "--uc", "--uc-cdp", "-s", f"--extension_dir={DIR}"])
