#   题目描述：
#   给定一个n个整数的数组nums和一个目标值target，找出数组中三个数，使它们的和与target最相近
#   返回他们的和
class Solution:
    def threeSum(self, nums, target):
        nums.sort()
        #   双指针模板
        i = 0  # 指向头
        j = len(nums) - 1
        minnum = 2**31 - 1
        number = 0
        print(nums)
        while (i < j):
            #   先确定 i，j，然后在k里面挑出一个最接近的
            for k in range(i + 1, j):
                now = nums[i] + nums[j] + nums[k]
                # print(now)
                # print (now - target)
                # print(now - target)
                # print(minnum)
                if abs(now - target) < minnum:
                    minnum = abs(now - target)
                    number = now
            print(number)
            if number < target:
                i += 1
            elif number > target:
                j -= 1
            else:
                return number
        return number



if __name__ == '__main__':
    # nums = [-1, 2, 1, -4]
    nums = [4, 0, 5, -5, 3, 3, 0, -4, -5]
    target = -2
    print(Solution().threeSum(nums, target))


#   要点：这样遍历会少一些样本，多一些重复的样本。应该是二分放在移动点的里面
