class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        m = len(image)
        n = len(image[0])
        base_color = image[sr][sc]
        if m == 0 or n == 0:
            return image
        if image[sr][sc] == newColor:
            return image

        def dfs(i, j):  # 1.确定递归函数的参数和返回值：改变原来的值，不需要返回什么
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:  # 2.确定终止条件：直接结束不输出什么就直接return就行
                return
            if image[i][j] == base_color:  # 3.确定单层递归的逻辑： 确定每一层递归需要处理的信息。下面几行都是
                image[i][j] = newColor
            else:
                return
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i+x, j+y)
                # print(i + x, j + y)
        dfs(sr, sc)
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
print(Solution().floodFill(image, sr, sc, newColor))

#  总结：这题还是要回到递归的知识点，你发现没，这种有规律，但是无法按顺序来的都是递归来做
#    1.确定递归函数的参数和返回值：
# #   确定哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数，
# #   并且还要明确每次递归的返回值是什么进而确定递归函数的返回类型。
#   2.确定终止条件：直接结束不输出什么就直接return就行
#   3.确定单层递归的逻辑： 确定每一层递归需要处理的信息。
