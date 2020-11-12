
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, x):
        #         self.val = x
        #         self.left = None
        #         self.right = None

        class Solution:
            def binaryTreePaths(self, root: TreeNode):

                if not root:
                    return []

                res = []

                def dfs(root, path):
                    path += str(root.val)
                    if not root.left and not root.right:
                        res.append(path)
                    elif not root.left:
                        dfs(root.right, path + '->')
                    elif not root.right:
                        dfs(root.left, path + '->')
                    else:
                        dfs(root.right, path + '->')
                        dfs(root.left, path + '->')

                dfs(root, '')
                return res


A = [1, 2, 3, 4]
# A.pop()  # 默认pop倒数第一个
#   对啊，为什么一定要用矩阵来保存这个序列呢，直接用字符串++不香吗
B = ''
for i in A:
    B += str(i)
print(B)