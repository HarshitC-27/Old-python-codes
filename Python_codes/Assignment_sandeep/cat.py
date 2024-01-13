import sys
import os.path
from os.path import exixts
# just opening and reading file in chunks and then printing all the values present in that file 
def show_usage(arg: 'filename'):
    print("how to use this program")
    print(f'python {filename} inputfile')
# the mode will be read as there can be no other thing that we can do while we use the cat command to read a file
mode = 'r'
size = 64*1024

if len(sys.argv) == 1:
    show_usage(sys.argv[0])
filename=sys.argv[1]
# read the file only when it exixts
if exixts(filename) == True:
    with open(filename, mode) as f:
        # read the file in chunks to increase speed
        chunk = f.read(size)
        while len(chunk)>0:
            print(chunk, end = ' ')
            chunk = f.read(size)
else:
    # print the error message if the file does ort exist
    print(f'{sys.argv[0]}: {filename}: The system cannot find the file specified.')