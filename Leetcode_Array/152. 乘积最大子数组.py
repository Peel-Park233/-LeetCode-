class Solution:
    def maxProduct(self, nums):
        # 研究以遍历每个起点可能的最大乘积
        m = len(nums)
        if m <= 1:
            return nums[-1]
        ans = 0
        for i in range(m):
            dp = [0 for _ in range(m)]
            dp[i] = nums[i]
            for j in range(i+1, m):
                dp[j] = dp[j-1] * nums[j]
            ans = max(ans, max(dp))
        return ans


# nums = [2, 3, -2, 4]
nums = [-2,0,-1]
print(Solution().maxProduct(nums))
