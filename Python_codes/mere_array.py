t=input()
t=int(t)
for k in range(0,t):
    n=input()
    n=int(n)
    a=[int(x) for x in input().split()]
    a_sort=sorted(a)
    ans="YES"
    min=a_sort[0]
    min=int(min)
    for i in range(n):
        if a[i]!=a_sort[i] and a[i]%min!=0:
            ans="NO"
            break
    print(ans)



