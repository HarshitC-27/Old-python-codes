import numpy as np
import random
n=input("Enter size of square matrix")
n=int(n)

array1=[[random.random() for i in range(n)] for j in range(n)]
array2=[[random.random() for i in range(n)] for j in range(n)]

print("First array")
for e in array1:
    print(e)
print("Second array")
for e in array2:
    print(e)

productmat=np.zeros((n,n))
for i in range(len(array1)):
    #iterate through columns of array1
    for j in range(len(array2[0])):
        # iterate through rows of array2
        for k in range(len(array2)):
           productmat[i][j] += array1[i][k] * array2[k][j]
print("Their product")
for r in productmat:
    print(r)

#!addition part
summat=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        summat[i][j]=array1[i][j] + array2[i][j]
print("Their sum")
for r in summat:
    print(r)

#!inverse part

