# 题目描述:
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。


class Solution:
    def twoSum(self, numbers, target):
        #   双指针模板
        i = 0   # 指向头
        j = len(numbers) - 1  # 指向尾
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return i + 1, j + 1


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))


#   要点：要用到题目中升序排列的特点
