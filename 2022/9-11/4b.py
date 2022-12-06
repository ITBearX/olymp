def is_par(s1, e1, s2, e2):
    x1 = e1[0] - s1[0]
    x2 = e2[0] - s2[0]
    y1 = e1[1] - s1[1]
    y2 = e2[1] - s2[1]
    if x1 != 0 and x2 != 0:
        return y1 / x1 == y2 / x2
    if x1 == 0 and x2 == 0:
        return True
    return False


s1, e1, s2, e2 = (tuple(int(s) for s in input().split()) for _ in range(4))
if is_par(s1, e2, s2, e1):
    print("Yes")
else:
    print("No")
