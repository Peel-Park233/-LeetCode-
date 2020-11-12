class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import defaultdict     # 不过为啥这个defaultdict有.next的方法
                                        #   这个函数就是如果没有就设置为默认值
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #   有意思，结合了链表和二叉树
        ans = defaultdict(list)
        def dfs(root, level):
            if not root:
                return
            # if level > len(ans):
            #     ans.append([])
            # ans[level-1].append(root.val)
            dfs(root.left, level+1)
            ans[level].append(root)
            dfs(root.right, level+1)
        dfs(root, 0)
        # print(ans)
        for k in ans.keys():
            for j in range(len(ans[k])-1):
                ans[k][j].next = ans[k][j+1]
        return root     # 最后return的是root，愣是没看懂