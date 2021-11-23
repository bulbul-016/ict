#task2
numbers = [int(i) for i in input().split(',')] #we will get our numbers
a = []
for i in numbers: # we will in our list
    cnt=0 # then create counter
    for j in numbers:
        if i == j:
            continue
        if i > j:
            cnt+=1
    a.append(cnt)
print(a) #printing result