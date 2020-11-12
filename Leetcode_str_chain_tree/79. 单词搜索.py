class Solution:
    def exist(self, board, word: str):
        n = len(board)
        m = len(board[0])
        self.ans = False
        #   dfs 已经用过的字母要设定为0
        def dfs(i, j, temp_word):
            print(len(temp_word))
            print(temp_word)
            if len(temp_word) == 0:
                self.ans = True
                return     # 但只是这个方法return了True
            temp = board[i][j]
            board[i][j] = '0'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy
                # print(x, y)
                # print(dx, dy)
                if 0 <= x < n and 0 <= y < m:
                    # print(board[x][y])
                    if board[x][y] == temp_word[0]:
                        dfs(x, y, temp_word[1:])
            # 那什么时候还回去呢，就是以这个为开始点的DFS结束的时候还回去
            board[i][j] = temp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(i, j, word[1:])

        return self.ans

#   原来这就是回溯啊，早说嘛
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"

print(Solution().exist(board, word))