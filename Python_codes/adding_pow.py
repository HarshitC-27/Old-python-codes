t=input()
t=int(t)
for i in range(0,t):
	n,k=map(int,input().split())
	a=list(map(int,input().split()))
	kbits=[0]*55
	for x in a:
		t=x
		i=0
		while(t):
			kbits[i]+=t%k
			t=t//k
			i+=1
	m=max(kbits)
	if m>1:
		print("NO")
	else:
		print("YES")
