
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #   创建一个列表嘛，看每个数组都是对称的
        self.total = [[]]
        def dfs(root, level):
            if level > len(self.total) - 1:
                self.total.append([])
            if not root:
                self.total[level].append('p')
                return
            self.total[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        for k in self.total:
            if k != k[::-1]:
                return False
        print(self.total)
        return True

root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(2)
print(Solution().isSymmetric(root))