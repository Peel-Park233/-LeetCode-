class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, i, j):
            while i < j:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if len(nums) < 2:
            return
        m = len(nums)
        point = m - 1
        while point > 0 and nums[point] <= nums[point-1]:   # 截断判断，又用到了
            point -= 1
        if point == m - 1:
            nums[m-1], nums[m-2] = nums[m-2], nums[m-1]
            return
        if point == 0:
            nums.reverse()
            return
        # print(point)
        for i in range(m-1, point-1, -1):
            if nums[i] > nums[point-1]:
                nums[i], nums[point-1] = nums[point-1], nums[i]
                break
        # nums[point:].reverse()
        reverse(nums, point, m-1)

#   这道题目还是很复杂的，需要进行的操作很多
#   目的就是找到一个稍微比原来那个数大一点的数

#  可以这样想，从后往前如果前面的数比后面的数大，那么就不可能换，所以找到一个
#   前面较小的数和后面较小但比前面大的那个数来与之交换。交换后再按
#   从小到大安排后面的数
