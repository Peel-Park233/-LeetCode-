class Solution:
    def combinationSum2(self, candidates, target: int):
        #   dfs
        length = len(candidates)
        ans = []
        def dfs(k, temp):
            if sum(temp) > target:
                return
            if sum(temp) == target:
                temp.sort()
                if temp not in ans:
                    ans.append(temp)
                return
            for i in range(k, length):
                dfs(i+1, temp+[candidates[i]])
        dfs(0, [])

        return ans


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))

#   怎么老是一样的题啊