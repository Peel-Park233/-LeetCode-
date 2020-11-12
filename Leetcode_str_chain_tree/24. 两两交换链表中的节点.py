class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode):
        # i = 0
        # 他这里是新建一个链表
        pre = ListNode(0)
        copy = pre
        while head and head.next:
            first = head
            Next = head.next
            Three = head.next.next
            Next.next, first.next = first, Three
            pre.next = Next  # 保存交换过的数据
            pre = first     # 就是上一组数的最后节点
            head = Three    # 下一组数的开始节点
        return copy.next
