n = int(input())

m = 2
while m * m <= n:
    if n % m == 0:
        n //= m
        print(m, end="*")
    else:
        m += 1
print(n)
