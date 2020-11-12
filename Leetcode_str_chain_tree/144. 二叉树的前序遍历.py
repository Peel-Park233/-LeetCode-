# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        white = 1
        gray = 0
        stack = [(root, white)]
        while stack:
            root, color = stack.pop()
            if not root:
                continue
            if color == white:
                stack.append((root.right, white))
                stack.append((root.left, white))
                stack.append((root, gray))
            else:
                ans.append(root.val)
        return ans