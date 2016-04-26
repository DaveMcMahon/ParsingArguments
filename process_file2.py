#!/usr/bin/env python3

import os
import sys
import logging
import argparse

logging.basicConfig(filename="output.log",  level=logging.DEBUG) 

def make_parser():
    desc = 'Command line parser'
    parser = argparse.ArgumentParser(description=desc)

    subparser = parser.add_subparsers(dest="command", help="Available commands")
    read_parser = subparser.add_parser("read", help="Reads the contents of the file")

    read_parser.add_argument("name", help="Name of the file")
    read_parser.add_argument("directory", help="Directory of the file")

    return parser
    

def check_file(file_str):
    abs_path_exists = os.path.isfile(file_str)
    
    if abs_path_exists:
        try:
            with open(file_str, "r") as fh:
                for line in fh:
                    print(line.rstrip('\n'))
        except FileNotFoundError:
            logging.debug("Issue opening/locating {!r}".format(file_str))
    else:
        print("{!r} does not exist".format(file_str))
                    
def main():
    logging.info("Main method")

    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    arguments = vars(arguments)

    command = arguments.pop("command")
    filename = arguments['name']
    directory = arguments['directory']

    if command == "read":
        abs_path = os.path.join(directory, filename)
        check_file(abs_path)
    else:
        print("Command not found")
if __name__=='__main__':
    main()
