import collections
nums = [3,3]
length=len(nums)
target = 6
dic=collections.Counter(nums)
for val in range(length):
    if dic.get(target-nums[val]) is not None:
        keys=nums[val]
        if keys==target-keys:
            if dic.get(keys)==2:
                nums.remove(keys)
                output=[val,nums.index(keys)+1]
                break
        else:
            output=[val,nums.index(target-nums[val])]
            break
print(output)

#######################

def twoSum2(nums: list, target: int) -> list:
    for i in range(len(nums)-1):
        try:
            return [i, nums[i+1:].index(target - nums[i])+i+1]
        except:
            pass
print(twoSum2([2,7,11,12],9))

##########################
def twoSum3(nums, target):
         h = {}
         for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]