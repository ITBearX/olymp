from math import gcd


def np(s, e):
    return gcd(abs(s[0]-e[0]), abs(s[1]-e[1]))


data = list(map(int, input().split()))
p = list(zip(data[::2], data[1::2]))

print(np(p[0], p[1]) + np(p[1], p[2]) + np(p[2], p[0]))
