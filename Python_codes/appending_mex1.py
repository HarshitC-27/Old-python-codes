n=input()
n=int(n)
t=0
t=int(t)
a=[int(x) for x in input().split()]
m=-1
m=int(m)
for i in range(0,n):
    if a[i]<=m+1:
        if a[i]>=m:
            m=a[i]
        t=t+1
        continue
    else:
        if a[i]>=m:
            m=a[i]
        print(i+1)
        break
if(t==n):
    print(-1)



