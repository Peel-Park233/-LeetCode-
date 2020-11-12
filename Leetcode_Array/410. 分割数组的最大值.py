# 题目描述:
# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。
# 设计一个算法使得这 m 个子数组各自和的最大值最小。


class Solution:
    def splitArray(self, nums, m):
        #   这样二分我是没想到的

        def check(mid):
            sumt = 0  # 加了多少数
            kuai = 1
            for i in nums:
                if sumt + i <= mid:
                    sumt += i
                else:
                    kuai += 1
                    sumt = i  # 直接把下一块的初始值设置为i，妙啊
            if kuai > m:     # 块多了就是mid小了
                return True
            else:
                return False
        low = max(nums)
        high = sum(nums)
        while low < high:
            mid = (low + high) // 2  # 向下取整
            if check(mid):
                low = mid + 1
            else:
                high = mid
        return low


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    print(Solution().splitArray(nums, m))


#   二分模板
#   第一步，先确定要二分什么，确定low和high
#   第二步，mid满足什么条件对low这边缩进，什么条件对high这边缩进
#   最后return low

# 要点：关键是对哪个二分.
# 先按照二分模板来，具体的实现如果麻烦的话可以再写一个函数


