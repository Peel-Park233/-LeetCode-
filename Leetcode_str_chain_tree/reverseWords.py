#   题目描述：翻转字符串里的单词
# 给定一个字符串，逐个翻转字符串中的每个单词。
#   字符串操作，满满的细节
class Solution:
    def reverseWords(self, s):
        if s == '':
            return ''
        str_1 = s
        str_1 = str_1.strip()  # 去掉str_1前后的空格
        # print(str_1.split(" ", -1))
        str_1 = str_1.split(' ', -1)  # 根据空格(" ")对字符串进行划分

        # str_2 = reversed(str_1)       # 对字符串进行反转
        str_2 = str_1[::-1]             #  对字符串进行反转而且之后不用list
        # print(list(str_2))
        str_2 = list(str_2)         # 将字符串列表化，这样才能print
        str_2 =' '.join(str_2)      # 用空格将字符串连起来
        return str_2


if __name__ == '__main__':
    s = "the sky is blue"
    print(Solution().reverseWords(s))
#   由于 split()split() 方法将单词间的 “多个空格看作一个空格”
# 因此不会出现多余的 “空单词” 。因此，直接利用 reverse()reverse()
# 方法翻转单词列表 strsstrs ，拼接为字符串并返回即可。