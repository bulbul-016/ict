nums=input().split()
first=0
second=0
result1=''
result2=''

for i in range(3):
    nums[i]=int(nums[i])
    first+=nums[i]
if nums[0]==nums[1] and nums[0]==nums[2]:
    result1+=str(first*3)
else: result1+= str(first)

for i in range(4,7):
    nums[i]=int(nums[i])
    second+=nums[i]
if nums[4]==nums[5] and nums[4]==nums[6]:
    result2+=str(second*3)
else: result2+= str(second)

print(result1+' or '+result2)
