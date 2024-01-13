s1=input()
s2=input()
l1=int(len(s1))
l2=int(len(s2))
i=1
i=int(i)
temp=0
temp=int(temp)
while(l1-i>=0 and l2-i>=0):
    if(s1==s2):
        print(0)
        break
    if(s1[l1-i:l1]==s2[l2-i:l2]):
        temp=temp+1
        i=i+1
        if(l1==1 or l2==1):
            print(l1-temp+l2-temp)
            break
    else:
        print(l1-temp+l2-temp)
        break





