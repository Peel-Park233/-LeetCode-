class Solution:
    def letterCombinations(self, digits):
        number_str = {'2': "abc", '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        #   用递归就需要思考，传入，传出，结束条件（我习惯把结束条件放在最前面）
        ans = []
        self.temp = ''  # 递归你这个怎么处理嘛，不可能放在外面处理，只可能作为输入函数处理
        # i 表示读到第几个数字
        def change_to_str(i, digits):
            print(self.temp)
            if i == len(digits):
                ans.append(self.temp)
                self.temp = ''  # 因为这样的话，作为全局变量这里一次运行就影响到后面'ae','af'
                return
            # print(digits[i])
            # print(number_str[digits[i]])
            for k in number_str[digits[i]]:
                # print(k)
                self.temp += k
                change_to_str(i + 1, digits)
        change_to_str(0, digits)
        return ans


if __name__ == '__main__':
    digits = '23'
    # print(digits[1])
    print(Solution().letterCombinations(digits))

# 递归很典型的错误例子，更加确信了确定哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数

