n=int(input())
d=0
while n!=0:
    n=n//10
    d+=1
if d==1: print('One digit number')
elif d==2: print('Two digit number')
elif d==3: print('Three digit number')
elif d>3: print('More than three digit number')