import requests
from json.decoder import JSONDecodeError

#//complete
class get4Bytes:
    def __init__(self):
        self.base_url = "https://www.4byte.directory"
        self.endpoint_signatures = f"{self.base_url}/api/v1/signatures/"
        self.endpoint_event_signatures = f"{self.base_url}/api/v1/event-signatures/"
            
    def get_functionSignature_from_methodID(self, method_id, debugmode=False):
        """Fetches the text signature of a given method ID from 4byte.directory."""
        endpoint = self.endpoint_signatures
        params = {
            'hex_signature': method_id,
            'format': 'json' 
        }

        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            try:
                data = response.json()
                if data['count'] > 0 and 'results' in data and len(data['results']) > 0:
                    function_signature = data['results'][0]['text_signature']
                    if debugmode:
                        print(f"Method ID: {method_id} | Signature: {function_signature}")
                    return function_signature
            except JSONDecodeError as e:
                print(f"Failed to decode JSON response. Error: {str(e)}")
            except ValueError as e:
                print(f"Failed to parse JSON response. Error: {str(e)}")
            except Exception as e:
                print(f"Failed to fetch data. Error: {str(e)}")

        else:
            raise Exception(f"Failed to fetch data, status code: {response.status_code}")

    import requests

    def search_functionSignature(self,signature, debugmode=False):
        """
        Search for function signatures in the Ethereum Signature Database.
        """
        endpoint = self.endpoint_signatures
        params = {
            'text_signature': signature,
            'format': 'json' 
        }
        try:
            response = requests.get(endpoint, params=params)
        except JSONDecodeError as e:
            print(f"Failed to decode JSON response. Error: {str(e)}")
        except ValueError as e:
            print(f"Failed to parse JSON response. Error: {str(e)}")
        except Exception as e:
            print(f"Failed to fetch data. Error: {str(e)}")
        if response.status_code == 200:
            response = response.json()
            methodID = response['results'][0]['hex_signature']
            if debugmode:
                print(f"Response : {response}")

            return response
        else:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
            

    def search_eventSignature(self, event_signature):
        """
        Search for event signatures in the Ethereum Signature Database.
        """
        endpoint = self.endpoint_event_signatures
        params = {
            'text_signature': event_signature,
            'format': 'json'
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            response = response.json()
            
            return response
        else:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def main():
    signature = "aggregate3((address,bool,bytes)[])"
    event="RequestCreated(address,address,int256,uint256[12])"
    method_id = "0x82ad56cb"
    get4bytes = get4Bytes()
    print(get4bytes.get_functionSignature_from_methodID(method_id))
    print(get4bytes.search_functionSignature(signature))
    print(get4bytes.search_eventSignature(event))


if __name__ == "__main__":
    main()
