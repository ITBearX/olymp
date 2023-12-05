# Проредить аллею - по формуле суммы прогрессии

n, m = map(int, input().split())

if m <= n:
    if m > 0:
        max_d = (n - m) // (m - 1) if m > 1 else 0
        w = int((max_d - max_d * m) * ((max_d + 1) / 2))
        w += (n - m + 1) * (max_d + 1)
    else:
        w = 1
else:
    w = 0

print(w)
