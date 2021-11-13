n=int(input('Enter number: '))
sum=0
for i in range(1,n+1):
    sum+=i
print('Sum of first '+str(n)+' numbers is: '+str(sum))
print('Average of '+str(n)+'numbers is: '+str(sum/n))

#first of all we will enter our number then with for loop go on from 1 to n and calculate sum
#then we divide sum to n and we will get average