a=int(input())
b=int(input())
n=int(input())

if (b*n)>=100:
    print(str(((b*n)//100)+(a*n)) + " "+str((b*n)%100))
else: print(str(a*n)+ " "+ str(b*n))

'''1 dollar=100 cents
then b is cents if b*n bigger than 100 then we make 
doolar from cents by dividing 100'''