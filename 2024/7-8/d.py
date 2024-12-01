from math import gcd


a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b < 0:
    a = -a
if d < 0:
    c = -c

num = a * d + c * b
den = b * d

k = gcd(num, den)
num //= k
den //= k

print(num, den)
