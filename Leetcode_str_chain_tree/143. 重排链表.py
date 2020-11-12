class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        ans = []
        # start = head
        pre = head
        # 这个做了什么，这个相当于将所有指针都放到这个列表里啦
        while head:
            ans.append(head)
            head = head.next
        # print(ans)
        m = len(ans)
        for i in range(m//2):
            ans[i].next = ans[~i]
            # ans[i].next = ans[m - i -1]
            ans[~i].next = ans[i+1]
        ans[m//2].next = None
        return ans[0]


#   妙啊，用列表储存节点！！！
# 注意的是最后那个节点要指向None