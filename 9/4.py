#task4
nums=input('nums = ' ).split(',') #we will get our numbers
res=0 # then create res value to keep result 

for i in range(len(nums)):
    check=True # we will in our list
    for j in range(len(nums)):
        if i!=j:
            if nums[i]==nums[j]: check=False   #check number is unique or not
    if check==True: res+=int(nums[i]) # if number is unique count sum of unique numbers
print(res) #printing result