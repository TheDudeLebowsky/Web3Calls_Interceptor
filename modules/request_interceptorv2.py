from pprint import pformat
from seleniumbase import BaseCase
from seleniumbase import SB
import pandas as pd
import threading
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
BLUE = "\033[94m"
PADDING = " " * 50


#//TESTING attempt to use this class without the need for pytest use SB instead of BaseCase
#//NOT WORKING
DIR = 'extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/11.13.1_0'
class CDPTests1():
    def __init__(self):
        self.initial_url = "https://artio.bend.berachain.com/dashboard"
        self.requests_counter = 0
        self.tab_counter = 0
        self.event_data = []
        self.events_df = None
        self.output_file_path_json = 'events.json'
        self.network_requests = True
        self.network_responses = True
        self.driver = SB(uc=True, uc_cdp_events=True, extension_dir=DIR)
        self.driver = get_new_driver(undetectable=True, uc_cdp_events=True)
    def start_browser(self):
        
        with self.driver as sb:  # By default, browser="chrome" if not set.
            
            sb.open(self.initial_url)
            self.add_cdp_listener(sb)

            #initiate the tab checking thread
            self.keep_checking_tabs = True
            tab_checking_thread = threading.Thread(target=self.switch_to_latest_tab_periodically, args=(5,))
            tab_checking_thread.start()

            #Wait for user input to exit, avoid closing the browser before the test is done
            input('press enter to exit') 
            self.keep_checking_tabs = False 
            tab_checking_thread.join()  
            
            
            sb.open("https://seleniumbase.github.io/realworld/login")
            sb.type("#username", "demo_user")
            sb.type("#password", "secret_pass")
            sb.enter_mfa_code("#totpcode", "GAXG2MTEOR3DMMDG")  # 6-digit
            sb.assert_text("Welcome!", "h1")
            sb.highlight("img#image1")  # A fancier assert_element() call
            sb.click('a:contains("This Page")')  # Use :contains() on any tag
            sb.click_link("Sign out")  # Link must be "a" tag. Not "button".
            sb.assert_element('a:contains("Sign in")')
            sb.assert_exact_text("You have been signed out!", "#top_message")
    #HELPER FUNCTIONS
    def save_to_json(self):
        """Updates the JSON file with the latest event data."""
        self.events_df.to_json( self.output_file_path_json, orient='records', lines=True, date_format='iso')

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
    
    def add_cdp_listener(self, sb):

        #To print everything, use "*". Otherwise select specific headers.
        def capture_data(data, save_to_file=True):
            print(f"{BLUE}{self.current_window_title}{RESET} | Tabs opened {CYAN}{self.tab_counter}{RESET} | Intercepted request # {CYAN}{self.requests_counter}{RESET}{PADDING}", end="\r")
            self.requests_counter += 1
            self.event_data.append(data)
            self.events_df = pd.DataFrame(self.event_data)
            if save_to_file:
                self.save_to_json()
            else:
                print(pformat(data))

        #Add the CDP listeners according to the options

        if self.network_requests is True:
            sb.add_cdp_listener(
                "Network.requestWillBeSent", capture_data)
            sb.add_cdp_listener(
                "Network.requestWillBeSentExtraInfo", capture_data)

        if self.network_responses is True:
            sb.add_cdp_listener(
                "Network.responseReceived", capture_data)
            sb.add_cdp_listener(
                "Network.responseReceivedExtraInfo", capture_data)


    #//MAIN        
    def test_main(self):


        #//TODO: Add the path to the user data directory to use existing cookies and sessions
        #options = webdriver.ChromeOptions() 
        #options.add_argument("user-data-dir=PATH")

        #Initialize the driver
        #if not (self.undetectable and self.uc_cdp_events):
        #    print("Warning: The undetectable and uc_cdp_events options are required for this test.")
        #    self.get_new_driver(undetectable=True, uc_cdp_events=True)
        self.driver.open(self.initial_url)
        self.add_cdp_listener()

        #initiate the tab checking thread
        self.keep_checking_tabs = True
        tab_checking_thread = threading.Thread(target=self.switch_to_latest_tab_periodically, args=(5,))
        tab_checking_thread.start()

        #Wait for user input to exit, avoid closing the browser before the test is done
        input('press enter to exit') 
        self.keep_checking_tabs = False 
        tab_checking_thread.join()  


if __name__ == "__main__":
    interceptor = CDPTests1()
    interceptor.start_browser()
