class Solution:
    def threeSum(self, nums):
        dic={}
        ans=set()
        for val in nums:
            if dic.get(val,0)==0:
                dic[val]=1
            else:
                dic[val]+=1
        lst=list(dic.keys())
        for i in range(len(lst)):
            for j in range(i,len(lst)):
                k=-1*(lst[i]+lst[j])
                if k in dic:
                    if i==j:
                        if dic[lst[i]]>=2:
                            if k==lst[i] and dic[k]<=2:
                                continue
                            else:
                                ans.add(tuple(sorted([lst[i],lst[j],k])))
                    else:
                        if k==lst[i] or k==lst[j] and dic[k]<2:
                            continue
                        else:
                            ans.add(tuple(sorted([lst[i],lst[j],k])))
        ans=list(map(list,ans))
        return ans

##################################################################################
def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res