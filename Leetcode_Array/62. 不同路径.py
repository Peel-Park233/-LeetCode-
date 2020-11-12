# 题目描述：
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？


class Solution:
    def uniquePaths(self, m, n):
        # 创建一个m*n的矩阵方法一：
        # mat = m * [0]
        # for i in range(len(mat)):
        #     mat[i] =n * [0]    # 每一行有这么多个
        #  方法二：
        if m==0 or n==0:
            return 0
        if m==1 or n==1:
            return 1
        mat =[[0 for i in range(n)] for i in range(m)]
        # print(type(mat))
        # mat[2][0] = 1
        # print(mat)
        # print(mat[0][0])
        for i in range(m):
            mat[i][0] = 1
        # print(mat)
        for i in range(n):
            mat[0][i] = 1
        # print(mat)
        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i-1][j] + mat[i][j-1]
        # print(mat[-1][-1])
        return mat[-1][-1]


#   测试用例
if __name__ == '__main__':
    m = 2
    n = 3
    print(Solution().uniquePaths(m, n))

#   要点：首先，为什么上面左边要padding一行，因为格子数值的计算就是上面格子加左边格子， 如果不padding
#   一行上面这一行就都要先算出来，所以也可以上面一行左边一行都令为1,就变成了处理边界的问题
#   采用哈希表来储存可能的数量
#  dp的状态转移方程
