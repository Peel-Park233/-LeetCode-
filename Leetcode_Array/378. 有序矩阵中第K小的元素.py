#   题目描述：
# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。


class Solution:
    def kthSmallest(self, matrix, k):
        # if matrix== []:
        #     return 0
        # n = len(matrix)
        # m_index = k // n
        # n_index = k % n
        #
        # return matrix[m_index][n_index - 1]
        mat_2 = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mat_2.append(matrix[i][j])
        # print(mat_2)
        mat_2.sort()
        print(mat_2)
        return mat_2[k-1]


if __name__ =='__main__':
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    print(Solution().kthSmallest(matrix, k))


# 要点：菜鸡做法，直接把矩阵变成一行
#