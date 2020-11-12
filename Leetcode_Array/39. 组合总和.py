class Solution:
    def combinationSum(self, candidates, target: int):
        ans = []
        #   对得到的结果sort然后判断它是否存在原来的数组
        def dfs(temp):
            if sum(temp) > target:
                return
            if sum(temp) == target:
                temp.sort()
                if temp in ans:
                    return
                else:
                    ans.append(temp)
            for i in candidates:
                dfs(temp+[i])
        dfs([])
        return ans


candidates = [2, 3, 5]
target = 8
print(Solution().combinationSum(candidates, target))


#   感悟，dfs感觉可以说是掌握了