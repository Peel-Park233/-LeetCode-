from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #   每次只能参加一笔交易
        #   那就把之前那题目分成两份
        def findProfit(price):
            m = len(price)
            dp = [0 for _ in range(m)]
            for i in range(m-1):
                dp[i] = max(price[i+1:]) - price[i]
            return max(dp)
        if len(prices) < 4:
            return findProfit(prices)
        ans = findProfit(prices)
        for i in range(2, len(prices)-1):
            ans = max(ans, findProfit(prices[:i]) + findProfit(prices[i:]))
        return ans


prices = [3,3,5,0,0,3,1,4]
print(Solution().maxProfit(prices))

#   又超时啦
