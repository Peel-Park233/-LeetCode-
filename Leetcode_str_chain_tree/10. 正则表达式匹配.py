class Solution:
    def isMatch(self, s: str, p: str):
        #   目标就是实现这两种功能，以及这两种功能配合起来
        # def match(s_index, p_index):
        #     if s_index == 0 and p_index == 0:
        #         return True
        #     if s_index == 0 and p_index != 0:
        #         return False
        #     if s_index != 0 and p_index == 0:
        #         return False
        #     if s[s_index] == p[p_index]:
        #         s_index -= 1
        #         p_index -= 1
        #     if p[p_index] == '.':
        #         s_index -= 1
        #         p_index -= 1
        #     if p[p_index] == '*':
        #         length = 0
        #         #   先计算出S列这个字母的长度，确定指针位置
        #         for i in range(s_index, -1, -1):
        #             if s[i] == s[s_index]:
        #                 s_index -= 1
        #                 length += 1
        #             else:
        #                 break
        #         #   额，实在是情况太多了
        if not p: return not s
        first_match = bool(s and p[0] in {s[0], '.'})
        # 如果第二个字母是 *
        if len(p) >= 2 and p[1] == "*":
            #   return 就是把P前一个数置为0 或者 s的指针往后移动一个并且P[0]和S[0]是相等的
            return self.isMatch(s, p[2:]) or \
            first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])


#   字符后面是否跟着星号会影响结果，分析起来有点复杂。所以从后往前
# 星号的前面肯定有一个字符，星号也只影响这一个字符，它就像一个拷贝器。

#   看懂了，其实挺简单的嘛










#
# print( 1 in {1, 2})
# print( 1 in [1, 2])