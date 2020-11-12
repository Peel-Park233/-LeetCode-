A = [-10, -3, 0, 5, 9]
print(A)
A.sort()
print(A)
#   就每次把一组数最中间的位置，作为树的头拎起来，剩下部分平均分两份就行


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):

        def make_tree(start_index, end_index):  # 只和长度有关
            # 首先判定我们的区间是否合理，即left_index要<=right_index
            # 当相等时，只有root会产生，不会产生左右小树
            if start_index > end_index:
                return None

            # 我这里变量名都写得比较长，目的是方便理解
            mid_index = (start_index + end_index) // 2
            this_tree_root = TreeNode(nums[mid_index])  # 做一个小树的root

            this_tree_root.left = make_tree(start_index, mid_index - 1)
            this_tree_root.right = make_tree(mid_index + 1, end_index)
            # print(this_tree_root)
            return this_tree_root  # 做好的小树
        return make_tree(0, len(nums)-1)


print(Solution().sortedArrayToBST(A))
