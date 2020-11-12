class Solution:
    def topKFrequent(self, nums, k: int):
        setnums = []
        record = []
        for i in nums:
            if i in setnums:
                p = setnums.index(i)
                record[p] += 1
            else:
                setnums.append(i)
                record.append(1)
        length = len(setnums)
# Python如何在对一个列表排序的同时对另一个列表进行操作(排序)
#   方法就是放到一起去然后按照第一行排序
        total = []
        for i in range(len(setnums)):
            total.append([record[i], setnums[i]])
        total.sort()
        print(total)
        ans = []
        for i in range(k):
            ans.append(total[-1][1])
            total.pop(-1)
        return ans


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))


