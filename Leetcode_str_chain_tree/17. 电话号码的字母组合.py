class Solution:
    def letterCombinations(self, digits: str):
        number_str = {'2': "abc", '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        #   用递归就需要思考，传入，传出，结束条件（我习惯把结束条件放在最前面）
        ans = []

        # i 表示读到第几个数字
        def change_to_str(i, possible):  # 传入的值是需要改变的值

            if i == len(digits):
                ans.append(possible)
                return
            print(digits[i])
            # print(number_str[digits[i]])
            for k in number_str[digits[i]]:
                change_to_str(i + 1, possible + k)
        change_to_str(0, '')
        return ans


