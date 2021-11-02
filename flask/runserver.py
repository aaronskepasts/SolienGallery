from argparse import ArgumentParser
from sys import exit, path, stderr

from server import app

#-----------------------------------------------------------------------

def main():
    try:
        # Retrieve the command-line arguments.
        desc = "Gallery application"
        parser = ArgumentParser(allow_abbrev=False, description=desc)
        help_str = "the port at which the server should listen"
        parser.add_argument("p", metavar="port", help=help_str, type=int)
        args = parser.parse_args()

        # Run the server on the given port.
        app.run(host="0.0.0.0", port=args.p, debug=True)

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

if __name__ == "__main__":
    main()
