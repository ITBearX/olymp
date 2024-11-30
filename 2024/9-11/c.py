opening = ["(", "[", "{"]
closing = [")", "]", "}"]


def balance(s):
    stack = []
    for ch in s:
        if ch in opening:
            stack.append(ch)
        elif ch in closing:
            i = closing.index(ch)
            if len(stack) == 0:
                return False
            if stack.pop() != opening[i]:
                return False
    return len(stack) == 0


with open("c-input.txt") as f:
    f.readline()
    print(sum(balance(s) for s in f))
