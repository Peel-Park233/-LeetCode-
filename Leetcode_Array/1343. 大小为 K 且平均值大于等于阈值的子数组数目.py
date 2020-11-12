# 题目描述：
# 给你一个整数数组 arr 和两个整数 k 和 threshold 。
# 请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。


class Solution:
    print(10)
    def numOfSubarrays(self, arr, k, threshold):

        res = 0
        arr = [0] + arr
        for i in range(1, len(arr)):
            arr[i] = arr[i] + arr[i-1]
            if i >= k and arr[i] - arr[i-k] >= k * threshold:
                res = res + 1
        return res


# 测试用例
if __name__ == '__main__':
   print(Solution().numOfSubarrays(arr=[2, 2, 2, 2, 2], k=2, threshold=2))


# 要点：用原来的表来记录到这个点累加的值，再用点与点之间的相减来计算这子数组的平均值
# 妙啊，动态规划
