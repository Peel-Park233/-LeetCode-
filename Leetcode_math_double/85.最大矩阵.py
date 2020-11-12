class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]: return 0
        row = len(matrix)
        col = len(matrix[0])
        height = [0] * (col + 2)    # 左右都需要空出一格来
        print(height)
        res = 0
        for i in range(row):
            stack = []
            for j in range(col + 2):
                if 1 <= j <= col:
                    if matrix[i][j-1] == "1":
                        height[j] += 1
                    else:
                        height[j] = 0
                while stack and height[stack[-1]] > height[j]:
                    cur = stack.pop()
                    res = max(res, (j - stack[-1] - 1)* height[cur])
                stack.append(j)
        return res

A = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

print(Solution().maximalRectangle(A))

#  和柱状图中最大矩形的不同就是以每一行为底，上面这个例子就是计算着4个底的柱状图最大面积
