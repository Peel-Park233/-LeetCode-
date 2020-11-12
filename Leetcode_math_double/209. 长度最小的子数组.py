# 题目描述:
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。
# 如果不存在符合条件的子数组，返回 0。


class Solution:
    def minSubArrayLen(self, s, nums):
        m = []
        if nums == []:
            return 0
        for i in range(len(nums)):
            # print(i)
            score = 1
            k = 0
            for j in range(i, len(nums)):
                k += nums[j]
                if k < s:
                    score += 1
                else:
                    # print(i)
                    m.append(score)
                    break

        print(m)
        if m == []:
            return 0
        else:
            return min(m)


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(s, nums))


#   要点：一定要清楚的是要输出上面，内存只需要记录要输出的东西.
#   别忘了加一些特判


