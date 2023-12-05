# Шифровка (поиск повторяющихся подстрок длины k)

n, k = map(int, input().split())
code = input()

# используем тип "множество" для хранеия встретившихся строк
subs = set()
found = False
for i in range(n - k + 1):
    s = code[i:i+k]     # используем срез для выделения подстроки
    if s in subs:
        found = True
        break
    else:
        subs.add(s)
if found:
    print("YES")
else:
    print("NO")
