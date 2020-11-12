#    定义链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#    定义链表
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 永远要记得head就是一个指针！！！，链表的值会改变，但是指针指向的位置不会变！！！
# 探究h = head后，h和head有什么关系 ,意思就是说head的指针一直指向第0个数
# 但是改变h会改变head指针的方向改变了！！！
# # 定义二叉树,
# class Tree:
#     def __init__(self, val, right=None, left=None):
#         self.right = right
#         self.left = left
#         self.val = val


# 定义二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

