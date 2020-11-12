class Solution:
    def getPermutation(self, n: int, k: int):
        #   定义一个递归函数
        #   输入值是现有的数组，剩余的数组
        total = ''
        ans = []
        for i in range(1, n+1):
            total += str(i)

        def dfs(temp, others):
            if len(ans) == k:       # 加了这个之后可以多过90个case
                return
            if len(others) == 0:
                ans.append(temp)
                return
            for i in range(len(others)):
               dfs(temp + str(others[i]), others[:i] + others[i+1:])

        dfs('', total)
        print(len(ans))
        return ans[k-1]


n = 7
k = 2020
print(Solution().getPermutation(n, k))

#   感悟递归真是一种有意思的遍历方法
