class Solution:
    def findMode(self, root):
        self.ans = []
        def dfs(root):
            if not root:
                return
            self.ans.append(root.val)
            dfs(root.right)
            dfs(root.left)
        dfs(root)
        # print(self.ans)
        if len(self.ans) <= 1:
            return self.ans
        self.ans.sort()
        nums = self.ans
        # final = []
        # number = 1
        # max_1 = 1
        #   遇到的一个问题就是最后一个数怎么办
        # for i in range(len(nums)-1):
        #     if nums[i+1] == nums[i]:
        #         number += 1
        #     else:
        #         if number == max_1:
        #             final.append(nums[i])
        #         elif number > max_1:
        #             final = [nums[i]]
        #             max_1 = number
        #         number = 1
        #     if nums[i] == nums[i-1] and i == len(nums) - 1:
        #         number += 1
        #         if number == max_1:
        #             final.append(nums[i])
        #         elif number > max_1:
        #             final = [nums[i]]
        #             max_1 = number
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dp[i]  = dp[i-1] + 1
        max_1 = max(dp)
        final = []
        # print(max_1)
        # print(nums)
        for i in range(len(dp)):
            if dp[i] == max_1:
                final.append(nums[i])

        return final

#   为什么不开大呢！！！！！
#   为什么不用dp呢！！！！！
