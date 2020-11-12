class Solution:
    def invertTree(self, root):
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            root.left, root.right = root.right, root.left
            #   这样的顺序就是他会先不断深度往下，直到最后一个开始交换，然后上一个节点交换
            #   不过先反转最后上面两个，然后再去反转下面的好像也可以哎
        dfs(root)
        return root