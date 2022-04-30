#!/usr/bin/env python3

from argparse import ArgumentParser
from sys import exit, path, stderr

from server import app

#-----------------------------------------------------------------------

# Runs the NFT gallery application at the specified server.
# Sample execution:
#    python runserver.py 9000
def main():
    try:
        # Retrieve the command-line arguments.
        parser = ArgumentParser(allow_abbrev=False, 
                                description="Gallery application")
        parser.add_argument("p", metavar="port", type=int,
                            help="port where the server should listen")
        args = parser.parse_args()

        # Run the server on the given port.
        app.run(host="0.0.0.0", port=args.p, debug=True)

    except Exception as ex:
        print(ex, file=stderr)
        exit(1) 

#-----------------------------------------------------------------------

if __name__ == "__main__":
    main()
