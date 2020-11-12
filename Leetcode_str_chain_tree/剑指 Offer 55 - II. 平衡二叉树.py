class Solution:
    def depth(self, root):
        if root:
            return 1 + max(self.depth(root.left), self.depth(root.right))
        else:
            return 0

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.depth(root.right) - self.depth(root.left)) > 1:  # 调用这自己类的函数需要加self
            return False

        return self.isBalanced(root.right) and self.isBalanced(root.right)