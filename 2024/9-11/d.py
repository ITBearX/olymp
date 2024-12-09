def is_smart(n):
    if int(n**0.5) ** 2 == n:
        return False
    d, m = 0, 2
    while n > 1 and m*m < n:
        if n % m == 0:
            if d == 0:
                d = m
                n //= d
                if d == n:
                    return False
            else:
                return False
        else:
            m += 1
    return d > 0


for i in range(1, 6):
    filename = f"d-input-{i}.txt"
    with open(filename) as f:
        f.readline()
        print(sum(is_smart(int(s)) for s in f))
