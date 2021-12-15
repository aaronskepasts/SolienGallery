from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork
import urllib.request, json
import threading
from os.path import exists
from json_validity import is_json_valid, write_invalid_output
from threading import Thread

MY_API_KEY_ID = "hQfwhpQgJfjxi6o"
MY_API_SECRET_KEY = "yQW675BRAI5f4ci"
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)

def get_data_from_url(data_url):
    assert(data_url != None)
    with urllib.request.urlopen(data_url) as url:
        data = json.loads(url.read().decode())
        return(data)

def cache_metadata(address):

    # check if address.json exists in cache
    validity = is_json_valid(address)
    if validity[0] == 0:
        return
    elif validity[0] != -1:
        print(validity[1])
        return

    # retrieve initial metadata from Solana
    try:
        nft_metadata = BLOCKCHAIN_API_RESOURCE.get_nft_metadata(
            mint_address=address,
            network=SolanaNetwork.MAINNET_BETA
        )
    except:
        # store addresses that are broken somewhere
        error = "Error getting nft_metadata using API for: " + str(address)
        print(error)
        write_invalid_output(error)
        return

    # retrive metadata from initial metadata uri
    try:
        metadata = get_data_from_url(nft_metadata['data']['uri'])
    except:
        error = "Error reading data from nft_metadata['data']['uri'] for: " + str(address)
        print(error)
        write_invalid_output(error)
        return

    # make new json file with address metadata
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
        counter += 1
        t = Thread(target=cache_metadata, args = (address,))
        t.start()

if __name__ == '__main__':
    main()
