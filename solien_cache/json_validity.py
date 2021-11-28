"""
Return codes:
-1 - json doesn't exist
0 - valid json exists
1 - invalid data
2 - too many keys
3 - invalid file
"""

from os.path import exists
import json

def is_json_valid(address):
    # check if json exists
    if not exists("soliens/" + address + ".json"):
        return (-1, "file doesn't exist at: " + address)
    ## check file is valid
    try:
        with open("soliens/" + address + '.json') as json_file:
            json_dict = json.load(json_file)
        # check no data is none in json
        for key in json_dict:
            if (json_dict[key]) is None:
                return (1, "invalid data at: " + address)
        # check correct num of keys
        if len(json_dict) != 7:
            return (2, "incorrect number of keys at : " + address)
    except:
        return (3, "invalid file at: " + address)

    return (0, "valid json exists at: " + address)

def main():
    with open('solien_addresses.json') as soliens_json:
        addresses = json.load(soliens_json)
    counter = 0
    for address in addresses:
        validity = is_json_valid(address)
        if counter == 10:
            break
        if validity[0] != 0:
            print(validity[1])
        counter += 1


if __name__ == '__main__':
    main()
