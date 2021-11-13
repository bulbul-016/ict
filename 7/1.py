p=input('size = ')
y=input('add_pepperoni = ')
c=input('extra_cheese = ')
result=0
if p=='S':
    result=15
    if y=='Y': result+=2 
    if c=='Y': result+=1
elif p=='M':
    result=20
    if y=='Y': result+=3
    if c=='Y': result+=1
else:
    result=25
    if y=='Y': result+=3
    if c=='Y': result+=1
print('Your final bill is: $'+str(result)+'.')