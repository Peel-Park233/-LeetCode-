# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val == p.val or root.val == q.val:
                # return p or q
                return root
            elif p.val < root.val < q.val or p.val > root.val > q.val:
                return root
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                root = root.right




#   利用二叉搜索树的性质
#   当p.val<root.val<q.val,那么这个root就是他的根节点
#   如果root.val>p.val and root.val>q.val,那么root.val太大了，root = root.left
#   反之就是root.val太小了，root = root.right
