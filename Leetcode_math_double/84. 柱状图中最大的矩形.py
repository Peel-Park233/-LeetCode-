#   这种遍历的方法，设定起始点的高度为最低高度，根据宽度不断向两边扩展
class Solution:
    def largestRectangleArea(self, heights):
        ans = 0
        for i in range(len(heights)):
            j, k = i, i  # 左右指针
            while(j >= 0) and heights[j] >= heights[i]:
                # 左指针探寻左边的节点
                #   就算j=-1指向了最后一点也没事，因为肯定不满足j>=0
                j -= 1
            while(k < len(heights)) and heights[k] >= heights[i]:
                # 右指针探寻右边的节点
                k += 1
            # print(j, k)
            # print(heights[j])
            ans = max(ans, (k - j - 1) * heights[i])
            print(ans)
        return ans


A =[2, 1, 5, 6, 2, 3]
# A = [2]
print(Solution().largestRectangleArea(A))

A.pop()  # 默认删除尾部元素
print(A)

#  但是这样算时间复杂度太高了