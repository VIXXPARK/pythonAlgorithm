nums=[0,1,0,3,12]
zeros=0
for i,v in enumerate(nums):
    if v!=0:
        nums[i],nums[zeros]=nums[zeros],nums[i]
        zeros+=1