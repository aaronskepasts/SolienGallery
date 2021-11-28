from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork
import urllib.request, json
import threading
from os.path import exists
from json_validity import is_json_valid
from threading import Thread

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/
MY_API_KEY_ID = "uJgPylQi1c7L8gs"
MY_API_SECRET_KEY = "stggEI2YyCHmUsj"
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)

def get_data_from_url(data_url):
    with urllib.request.urlopen(data_url) as url:
        data = json.loads(url.read().decode())
        return(data)

def create_json(address):
    validity = is_json_valid(address)
    if validity[0] == 0:
        return
    elif validity[0] != -1:
        print(validity[1])
        return
    try:
        nft_metadata = BLOCKCHAIN_API_RESOURCE.get_nft_metadata(
            mint_address=address,
            network=SolanaNetwork.MAINNET_BETA
        )
    except:
        print("Error getting nft_metadata using API for: " + address)
        return
    metadata = get_data_from_url(nft_metadata['data']['uri'])
    file_name = "soliens/" + address + ".json"
    new_json = open(file_name, "w")
    json.dump(metadata, new_json, indent=2)
    new_json.close()
    validity = is_json_valid(address)
    if validity[0] != 0:
        print(validity[1])

def main():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    with open('solien_addresses.json') as soliens_json:
        addresses = json.load(soliens_json)
    counter = 0
    for address in addresses:
        print(counter)
        if counter == 5:
            address = "test"
        counter += 1
        if counter == 10:
            break
        t = Thread(target=create_json, args = (address,))
        t.start()

if __name__ == '__main__':
    main()
