# Шифровка (поиск повторяющихся подстрок длины k)
# Решение с использованием булевского массива

n, k = map(int, input().split())
code = input()

subs = (10 ** k) * [False]
found = False
for i in range(n - k + 1):
    s = int(code[i:i+k])
    found = subs[s]
    if found:
        break
    subs[s] = True

print("YES" if found else "NO")
