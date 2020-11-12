class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


A = [3, 9, 20, 1, 1, 15, 7]
print(max(A))
this_tree_root = TreeNode(A)
print(this_tree_root.val)
a = []
print(len(a))

#  所以说这道题目就是广度优先搜索
#
# if not root:
#     return []
result = []

# root = TreeNode()
#   好像并不是广度优先搜索，而是符合这个level的自动归到这一层
def add_result(level, node):
    if level > len(result) - 1:  # 看是不是这一层的，如果超出这一层result也加一层
        result.append([])
    result[level].append(node.val)   # 在这一层添加上node的值
    if node.left:   # 如果这个node左节点存在
        add_result(level+1, node.left)
    if node.right:
        add_result(level+1, node.right)

# add_result(0, root)
# B=[]
# print(max(B))
# return result，
#   为什么这个递归不需要返回值，因为都加到result上面了呀
