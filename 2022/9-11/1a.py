n = int(input())

m = 2
while n > 1:
    if n % m == 0:
        n //= m
        print(m, end="*" if n > 1 else "\n")
    else:
        m += 1
