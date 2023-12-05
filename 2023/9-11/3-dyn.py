heads = int(input())

power = (heads + 1) * [1]
power[2] = 2
power[3] = 3

for i in range(4, heads+1):
    power[i] = max(power[i-2] * 2, power[i-3] * 3)

print(power[heads])
