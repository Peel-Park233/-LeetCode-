class Solution:
    def maxSubArray(self, nums):
        dp = [0 for i in range(len(nums))]
        if not nums:
            return 0
        dp[0] = nums[0]
        for k in range(1, len(nums)):
            dp[k] = max(nums[k], nums[k] + dp[k-1])
        print(dp)
        return max(dp)


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))
