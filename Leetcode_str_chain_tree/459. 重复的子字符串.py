class Solution:
    def repeatedSubstringPattern(self, s: str):
        # 重复子字符串的最大长度
        m = len(s)//2
        #  先把可能的长度都放在一起，节约时间，也利于滑动窗口最后一部分长度不一致的问题
        possible_len = []
        for i in range(1, m+1):
            if len(s) % i == 0:
                possible_len.append(i)
        # 滑动窗口来做
        for i in possible_len:  # 遍历这些长度
            temp = s[:i]  # 因为左闭右开
            for k in range(i, len(s)-i+1, i):
                if s[k:k+i] != temp:
                    break
                if k == len(s) - i:
                    return True
        return False


s = "abab"
print(Solution().repeatedSubstringPattern(s))