n,c=input().split()
n,c=[int(n),int(c)]
x = [int(x) for x in input().split()]
a=x[0]
curr=1
for i in range(n-1):
    b=x[i+1]
    if(b-a<=c):
        curr=curr+1
    else:
        curr=1
    a=b
    i=i+1
print(curr)




