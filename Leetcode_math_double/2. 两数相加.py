class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode(0)       # 头结点，无存储，指向链表的第一个节点
        l3 = start          # 初始化链表节点
        temp = 0            # 初始化进一的数
        while l1 and l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            # if a + b <= 9:        # 其实这个用% 和 // 表示更好,应该还要加上temp
            #     if temp == 1:
            #         l3.next = ListNode(a + b + 1)
            #         temp = 0
            #     else:
            #         l3.next = ListNode(a + b)
            # else:
            #     if temp == 1:
            #         l3.next = ListNode(a + b - 10 + 1)
            #         temp = 0
            #     else:
            #         l3.next = ListNode(a + b - 10)
            #     temp += 1
            sum = a + b + temp
            temp = sum // 10
            l3.next = ListNode(sum % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            l3 = l3.next
        if temp != 0:
            l3.next = ListNode(1)
        return start.next  # 返回头结点的下一个结点，即链表的第一个结点

#   关于链表，先留一个指针指向头，然后生成新链表的方式就是l3.next = ListNode(value)