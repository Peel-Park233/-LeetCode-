#  题目描述
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。


class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        if n == 0:
            return 0
        mat = [i*[0] for i in range(1, n+1)]
        # print(mat)
        # print(triangle)
        for i in range(1, n):
            for j in range(len(triangle[i])):
                if j == 0:  # 若是在最左边
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
            #   如果下面不是elif，而是if,相当于第一个if是特判，下面的if_else还会执行一次
                elif j == i:  # 这样就可以表示在最右边，我傻了
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j-1]
                else:
                    print(j)
                    triangle[i][j] = triangle[i][j] + min(triangle[i - 1][j], triangle[i-1][j-1])
        print(triangle)
        return min(triangle[-1])


if __name__ == '__main__':
    triangle = [
                 [2],
                [3, 4],
               [2, 2, 3],
              [7, 9, 10, 2]
            ]
    print(Solution().minimumTotal(triangle))

#   要点：创建一个哈希表
#  对if_else的深入理解

