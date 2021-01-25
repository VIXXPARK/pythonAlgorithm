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

        
#####
def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        checker = {}
        for i, v in enumerate(nums):
            if target - v in checker:
                return [checker[target - v], i]
            else:    
                checker[v] = i
        return []        