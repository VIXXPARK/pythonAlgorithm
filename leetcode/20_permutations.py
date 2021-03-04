class Solution:
    def permute(self,nums:list):
        if nums==[]:
            return []
        n=len(nums)
        List = []
        temp=[0]*n

        def permute_recursive(nums,index,n):
            if index==n:
                List.append(temp[:])
                return
            for i in range(len(nums)):
                temp[index]=nums[i]
                permute_recursive(nums[:i]+nums[i+1:],index+1,n)
        
        permute_recursive(nums,0,n)
        return List