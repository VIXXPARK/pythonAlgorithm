class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices or len(prices) == 1:
            return 0
        differenceList = [0] * (len(prices) - 1)
        for i in range(1, len(prices)):
            differenceList[i - 1] = prices[i] - prices[i - 1]
        highestStock = [0] * len(differenceList)
        accumulator = 0
        for index in range(0, len(differenceList)):
            if 1 <= accumulator + differenceList[index]:
                accumulator += differenceList[index]
                highestStock[index] = accumulator
            else:
                highestStock[index] = accumulator
                accumulator = 0
        return max(highestStock)

s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))