# Раскрасить таблицу умножения

m, n = map(int, input().split())

red, green, blue = 0, 0, 0
for i in range(1, m+1):
    for j in range(1, n+1):
        prod = i * j
        r = prod % 2 == 0
        g = prod % 3 == 0
        b = prod % 5 == 0
        blue += b
        green += (g and not b)
        red += (r and not g and not b)

black = m * n - red - green - blue

print("RED :", red)
print("GREEN :", green)
print("BLUE :", blue)
print("BLACK :", black)
