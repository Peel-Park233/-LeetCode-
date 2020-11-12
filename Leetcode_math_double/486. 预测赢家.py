# 这里我们定义dp[i][j]为[i,j]中玩家1比玩家2最多能获得的分数.
# 此时玩家1比玩家2最多能获得的分数就是nums[j]-dp[i][j-1]
# 这样来DP也可以。。。
#  遍历法就是最后取一个点从第一个点遍历到最后一个点
class Solution():
    def winner(self, nums):
        m = len(nums)
        dp = [[0 for i in range(m)] for i in range(m)]
        for i in range(m):
            dp[i][i] = nums[i]  # 已知的
        for i in range(m-2, -1, -1):      # 动态转移方程必须要倒着来，这样才可以补充下一个dp[i]需要的dp元素
            for j in range(i+1, m):
                dp[i][j] = max(nums[j] - dp[i][j-1], nums[i] - dp[i+1][j])
                print(dp)
        return dp[0][-1] >= 0


nums = [1, 5, 233, 7]
print(Solution().winner(nums))

#   DP就是由短到长，由小到大
