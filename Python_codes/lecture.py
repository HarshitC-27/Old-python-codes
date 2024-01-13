n,m=input().split()
n,m=[int(n),int(m)]
x=[]
for i in range(0,m):
    x.append(input())
y=[str(y) for y in input().split()]
for i in range(0,n):
    s1=y[i]
    for j in range(0,m):
        s,s2=x[j].split()
        if s==s1:
            if len(s2)<len(s1):
                print(s2,end=' ')
            else:
                print(s1,end=' ')
            break
        

