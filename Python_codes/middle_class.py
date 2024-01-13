T=input()
T=int(T)
for i in range(T):
    n,x=[int(x) for x in input().split()]
    a=[int(a) for a in input().split()]
    a.sort()
    j=n-1
    s=0
    t=0
    ans=0
    while(j>=0):
        s+=a[j]
        t=t+1
        if(s>=t*x):
            ans=ans+1
            if t==n:
                print(ans)
        else:
            print(ans)
            break
        j=j-1
    i=i+1


