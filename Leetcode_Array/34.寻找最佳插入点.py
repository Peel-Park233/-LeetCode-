#   题目描述：
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，
# 返回它将会被按顺序插入的位置。   你可以假设数组中无重复元素。


class Solution:
    def searchInsert(self, nums, target):

        if len(nums) == 0:
            return 0
        low = nums[0]
        high = nums[-1]
        k = 0
        for i in range(0, len(nums)):
            if target == nums[i]:
                return i
            elif target > nums[i]:
                k += 1
                if k == len(nums):
                    return k
            else:
                return i


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    print(Solution().searchInsert(nums, target))

#  要点：很简单的一道题目，不要强行想要二分嘛
#   如果要用二分法，low和high就要作为数组的index，二分法好就好在logn

print()




