s,t=input(),input()
i,j=len(s),len(t)
while i*j*(s[i-1]==t[j-1]):
    i-=1;j-=1
print(i+j)