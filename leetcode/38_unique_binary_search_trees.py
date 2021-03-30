class Solution:
    def numTrees(self, n: int) -> int:
        lst=[1,1,2,5,14,42,132]
        if n>=7:
            for i in range(7,n+1):
                left,mid,top=0,1,i-1
                ans=0
                while left<=i-1:
                    ans+=lst[top]*lst[left]
                    left+=1
                    top-=1
                lst.append(ans)
        return lst[n]
s=Solution()
print(s.numTrees(7))