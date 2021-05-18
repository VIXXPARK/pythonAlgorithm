def canJump(nums):
    goal = len(nums) - 1
    for i in range(len(nums))[::-1]:
        if i + nums[i] >= goal:
            goal = i
    return not goal

print(canJump([2,3,1,1,4]))