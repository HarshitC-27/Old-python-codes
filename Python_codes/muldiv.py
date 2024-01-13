t=input()
t=int(t)
for i in range(t):
    cnt2=0
    cnt3=0
    cnt2=int(cnt2)
    cnt3=int(cnt3)
    x=input()
    x=int(x)
    while(x%2==0):
        cnt2=cnt2+1
        x=x/2
    while(x%3==0):
        cnt3=cnt3+1
        x=x/3
    if(cnt2>cnt3 or x!=1):
        print(-1)
    else:
        print(2*cnt3-cnt2)