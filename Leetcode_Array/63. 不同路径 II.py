#  题目描述:还是机器人网格题，现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid == []:
            return 0
        m = len(obstacleGrid)   # 行数
        n = len(obstacleGrid[0])    # 列数
        dp = [[0 for i in range(n+1)]for j in range(m+1)]   # 靠，这里写错了，print检查出来了
        dp[0][1] = 1
        print(dp)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0        # 妙啊，障碍物设置为0，即解决了本身，又正好适应作为加数相加
                else:
                    # print(j)
                    # print(dp[i][j - 1])
                    # print(dp[i - 1][j])
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    ob = [
          [0, 0, 0],
          [0, 1, 0],
          [0, 0, 0]
        ]
    print(Solution().uniquePathsWithObstacles(ob))


# 要点：障碍物用0替代，针对右边或下面的点就相当于少了一条路
