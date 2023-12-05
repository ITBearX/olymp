# Лестницы - динамическое программирование

n = int(input())

stairs = (n+1) * [1]

for i in range(3, n+1):
    if i % 2 == 0:
        m = i // 2
    else:
        m = i // 2 + 1
    stairs[i] = sum(stairs[:m])

print(stairs[n])
