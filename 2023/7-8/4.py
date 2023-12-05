# Ход коня

s = input()

if len(s) != 5 or s[2] != "-":
    print("ERROR")
else:
    v1 = ord(s[0]) - ord("A") + 1
    v2 = ord(s[3]) - ord("A") + 1
    h1 = ord(s[1]) - ord("0")
    h2 = ord(s[4]) - ord("0")
    if 1 <= h1 <= 8 and 1 <= v1 <= 8 and 1 <= h2 <= 8 and 1 <= v2 <= 8:
        dh = abs(h1 - h2)
        dv = abs(v1 - v2)
        if dh == 1 and dv == 2 or dh == 2 and dv == 1:
            print("YES")
        else:
            print("NO")
    else:
        print("ERROR")
