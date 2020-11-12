class Solution:
    def combine(self, n: int, k: int):
        #   因为'12'和'21'只能算一个，所以用下面方法遍历
        ans = []

        def dfs(i, temp):
            if len(temp) == k:
                ans.append(temp)
                return
            for j in range(i, n+1):
                dfs(j+1, temp+[j])      # 学到了data=[] ,data+=[1], data += [2], 输出data = [1, 2]

        dfs(1, [])
        return ans


print(Solution().combine(4, 2))