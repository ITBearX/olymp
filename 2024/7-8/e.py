with open("e-input.txt") as f:
    f.readline()
    cnt = 0
    for s in f:
        balance = 0
        for ch in s:
            if ch == "(":
                balance += 1
            elif ch == ")":
                balance -= 1
            if balance < 0:
                break
        if balance == 0:
            cnt += 1
    print(cnt)
