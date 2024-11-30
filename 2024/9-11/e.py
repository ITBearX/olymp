a, b = map(int, input().split())
d = ((a % 10) ** ((b - 1) % 4 + 1)) % 10 if b > 0 else 1
print(d)
