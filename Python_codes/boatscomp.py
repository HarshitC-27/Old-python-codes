from collections import*
for s in[*open(0)][2::2]:
    c=Counter(map(int,s.split()));r=[0]*101
    for x in c:
        for y in c:r[x+y]+=min(c[x],c[y])
    print(max(r)//2)