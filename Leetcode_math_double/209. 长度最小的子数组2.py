# 题目描述:
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。
# 如果不存在符合条件的子数组，返回 0。


class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        if nums[0] >= s:
            return 1
        i = 0  # 头
        j = 0  # 尾
        minans = 2**31 - 1
        while j < len(nums):
            numbers = sum(nums[i:j+1])

            # print(numbers)
            if numbers < s:
                j += 1
            else:
                minans = min(minans, j - i + 1)
                i += 1

        return minans if minans != 2**31 -1 else 0


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(s, nums))


#   要点：双指针好巧妙啊，尾指针用来满足条件，头指针用来完成一次计算后指向后面
#   滑动窗口
