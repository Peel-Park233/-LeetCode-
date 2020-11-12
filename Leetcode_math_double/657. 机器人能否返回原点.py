class Solution:
    def judgeCircle(self, moves: str):
        m = len(moves)
        right = 0
        left = 0
        up = 0
        down = 0
        for i in moves:
            if i == 'R':
                right += 1
            elif i == 'L':
                left += 1
            elif i == 'U':
                up += 1
            elif i == 'd':
                down += 1
        if right == left and up == down:
            return True
        else:
            return False
