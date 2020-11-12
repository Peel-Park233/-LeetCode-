# 题目描述:
#   爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
# 只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 False

#   如果真的做不出来， 就1， 2， 3， 4这样代入看看有什么规律，突然发现有点想海盗分金的题，从后往前做


class Solution:
    def divisorGame(self, N):
        if N < 2:
            return False  # 如果是1， 爱丽丝无法操作所以是false
        if N % 2 == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().divisorGame(7))


#   要点:   N是奇数，N-X一定是偶数，N是偶数，N-X可以是奇数也可以是偶数，
#  给别人奇数，自己就一定能得到偶数，所以要一直给别人奇数，最后一定是自己得到2，然后对面就输了。

