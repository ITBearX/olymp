n, m = map(int, input().split())
matr = [[0]*m for _ in range(n)]

top, bottom = 1, n-1
left, right = 0, m-1
r, c, dr, dc = 0, 0, 0, 1

for cnt in range(1, n * m + 1):
    matr[r][c] = cnt
    turn = True
    if dc == 1 and c >= right:
        right -= 1
    elif dc == -1 and c <= left:
        left += 1
    elif dr == 1 and r >= bottom:
        bottom -= 1
    elif dr == -1 and r <= top:
        top += 1
    else:
        turn = False
    if turn:
        dr, dc = dc, -dr
    r += dr
    c += dc 

for row in matr:
    for item in row:
        print(item, end="\t")
    print()
