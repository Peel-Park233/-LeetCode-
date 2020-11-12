class Solution:
    def permuteUnique(self, nums):
        m = len(nums)
        ans = []
        for i in range(m):      # 指代第几个数字
            for j in range(i+1, m):  # 指代和第几个数字交换
                temp = nums
                temp[i], temp[j] = temp[j], temp[i]   # 这样是不行的，因为temp改变位置的时候nums也改变位置了
                print(temp)
                print(nums)
                if temp not in ans:

                    ans.append(temp)
        return ans


nums = [1, 1, 2]
print(Solution().permuteUnique(nums))