n = int(input())
s = 0
for i in range(n):
    row = input().split()
    for j in range(i):
        s += int(row[j])
print(s)
