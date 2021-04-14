class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0,1,2,3,1,2,3,4,2,1]
        for i in range(10,n+1):
            if (i**0.5)==int((i**0.5)):
                dp.append(1)
            else:
                x=i
                j=1
                while j*j<i:
                    x=min(x,dp[j*j]+dp[i-j*j])
                    j+=1
                dp.append(x)
        return dp[n]

##################################################
def numSquares(n):
	dp = [0] + [float('inf')]*n
	for i in range(1, n+1):
		dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
	return dp[n]
###################################################

def numSquares2(n):
	squares = [i**2 for i in range(1, int(n**0.5)+1)]
	d, q, nq = 1, {n}, set()
	while q:
		for node in q:
			for square in squares:
				if node == square: return d
				if node < square: break
				nq.add(node-square)
		d,q, nq = d+1, nq, set()

print(numSquares2(15))