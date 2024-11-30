hour, min, passed = map(int, input().split())

pd = passed // 720
ph = (passed % 720) // 60
pm = passed % 60
bells = pd * 114 + ph * (2*hour + ph + 1) // 2 + ph * 3
if min + pm >= 60:
    bells += hour + ph + pm // 15
else:
    bells += pm // 15
print(bells)
