from os.path import exists
import json
import time

"""
Return codes:
(-1, json doesn't exist)
(0, valid json exists)
(1, invalid data)
(2, incorrect number of key)
(3, invalid file)
"""

def write_invalid_output(error):
    assert(error != None)
    out_file_name = "invalid" + str(time.strftime("%Y-%m-%d")) + ".txt"
    with open(out_file_name, 'a') as out_file:
        out_file.write(error + '\n')
        out_file.close()

def is_json_valid(address):

    # check if json exists
    if not exists("soliens/" + address + ".json"):
        error = "file doesn't exist at: " + str(address)
        write_invalid_output(error, address)
        return (-1, error)

    # check file is valid
    try:
        with open("soliens/" + address + '.json') as json_file:
            json_dict = json.load(json_file)

        # check data is not none in json
        for key in json_dict:
            if (json_dict[key]) is None:
                error = "invalid data at: " + str(address)
                write_invalid_output(error)
                return (1, error)

        # check correct num of keys
        if len(json_dict) != 7:
            error = "incorrect number of keys at: " + str(address)
            write_invalid_output(error)
            return (2, error)

    # file is invalid
    except:
        error = "invalid file at: " + str(address)
        write_invalid_output(error)
        return (3, error)

    # file valid
    return (0, "valid json exists at: " + str(address))

def main():
    with open('solien_addresses.json') as soliens_json:
        addresses = json.load(soliens_json)
    counter = 0
    for address in addresses:
        validity = is_json_valid(address)
        if validity[0] != 0:
            print(validity[1])
        counter += 1
        if counter == len(addresses):
            print(counter)


if __name__ == '__main__':
    main()
