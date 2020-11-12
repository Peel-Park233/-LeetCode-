class Solution:
    def solve(self, board):
        m = len(board)
        n = len(board[0])
        if m == 0 or n == 0:
            return board
        def dfs(i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return
            else:
                if board[i][j] == 'O':
                    board[i][j] = 'R'   # 和边界连续的O用R来代替
                else:
                    return

            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 四个方向传播公式
                dfs(i + x, j + y)

        for i in range(m):      # 这里就相当于是多个起点
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        # board = board.replace('O', 'X')  # 这种只能替换字符串
        # board = board.replace('R', 'O')  # 这种只能替换字符串
        print(board)
        for i in range(m):
            board[i] = ['X' if x == 'O' else x for x in board[i]]
        print(board)
        for i in range(m):
            board[i] = ['O' if x == 'R' else x for x in board[i]]
        return board


# board = [["X", "X", "X", "X"], ["X", "O", "O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
# print(board)
print(Solution().solve(board))