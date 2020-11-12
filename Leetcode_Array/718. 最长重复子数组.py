# 题目描述：给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。


class Solution:
    def findLength(self, A, B):
        # n = len(A)
        # m = len(B)
        # box = []
        # if n == 0 or m == 0:
        #     return 0
        # for i in range(n):
        #     if A[i] in B:
        #         B.remove(A[i])
        #         box.append(A[i])
        #
        # return len(box)
        m = len(A)
        n = len(B)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]  # m行n列的数组
        score = 0
        #   就相当于dp矩阵padding了一行一列0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i-1] == B[j-1]:    # 这是子数组相同的起点
                    dp[i][j] = dp[i-1][j-1] + 1
                    score = max(score, dp[i][j])
        print(dp)
        return score


if __name__ == '__main__':
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    print(Solution().findLength(A, B))

#  要点：子数组总是连续的
#   对应的图画出来了，结果也就出来了
