# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        start = ListNode(0)  # 先搞一个空节点的原因是防止删除的就是头结点
        start.next = head
        test = head
        ans = start
        while test:
            test = test.next
            length += 1
        point = length - n
        #   指到要删除哪个节点的前一个节点
        while point > 0:
            start = start.next
            point -= 1

        start.next = start.next.next
        return ans.next