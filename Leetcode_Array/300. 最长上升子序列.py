class Solution:
    def lengthOfLIS(self, nums):
        score = 0
        for i in range(len(nums)):

            temp = [nums[i]]
            for j in range(i+1, len(nums)):
                if nums[j] > temp[-1]:
                    temp.append(nums[j])
            print(temp)
            score = max(len(temp), score)
        return score


nums = [10, 9, 2, 5, 3, 4]
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().lengthOfLIS(nums))

#   动态规划，由短到长
