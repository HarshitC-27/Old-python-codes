n,sx,sy=input().split()
n=int(n)
sx=int(sx)
sy=int(sy)
st_tent=0
st_max=-1
st_tent=int(st_tent)
st_max=int(st_max)
xfinal=0
yfinal=0
xfinal=int(xfinal)
yfinal=int(yfinal)
a=[]
for i in range(0,n):
    a.append(input().split())
    # print(a[0][0])
# for i in range(0,n):
xmin=1e9
ymin=1e9
xmax=-1
ymax=-1
xmin=int(xmin)
xmax=int(xmax)
ymin=int(ymin)
ymax=int(ymax)
for i in range(0,n):#finding xmin and xmax etc.
    xt=int(a[i][0])
    yt=int(a[i][1])
    if xt>xmax:
        xmax=xt
    if xt<xmin:
        xmin=xt
    if yt>ymax:
        ymax=yt
    if yt<ymin:
        ymin=yt
# for x in range(xmin,xmax+1):#fixing a place for tent
    x=xmax
    x=int(x)
    while x>=xmin:
        y=ymax
        y=int(y)
        # for y in range(ymin,ymax+1):
        while y>=ymin:
            st_tent=0
            for i in range(0,n):#finding a student
                xi=a[i][0]
                yi=a[i][1]
                xi=int(xi)
                yi=int(yi)
                if((xi<=x and x<=sx)or(xi>=x and x>=sx)) and ((yi<=y and y<=sy)or(yi>=y and y>=sy)):
                    st_tent=st_tent+1
                    print(str(xi)+" "+str(yi))
            
        # print("this is st_tent"+str(st_tent)+"for"+str(x)+","+str(y))
            if(st_tent>=st_max and (x!=sx or y!=sy)):
                st_max=st_tent
                xfinal=x
                yfinal=y
            y=y-1
        x=x-1
print(st_max)
print(str(xfinal)+" "+str(yfinal))