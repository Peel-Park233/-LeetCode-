class Solution:
    def solve(self, board):
        m = len(board)
        n = len(board[0])
        if m == 0 or n == 0:
            return board

        def dfs(i,  j):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                return  # 不做改变
            # if board[i-1][j] != 'O' and board[i][j-1] != 'O' and  board[i][j+1] != 'O' and board[i+1][j] != 'O':
            #     board[i][j] = 'X'
            else:
                return

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return board


board = [['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X'],['X', 'X', 'O', 'X'],['X', 'O', 'X', 'X']]
# print(board[1][3])
print(Solution().solve(board))

#   和刚刚那题图像渲染一样，刚刚是从一个点渲染，现在是从边界渲染