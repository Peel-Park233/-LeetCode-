# 题目描述：景点的评分之和减去它们两者之间的距离。
# 返回一对观光景点能取得的最高分。


class Solution:
    def maxScoreSightseeingPair(self, A):
        # n =len(A)
        # score = 0
        # compare = 0
        # if n < 2:
        #     return 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         compare = A[i] + A[j] + i - j
        #         score = max(compare, score)
        #
        # return score
        score = 0
        n = len(A)
        if n < 2:
            return 0
        pre_max = 0 + A[0]
        for j in range(1, n):
            score = max(score, pre_max + A[j] - j)
            pre_max = max(pre_max, A[j] + j)        # 因为下一个指向的数肯定在他右边，所以可以取最大值
        return score


if __name__ == '__main__':
    print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))

#   这题中等难度，脑子呢！
#   通过数学的方式将A[i] + i + A[j] - j分开，然后储存前面的最大值，遍历后面那个数即可，妙啊！


