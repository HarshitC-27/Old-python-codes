n=input()
n=int(n)
s=input()
l=len(s)
l=int(l)
nA=0
nI=0
nA=int(nA)
nI=int(nI)
for i in range(l):
    c=s[i]
    if(c=='A'):
        nA=nA+1
    if(c=='I'):
        nI=nI+1
if(nI==0):
    print(nA)
elif(nI==1):
    print(1)
else:
    print(0)

