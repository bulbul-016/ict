#task3
nums=input('nums = ' ).split(',') #we will get our numbers
res=0 # then create result number
for i in range(len(nums)): # we will go in our list
    for j in range(len(nums)):
        if i>j:
            if nums[i]==nums[j]: res=nums[i] #check numbers are repeated or not
print(res) #printing result