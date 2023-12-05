# Драконы - "хитрое" решение

heads = int(input())

power = 3 ** (heads // 3)
if heads % 3 == 1:
    power = power * 4 // 3
elif heads % 3 == 2:
    power = power * 2

print(power)
