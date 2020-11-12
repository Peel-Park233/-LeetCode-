class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #   dfs，就一块岛屿所以不需要dfs
        # 巧妙的方法就是只要上面有一条边，下面就一定会有一条边
        # 所以只需要判断左边和上面是否为0就能知道有多少条边
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i-1 < 0 or grid[i-1][j] == 0:    # 如果小于0就会直接截断，不会进行下一步判断所以不会越界
                        ans += 1
                    if j-1 < 0 or grid[i][j-1] == 0:
                        ans += 1
                    if i+1 > m-1 or grid[i+1][j] == 0:
                        ans += 1
                    if j+1 > n-1 or grid[i][j+1] == 0:
                        ans += 1
        return ans

#   当然普通的方法也可以
#   新技巧就是if的判断截断