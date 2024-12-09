h, m, n = map(int, input().split())

chimes = (n // 720) * 114
for _ in range(1, n % 720 + 1):
    m += 1
    if m == 60:
        m = 0
        h += 1
        chimes += h
        if h == 12:
            h = 0
    elif m % 15 == 0:
        chimes += 1
print(chimes)
