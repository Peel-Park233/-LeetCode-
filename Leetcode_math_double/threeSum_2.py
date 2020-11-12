#   题目描述：
#   给定一个n个整数的数组nums和一个目标值target，找出数组中三个数，使它们的和与target最相近
#   返回他们的和
class Solution:
    def threeSum(self, nums, target):
        nums.sort()
        ans = 0
        minnum = 2**32 - 1
        for i in range(len(nums) - 2):

            #   双指针模板
            j = i + 1  # 指向头
            k = len(nums) - 1
            while j < k:
                now = nums[i] + nums[j] + nums[k]
                if abs(now - target) < minnum:
                    ans = now
                    minnum = abs(now - target)
                if now < target:
                    j += 1
                elif now > target:
                    k -= 1
                else:
                    return ans
        return ans


if __name__ == '__main__':
    # nums = [-1, 2, 1, -4]
    nums = [4, 0, 5, -5, 3, 3, 0, -4, -5]
    target = -2
    print(Solution().threeSum(nums, target))

#  和第一种方法最大的差别其实就是做指针判断的时候前一种是多个k 做一次，这种是每个i做很多次
