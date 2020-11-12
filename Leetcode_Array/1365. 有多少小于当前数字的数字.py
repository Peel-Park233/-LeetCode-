class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        for i in nums:
            temp = 0
            for j in nums:
                if j < i:
                    temp += 1
            ans.append(temp)
        return ans