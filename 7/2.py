y=int(input())
if y%4==0:
    if y%100==0:
        if y%400==0:
            print(str(y)+' is a leap year.')
        else: print(str(y)+ ' is not a leap year')
    else: print(str(y)+ ' is not a leap year')
else: print(str(y)+ ' is not a leap year')