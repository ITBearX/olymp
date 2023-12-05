def sum_digits(a):
    s = 0
    while a > 0:
        s += a % 10
        a //= 10
    return s


def comp(a, b, sum_b):
    sum_a = sum_digits(a)
    if sum_a > sum_b:
        return sum_a
    if sum_a == sum_b:
        return a < b
    return 0


n = int(input())
best_val, best_sum = 0, 0
d = 1
while d * d <= n:
    if n % d == 0:
        m = n // d
        result = comp(d, best_val, best_sum)
        if result > 0:
            best_val = d
            best_sum = result
        result = comp(m, best_val, best_sum)
        if result > 0:
            best_val = m
            best_sum = result
    d += 1

print(best_val)
