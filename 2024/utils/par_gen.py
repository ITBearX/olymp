from random import randint, choice, uniform
from string import ascii_letters


NUM_LINES = 10000
CORRECT = 0.25
MIN_LEN, MAX_LEN = 1000, 5000
DENSITY = 0.2

opening = ["(", "[", "{"]
closing = [")", "]", "}"]
# opening = ["("]
# closing = [")"]


def coin(param):
    return uniform(0, 1) <= param


def gen_string(correct=True):
    stack = []
    s = ""
    size = randint(MIN_LEN, MAX_LEN)
    for _ in range(size):
        if coin(DENSITY):
            if correct:
                if coin(0.5) and len(stack) > 0:
                    ch = closing[opening.index(stack.pop())]
                else:
                    ch = choice(opening)
                    stack.append(ch)
            else:
                ch = choice(opening+closing)
        else:
            ch = choice(ascii_letters)
        s += ch
    if len(stack) > 0:
        for ch in stack[::-1]:
            s += closing[opening.index(ch)]
    return s + "\n"


filename = input("Имя файла: ")
with open(filename, "w") as f:
    f.write(str(NUM_LINES) + "\n")
    for nline in range(NUM_LINES):
        f.write(gen_string(coin(CORRECT)))
