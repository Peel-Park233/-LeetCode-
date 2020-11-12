class Solution:
    def exist(self, board, word: str):
        n = len(board)
        m = len(board[0])
        def dfs(index, x, y):
            if index == len(word) - 1 and board[x][y] == word[-1]:
                return True     # 这里返回True仅仅是递归中的一个子递归通过了
            temp = board[x][y]
            board[x][y] = 0
            for i, j in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if 0 <= i <n and 0 <= j < m and board[i][j] != 0 and board[i][j] == word[index+1]:
                    if dfs(index + 1, i, j):    # 递归的同时加一个判断，如果上面返回True，这个函数也返回True
                        return True
            board[x][y] = temp
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(0, i, j):
                        return True
        return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"

print(Solution().exist(board, word))
