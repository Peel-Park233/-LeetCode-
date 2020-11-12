li = [11,22,22,33,44,44]
set = set(li)
li = list(set)
print(li)
class Solution:
    def removeDuplicates(self, nums) -> int:
        ans = []
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans.append(nums[i])
        return ans
nums = [1,1,2]
print(Solution().removeDuplicates(nums))