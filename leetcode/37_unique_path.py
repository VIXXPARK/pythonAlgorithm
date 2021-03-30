class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        top=m+n-2
        big,small=0,0
        if m-1>n-1:
            big,small=m-1,n-1
        else:
            big,small=n-1,m-1
        
        def fromTo(bottom,top):
            ans=1
            for val in range(bottom+1,top+1):
                ans*=val
            return ans
        up=fromTo(big,top)
        down=fromTo(0,small)
        return up//down