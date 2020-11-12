class Solution:
    def pondSizes(self, land):
        if not land: return 0
        ans = []

        def dfs(i, j):
            if land[i][j] == 0: # 这里再判断一次的目的是防止下面步骤dfs进入1的
                self.score += 1
                land[i][j] = 1
            for m, n in [(-1, 0), (-1, 1), (1, 0), (1, -1), (-1, -1), (0, -1), (1, 1), (0, 1)]:
                if 0 <= i+m < len(land) and 0 <= j+n < len(land[0]) and land[i+m][j+n] == 0:
                    dfs(i+m, j+n)

        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 0:
                    self.score = 0
                    dfs(i, j)
                    ans.append(self.score)

        return sorted(ans)
land = [
  [0, 2, 1, 0],
  [0, 1, 0, 1],
  [1, 1, 0, 1],
  [0, 1, 0, 1]
]
print(Solution().pondSizes(land))

# 好像这种类型的dfs的题目差不多，都需要将这个值改变
# 当DFS什么时候结束不是确定的，这个时候就需要定义实例变量
# python的几种变量——按作用域分
# 1、全局变量：在模块内、在所有函数外面、在class外面，这就是全局变量。
# 2、局部变量：在函数内、在class的方法内（未加self修饰的) ,这就是局部变量
# 3、静态变量（也可以说，类属性）：在class内的，但不在class的方法内的，这就是静态变量
# 4、实例变量（也可以说，实例属性）：在class的方法内的，用self修饰的变量，这就是实例变量

# 类变量和实例变量的区别在于：类变量是所有对象共有，其中一个对象将它值改变，其他对象得到的就是改变后的结果；
# 而实例变量则属对象私有，某一个对象将其值改变，不影响其他对象