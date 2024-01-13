for t in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	odds=[i for i in range(n*2) if arr[i]&1]
	evens=[i for i in range(n*2) if not arr[i]&1]
	ct=0
	while ct<n-1:
		if len(odds) > 1:
			print(odds.pop()+1,odds.pop()+1)
		elif len(evens) > 1:
			print(evens.pop()+1,evens.pop()+1)
		ct+=1
