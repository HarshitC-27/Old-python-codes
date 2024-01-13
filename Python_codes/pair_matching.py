from collections import Counter

count1 = Counter()
count2 = Counter()
i=input()
for t in range(0,int(i)):
    s = input()
    p = 0
    q = 0
    for c in s:
        if c == "(":
            p += 1
        else:
            p -= 1
            q = min(q, p)
    if p == q:
        count1[-p] += 1
    elif q == 0:
        count2[p] += 1
print(sum((min(count1[k], count2[k]) for k in count1.keys())) + count1[0] // 2)