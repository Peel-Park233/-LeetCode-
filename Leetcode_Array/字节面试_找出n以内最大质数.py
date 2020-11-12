def solve(n):
    if n < 0:
        print("不存在")
    if n <= 2:
        print(n)
    for i in range(n, 2, -1):
        ans = 1
        for j in range(2, i):
            if i % j == 0:
                ans = 0
                break
        if ans == 1:
            print(i)
            break

solve(100)
