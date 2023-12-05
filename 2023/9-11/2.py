n, k = map(int, input().split())
code = input()

subs = set()
found = False
for i in range(n - k + 1):
    s = code[i:i+k]
    if s in subs:
        found = True
        break
    else:
        subs.add(s)
if found:
    print("YES")
else:
    print("NO")
