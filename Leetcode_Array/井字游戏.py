# 题目描述:
# 设计一个算法，判断玩家是否赢了井字游戏。输入是一个 N x N 的数组棋盘，
# 由字符" "，"X"和"O"组成，其中字符" "代表一个空位。


class Solution:
    def tictactoe(self, board):
        re = []     # 所有情况
        x = ''  # 斜着的
        u = ''  # 反斜着的
        n = len(board)
        for i in range(n):
            re.append(board[i])    # 保存横着的
            x += board[i][i]       # 斜着的
            u += board[i][n-i-1]   # 反斜着的
        print(x)
        re.append(x)
        re.append(u)
        for i in range(n):
            s = ''  # 竖着的
            for j in range(n):
                s += board[j][i]
            re.append(s)
        print(re)
        if n*'X' in re:
            return "X"
        if n*'O' in re:
            return "O"
        if ' ' in ''.join(board):
            return "Pending"
        else:
            return "Draw"


#   测试用例
if __name__ == '__main__':
    board = ["O X", " XO", "X O"]
    print(Solution().tictactoe(board))

# 要点：保存所有情况下的横着的，斜着的，竖着的，然后用 in 函数进行查询是否有
