import re
import sys
f=0
# just opening the file file and using the for loo pto traverse through the file and print the line in whch we get the specified and desired value
with open(sys.argv[2],"r") as file:
    for line in file:
        if re.search(sys.argv[1], line):
            f=1
            print(line)
if f==0:
    # this is implemented when the specified thing is not found anywhere in the file
    print('Not found in this file')