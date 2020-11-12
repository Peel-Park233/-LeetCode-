#   动态规划嘛，由短到长
class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        if len(strs) == 0:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 准备很多个背包

        for strs_item in strs:
            item_count0 = strs_item.count('0')
            item_count1 = strs_item.count('1')

            # 遍历可容纳的背包
            for i in range(m, item_count0 - 1, -1):  # 采取倒序
                for j in range(n, item_count1 - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - item_count0][j - item_count1])
                    print(dp)
        return dp[m][n]


Array = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(Solution().findMaxForm(Array, m, n))

#   不得不说，实在太牛逼了，用m,n来代表0和1的个数，然后得到的dp状态转移方程
#   dp[i][j] = max(dp[i][j], 1 + dp[i - item_count0][j - item_count1])

# 背包问题（Knapsack problem）是动态规划的经典问题。动态规划的基础是递归，
# 和分治一样，都是假设子问题已经解决，由子问题的解组合计算得到父问题的解，
# 类似裴波那契数列中的递推式如f(n) = f(n-1) + f(n-2)。但在递归的过程中会出现重复计算子问题的现象，
# 为了避免重复计算，用一个表格记录子问题的结果供查找，从下往上进行递推。
# 找递推式（or 状态转移方程）的思路一般是由最终状态往前回溯，考察解答最终问题需要哪些子问题。







