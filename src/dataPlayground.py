import requests

from constants import apiKey, merchantID
apiURL = 'https://apisandbox.dev.clover.com'

def main():
    print("Starting...")
    url = f"https://api.clover.com/v3/merchants/{merchantID}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    print(response.text)
    
    
    





if(__name__ == "__main__"):
    main()