from seleniumbase import Driver
import sys 
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.')))
import pandas as pd
import time
import json
import threading
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
ORANGE = "\033[33m"
PADDING = " " * 50

def remove_keys(data, keys_to_remove):
    """Recursively remove specified keys from a nested dictionary."""
    if isinstance(data, dict):
        return {k: remove_keys(v, keys_to_remove) for k, v in data.items() if k not in keys_to_remove}
    elif isinstance(data, list):
        return [remove_keys(item, keys_to_remove) for item in data]
    else:
        return data


def extract_keys(data, keys_to_extract):
    """Recursively extract specified keys from a nested dictionary."""
    extracted_data = {}
    
    def recurse_items(current_data, path=""):
        if isinstance(current_data, dict):
            for key, value in current_data.items():
                new_path = f"{path}.{key}" if path else key
                if key in keys_to_extract:
                    extracted_data[new_path] = value
                if isinstance(value, (dict, list)):
                    recurse_items(value, new_path)
        elif isinstance(current_data, list):
            for index, item in enumerate(current_data):
                recurse_items(item, f"{path}[{index}]")

    recurse_items(data)
    return extracted_data




DIR = 'extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/11.13.1_0'
class Interceptor():
    def __init__(self, initial_url=None, output_file_path_json=None, network_requests=True, network_responses=True, uc=True, uc_cdp_events=True, extension_dir=DIR, user_data_dir=None, proxy=None):
        self.initial_url = "https://artio.bend.berachain.com/dashboard"
        self.requests_counter = 0
        self.tab_counter = 0
        self.event_data = []
        self.events_df = None
        self.output_file_path_json = 'events.json'
        self.network_requests =network_requests
        self.network_responses = network_responses  
        self.filtered_event_data_strings = set() 
        self.keys_to_ignore = ['requestId', 'timestamp', 'requestid', 'initiator', 'priority','headers','connectTiming', 'responseTime', 'date', 'etag', 'logId', 'signatureData', 'validFrom', 'validTo', 'expires', 'sendEnd', 'sendStart', 'timing']
        self.keys_to_focus = ['params']
        self.driver = Driver(uc=True, uc_cdp_events=True, extension_dir=DIR, user_data_dir=None, proxy=None)

    def start_browser(self):
        
        with self.driver as sb: 
            
            sb.open(self.initial_url)
            self.add_cdp_listener(sb)

            self.keep_checking_tabs = True
            self.tab_checking_thread = threading.Thread(target=self.switch_to_latest_tab_periodically, args=(2,))
            self.tab_checking_thread.start()
            
            #Loop prevent the main thread from exiting
            while self.keep_checking_tabs is True:
                time.sleep(1)
            
            self.tab_checking_thread.join()
            return

    #HELPER FUNCTIONS
    def save_to_json(self):
        """Updates the JSON file with the latest event data."""
        self.events_df.to_json( self.output_file_path_json, orient='records', lines=True, date_format='iso')

    def switch_to_latest_tab_periodically(self, interval=2):
        """
        Periodically checks for new tabs and switches to the latest one.
        :param interval: Time in seconds between checks.
        """
        while self.keep_checking_tabs:
            try:
                current_handles = self.driver.window_handles
                self.tab_counter = len(current_handles)
                self.current_window_handle = self.driver.current_window_handle
                self.current_window_title = self.driver.title

                # Check if there are multiple tabs and if the latest tab is not the current one
                if current_handles and self.tab_counter > 1 and current_handles[-1] != self.current_window_handle:
                    self.driver.switch_to.window(current_handles[-1])
                    self.current_window_handle = self.driver.current_window_handle
                    self.tab_counter = len(current_handles)
                    print("Switched to new tab:", self.driver.title)
                    self.current_window_title = self.driver.title
            except Exception as e:
                if "target window already closed" in str(e):
                    current_handles = self.driver.window_handles
                    if current_handles:
                        # Switch to the first tab if the current tab is closed
                        self.driver.switch_to.window(current_handles[0])
                        print(f"{ORANGE}Switched to the first available tab after closure: {self.driver.title}{RESET}")

                elif 'disconnected: not connected to DevTools' in str(e):
                    print(f"{RED}DevTools disconnected. Stoping the cdb listener.{RESET}")
                    self.keep_checking_tabs = False
                    if self.driver:
                        self.driver.quit()
                        return

            time.sleep(interval)
    
    def add_cdp_listener(self, sb):

        def capture_data(data, save_to_file=True):

            filtered_data = remove_keys(data, self.keys_to_ignore) #remove keys that prevent comparison such as unique id or timestamps(Use with focused_data to remove a key from a nested dict that could prevent comparison.)
            focused_data = extract_keys(filtered_data, self.keys_to_focus) #Uses specified keys to focus on specific data for comparison. if focused data is different, save it.
            if focused_data:
                focused_data_string = json.dumps(focused_data, sort_keys=True)
                if focused_data_string not in self.filtered_event_data_strings:
                    print(f"{BLUE}{self.current_window_title}{RESET} | Tabs opened {CYAN}{self.tab_counter}{RESET} | Intercepted request # {CYAN}{self.requests_counter}{RESET}{PADDING}")
                    self.event_data.append(data) 
                    self.filtered_event_data_strings.add(focused_data_string) 
                    self.requests_counter += 1
                else:
                    print(f"{YELLOW}Duplicate request --> ignored{RESET}")
            else:
                self.event_data.append(data)  
                self.requests_counter += 1

            self.events_df = pd.DataFrame(self.event_data)
            if save_to_file:
                self.save_to_json()


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





if __name__ == "__main__":
    interceptor = Interceptor(initial_url="https://artio.bend.berachain.com/dashboard", output_file_path_json='events.json', network_requests=True, network_responses=True)
    interceptor.start_browser()
