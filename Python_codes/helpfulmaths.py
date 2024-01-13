str=input()
l=len(str)
l=int(l)
t=0
t=int(t)
for i in range(l):
    i=int(i)
    if str[i]=='1':
        if(t==0):
            print('1',sep='',end='')
            t=t+1
        else:
            print('+1',sep='',end='')
            t=t+1
for i in range(l):
    i=int(i)
    if str[i]=='2':
        if(t==0):
            print('2',sep='',end='')
            t=t+1
        else:
            print('+2',sep='',end='')
            t=t+1
for i in range(l):
    i=int(i)
    if str[i]=='3':
        if(t==0):
            print('3',sep='',end='')
            t=t+1
        else:
            print('+3',sep='',end='')



