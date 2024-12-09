from math import gcd


a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b < 0:
    a, b = -a, -b
if d < 0:
    c, d = -c, -d

num = a * d + c * b
den = b * d

k = gcd(num, den)
num //= k
den //= k

print(num, den)
