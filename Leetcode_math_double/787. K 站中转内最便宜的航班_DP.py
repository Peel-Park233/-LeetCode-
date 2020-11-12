class Solution(object):
    def findCheapesPrice(self, n, flights, src, dst, K):
        dp = [[float('inf')] *n for i in range(K+1)]
        #   初始化0次转机直达的费用,直达到这个目的地所用的钱
        for s, d, p in flights:
            if s == src:
                dp[0][d] = p
        for k in range(1, K+1):
            for s, d, p in flights:
                dp[k][d] = min(dp[k-1][d], dp[k-1][s]+p, dp[k][d])
        return dp[-1][dst] if dp[-1][dst] != float('inf') else -1