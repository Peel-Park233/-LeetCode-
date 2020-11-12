class Solution:
    def fourSum(self, nums, target: int):
        #   dfs
        ans = []

        def dfs(temp, others):  # 定义输入输出
            if len(temp) == 4:  # 定义结束条件
                temp.sort()
                print(temp)
                if sum(temp) == 0 and temp not in ans:
                    ans.append(temp)
                    return
                else:
                    return

            for i in range(len(others)):  # 定义单步逻辑
                dfs(temp + [others[i]], others[:i] + others[i + 1:])

        dfs([], nums)
        return ans
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(Solution().fourSum(nums, target))