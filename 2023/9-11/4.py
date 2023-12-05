def stairs(prev_level, n):
    if n == 0:
        return 1
    cnt = 0
    for level in range(1, min(prev_level, n+1)):
        cnt += stairs(level, n - level)
    return cnt


n = int(input())
cnt = 0
for base_level in range(n // 2, n + 1):
    cnt += stairs(base_level, n - base_level)
print(cnt)
