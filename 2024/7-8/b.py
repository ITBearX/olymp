fields = [input() for _ in range(2)]
x = [ord(f[0]) - ord("A") + 1 for f in fields]
y = [int(f[1]) for f in fields]
if any(c < 1 or c > 8 for c in x + y):
    print(3)
elif abs(x[0]-x[1]) == abs(y[0]-y[1]):
    print(1)
else:
    print(2)
