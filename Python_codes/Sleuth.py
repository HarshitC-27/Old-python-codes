question=input()
# cha=question[len(question)-2]
# if(cha=='a' or cha=='A' or cha=='e' or cha=='E' or cha=='i' or cha=='I' or cha=='o' or cha=='O' or cha=='u' or cha=='U' or cha=='y' or cha=='Y'):
#     print("YES")
# else:
#     print("NO")
l=len(question)
l=int(l)
i=l-1
i=int(i)
while(i>=0):
    cha=question[i]
    if(cha!=' ' and cha!='?'):
        if(cha=='a' or cha=='A' or cha=='e' or cha=='E' or cha=='i' or cha=='I' or cha=='o' or cha=='O' or cha=='u' or cha=='U' or cha=='y' or cha=='Y'):
            print("YES")
            break
        else:
            print("NO")
            break
    else:
        i=i-1

