def is_smart(n):
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


with open("d-input.txt") as f:
    f.readline()
    print(sum(is_smart(int(s)) for s in f))
