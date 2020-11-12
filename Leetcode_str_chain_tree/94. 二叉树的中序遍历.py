class Solution:
    def inorderTraversal(self, root):
        white, gray = 0, 1
        stack = [(white, root)]
        ans = []
        while stack:
             color, node = stack.pop()  # 最后一个放进去的开始删除
             if node is None: continue
             if color == white:
                 stack.append((white, node.right))  # 中序列，左中右，所以放进去是右中左
                 stack.append((gray, node))
                 stack.append((white, node.left))

             else:
                 ans.append(node.val)
        return ans
