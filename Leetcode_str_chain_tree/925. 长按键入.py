def demo_1027():
    a = 0
    b = 10
    while a < b:
        a += 2
        b += 1
        if a > 5:
            return a    # 能跳出while和def
    return a, b


print(demo_1027())


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        #   双指针法，简简单单
        if not name or not typed:
            return False
        if name[0] != typed[0]:
            return False
        type1 = 0   # 指向name
        type2 = 0   # 指向type
        m = len(name)
        n = len(typed)
        # name = name.ljust(n,'0')
        name = name + '0'
        # print(name)
        while type1 < m+1 and type2 < n:
            if name[type1] == typed[type2]:
                type1 += 1
                type2 += 1

            elif name[type1-1] == typed[type2]:
                 type2 += 1

            else:
                return False
        # print(type1, type2)
        if type1 == m and type2 == n:
            return True
        else:
            return False