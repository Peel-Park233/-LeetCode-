# 题目描述：
# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
# 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

class Solution:
    def missingNumber(self, nums):
        if len(nums) == 1:
            if nums[0] == 1:
                return 0
            else:
                return 1
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] != 1:
                return nums[i+1] - 1
        if len(nums)> nums[-1]:
            return nums[-1] + 1
        else:
            return nums[0] - 1


if __name__ == '__main__':
    a = [0, 1, 3]
    print(Solution().missingNumber(a))

# 要点： 要加一些特判
