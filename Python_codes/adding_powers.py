t=input()
t=int(t)
ans="YES"
for i in range(0,t):
    ans="YES"
    n,k=input().split()
    n=int(n)
    k=int(k)
    a=[int(x) for x in input().split()]
    a_sort=sorted(a)
    max=int(a_sort[n-1])
    p=0
    p=int(p)
    while k**p<=int(1e16):
        p=p+1
    while(p>=0):
        val=k**p
        p=p-1
        val=int(val)
        freq=0
        freq=int(freq)
        for j in range(0,n):
            if a[j]>=val:
                freq=freq+1
        if freq>=2:
            ans="NO"
            break
    print(ans)
