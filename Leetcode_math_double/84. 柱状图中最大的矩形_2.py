#   维护一个递增的栈，当出现小于的数就多次计算前面的面积,递增栈的概念
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        heights = [0] + heights + [0]   # 前后都加上0
        res = 0
        for i in range(len(heights)):
            print('第', i, '次')
            while stack and heights[stack[-1]] > heights[i]:
                print(stack)
                tmp = stack.pop()
                # print(tmp)
                print(stack)    # 这里stack留下的那个数乘以长度
                # print(i, stack[-1], heights[tmp])
                score = (i - stack[-1] - 1) * heights[tmp]
                res = max(res, score)
                print(score)
            stack.append(i)

        return res

# 上述写法中，我们需要再嵌套一层 while 循环来向左找到第一个比柱体 i 高度小的柱体，
# 这个过程是 O(N) 的那么我们可以 O(1) 的获取柱体 i 左边第一个比它小的柱体吗？
# 答案就是单调增栈，因为对于栈中的柱体来说，栈中下一个柱体就是左边第一个高度小于自身的柱体。


B = [0, 2, 1, 5, 6, 2, 3, 0]
A = [2, 1, 5, 6, 2, 3]
# A = [2]
print(Solution().largestRectangleArea(A))

# A.pop()  # 默认删除尾部元素
# print(A)

#   总结，这个栈就一定要维持递增的状态，如果下一个比上一个小了了，就去掉那些比它高的，并计算面积
#   然后继续维持递增的栈