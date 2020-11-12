# 题目描述：买卖股票的最佳时机含手续费
#   同时也是动态规划题


class Solution:
    def maxProfit(self, prices, fee):
        if len(prices) == 0:
            return 0
        # lirun= []
        # k = 0
        # jiage = 0
        # for i in range(len(prices)-1):
        #     if k == 0 and prices[i+1]>prices[i]:
        #         k = k + 1
        #         jiage = prices[i]
        #     if k == 1 and prices[i] < prices[i+1] and prices[i] - jiage>2:
        #         k = k - 1
        n = len(prices)
        dp = [[0 for i in range(2)]for i in range(n)]   # 两行 n列
        # print(dp)
        dp[0][0] = 0        # 第一天不买的话钱是多少
        dp[0][1] = -prices[0] - fee   # 第一天买的话钱是多少
        for i in range(1, n):
            # 第i天如果不持有，只有两种可能，1.前一天就没有买，2.前一天买了，今天卖了
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # 第i天如果持有，只有两种可能，1.前一天没买，今天买了，2.前一天就买了
            dp[i][1] = max(dp[i-1][0] - prices[i] - fee, dp[i-1][1])
        print(dp)
        return dp[-1][0]


if __name__ == '__main__':
    prices = [1, 2, 10, 4, 6, 9, 2]
    fee = 2
    print(Solution().maxProfit(prices, fee))

#   要点：这就是动态规划吗，爱了爱了。如果这步之前都是最优的，你只需要选择这步最优就好了
#    也不是是根据这步如果这样选前一步的最优选择是什么。反向推导。一种有目的的，动态的方式把可能都记录下来
#   把一个大问题拆分成很多个可以重复的小问题，把之前的选择都保留下来，以空间换时间。
