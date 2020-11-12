# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        def dfs(preorder, inorder):
            if not preorder:
                return
            ind = inorder.index(preorder[0])
            root = TreeNode(preorder[0])
            #   最关键一步，pre左边的数
            root.left = dfs(preorder[1:ind+1], inorder[:ind])
            root.right = dfs(preorder[ind+1:], inorder[ind+1:])
            return root

        return dfs(preorder, inorder)
