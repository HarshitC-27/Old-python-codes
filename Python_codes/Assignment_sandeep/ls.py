# myls.py
# Import the argparse library
import argparse
# this is just used to give the list of all the files in the inputted directory
import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='Lists the contents of a folder')

# Add the arguments
my_parser.add_argument('Path',
                    metavar='path',
                    type=str,
                    help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))