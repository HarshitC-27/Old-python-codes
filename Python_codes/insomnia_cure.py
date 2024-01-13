k=input()
l=input()
m=input()
n=input()
d=input()
k=int(k)
l=int(l)
m=int(m)
n=int(n)
d=int(d)
ans=0
ans=int(ans)
for i in range(d+1):
    if((i%k==0 and i>=k and k!=0) or (i%l==0 and i>=l and l!=0) or (i%m==0 and i>=m and m!=0) or (i%n==0 and i>=n and n!=0)):
        # print(i)
        ans=ans+1
print(int(ans))




