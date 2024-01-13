t=input()
t=int(t)
for k in range(0,t):
    n,m=input().split()
    n,m=[int(n),int(m)]
    n=int(n)
    m=int(m)
    f=0
    f=int(f)
    a=[]
    for i in range(0,n):   #where n is the no. of lines you want 
        a.append(input())  # for taking m space separated integers as input
    for i in range(0,n):
        for j in range(0,m):
            if i==n-1 and a[i][j]=='D':
                f=f+1
            if j==m-1 and a[i][j]=='R':
                f=f+1
    print(f)

