class Solution:
    def combine(self, n: int, k: int):
        #   先暴力法
        data = []
        for i in range(1, n+1):
            data.append(i)
        ans = []

        def dfs(data, temp):
            if len(temp) == k:
                # print(temp)
                ans.append(temp)
                # print(ans)
                return
            for i in range(len(data)):
                # temp.append(data[i])    #   这个temp放在外面就会不断地累加，导致最后的ans输出的就是temp
                dfs(data[:i]+data[i+1:], temp+[data[i]])    # 太对了哥，哥太对，对于inttemp+[data[i]]这个可以append香多了

            return
        dfs(data, [])
        print(ans)
        return ans

n = 4
k = 2
Solution().combine(n, k)





