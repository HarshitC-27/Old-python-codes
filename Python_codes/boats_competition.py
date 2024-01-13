t=input()
t=int(t)
ci=0
cj=0
ci=int(ci)
cj=int(cj)
ans_max=0
ans_max=int(ans_max)
ans_s=0
ans_s=int(ans_s) 
for k in range(0,t):#loop for test case
    n=input()
    n=int(n)#number of values
    a=[int(x) for x in input().split()]
    ans_max=0
    for s in range(2,2*n+1):
        ans_s=0
        s=int(s)
        for i in range(1,int((s+1)/2)):
            if s-i>n:
                continue
            i=int(i)
            j=int(s-i)
            ci=0
            cj=0
            for l in range(0,n):
                if a[l]==i:
                    ci=ci+1
                if a[l]==j:
                    cj=cj+1
            if i==j and ci==cj and ci==1:
                ans_s=ans_s+0
            else:
                ans_s=ans_s+min(ci,cj)
        if s%2==0:
            cs2=0
            cs2=int(cs2)
            for l in range(0,n):
                if a[l]==s/2:
                    cs2=cs2+1
            ans_s=ans_s+int(cs2/2)
        # print("ans s is"+str(ans_s)+"for s="+str(s))#added
        if ans_s>ans_max:#to store maximum answer
            ans_max=ans_s
    print(int(ans_max))