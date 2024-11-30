from math import gcd, lcm


a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b < 0:
    a = -a
if d < 0:
    b = -b

den = lcm(b, d)
num = a * den // b + c * den // d

if den % num == 0:
    k = gcd(num, den)
    num = num // k
    den = den // k

print(num, den)
