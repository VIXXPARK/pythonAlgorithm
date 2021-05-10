class Solution: ## 내 풀이
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins=set(coins)
        coins=list(coins)
        coins.sort()
        dp=[0]*(amount+1)
        cur=0;flag=True
        for i in range(1,amount+1):
            if flag:
                flag=False
            if cur<len(coins) and coins[cur]==i:
                dp[coins[cur]]=1
                cur+=1
            else:
                for coin in coins[:cur+1]:
                    if dp[i] and i>coin:
                        if dp[i-coin]!=0:
                            dp[i]=min(dp[i],dp[i-coin]+1)
                    else:
                        if i>coin:
                            if dp[i-coin]!=0:
                                dp[i]=dp[i-coin]+1
        if not flag:
            return dp[-1] if dp[-1] else -1
        else:
            return 0

#############################################################################

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1