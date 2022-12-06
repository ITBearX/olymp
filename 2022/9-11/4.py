def vect_prod(s1, e1, s2, e2):
    x1 = e1[0] - s1[0]
    x2 = e2[0] - s2[0]
    y1 = e1[1] - s1[1]
    y2 = e2[1] - s2[1]
    return x1 * y2 - y1 * x2


s1, e1, s2, e2 = (tuple(int(s) for s in input().split()) for _ in range(4))
vp1 = vect_prod(s1, e1, s1, s2) 
vp2 = vect_prod(s1, e1, s1, e2) 
vp3 = vect_prod(s2, e2, s2, s1)
vp4 = vect_prod(s2, e2, s2, e1)
if vp1 * vp2 > 0 or vp3 * vp4 > 0:
    if vp1 == 0 and vp2 != 0 or vp1 != 0 and vp2 == 0:
        print("Yes")
    elif s1 == s2 or s1 == e2 or e1 == s2 or e1 == e2:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")
