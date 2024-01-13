import sys
import os.path
from os.path import exixts

def show_usage(arg: 'filename'):
    print("how to use this program")
    print(f'python {filename} inputfile')

mode = 'r'
size = 64*1024

if len(sys.argv) == 1:
    show_usage(sys.argv[0])
filename=sys.argv[1]
if exixts(filename) == True:
    with open(filename, mode) as f:
        chunk = f.read(size)
        while len(chunk)>0:
            print(chunk, end = ' ')
            chunk = f.read(size)
else:
    print(f'{sys.argv[0]}: {filename}: The system cannot find the file specified.')