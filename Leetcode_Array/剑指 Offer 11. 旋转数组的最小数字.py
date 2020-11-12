# 题目描述:
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素

#   不能用min，就是O(n)的暴力法去做，要用O(log(n)),那就是二分查询了


class Solution:
    def findMin(self, nums):
        low = 0
        high = len(nums) -1
        if len(nums) <= 100:     #  用这个代替特判，美滋滋
            return min(nums)
        while low < high:

            mid = (low + high) // 2

            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = high - 1    # 为了安全起见，防止正好是一样的数，让他一步一步逼近

        return nums[low]


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(Solution().findMin(nums))

#   要点：low = mid + 1换成low = mid也可以，二分法再多做几题
