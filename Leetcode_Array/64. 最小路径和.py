#  题目描述:
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。


class Solution:
    def minPathSum(self, grid):
        if grid == []:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        #  边界上这两种情况也算是特判吧，就是特判，或者padding也可以
        for i in range(1, m):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1, n):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j], grid[j-1][i]) + grid[i][j]

        return grid[-1][-1]


if __name__ == '__main__':
    grid = [
              [1, 3, 1],
              [1, 5, 1],
              [4, 2, 1]
            ]
print(Solution().minPathSum(grid))

#   要点：关于动态规划最关键就是特判吧（更准确的说是边界）
#   或者外面加一层padding然后因为求最小所以都设为2**31-1

