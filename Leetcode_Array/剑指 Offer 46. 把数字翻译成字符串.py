class solution():

    def translateNum(self, num):
        dic = {i: chr(i) for i in range(26)}
        self.ans = 0
        snum = str(num)

        def translate(snum):
            if len(snum)==0:    # 说明递归结束了
                self.ans += 1
                # print('+1')
                return
            if int(snum[0]) in dic.keys():
                # print('一个')
                translate(snum[1:])
            if len(snum) > 1:
                if int(snum[0: 2]) in dic.keys():
                    # print('两个')
                    translate(snum[2:])
        translate(snum)

        return self.ans

# 一个python文件通常有两种使用方法，第一是作为脚本直接执行，第二是 import 到其他的 python 脚本中被调用（模块重用）执行。
# 因此 if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，在 if __name__ == 'main': 下的代码只有在第一种情况下
# （即文件作为脚本直接执行）才会被执行，而 import 到其他脚本中是不会被执行的。


if __name__ == "__main__":
    print(solution().translateNum(205))

# print(chr(3))