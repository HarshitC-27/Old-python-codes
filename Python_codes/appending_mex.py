n=input()
n=int(n)
t=0
t=int(t)
a=[int(x) for x in input().split()]
if a[0]!=0:
    print(1)
else:
    t=1
    for i in range(1,n):
        f=0
        for j in range(0,i):
            if(a[i]==a[j] or a[i]==a[j]+1):
                f=1
                break
        if f==1:
            t=t+1
            continue
        if a[i]<=a[i-1]+1:
            t=t+1
            continue
        else:
            print(int(i)+1)
            break
if(t==n):
    print(-1)





