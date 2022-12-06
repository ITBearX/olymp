n = int(input())
min_w, max_w = 100_000, 0
for i in range(n):
    wage = int(input())
    if wage < min_w:
        min_w = wage
    if wage > max_w:
        max_w = wage
print(max_w - min_w)
