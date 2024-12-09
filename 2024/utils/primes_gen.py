from random import uniform, choice, randint


NUM = 500
SMART = 0.35
PRIME = 0.05
SQR = 0.4
MIN, MAX = 1, 100_000_000

with open("primes_table.txt") as pf:
    primes = []
    for line in pf:
        primes += [int(word) for word in line.split()]
primes.sort()


src = primes
filename = input("Имя файла: ")
with open(filename, "w") as f:
    f.write(str(NUM) + "\n")
    cnt = 0
    for _ in range(NUM):
        coin = uniform(0, 1)
        if coin <= SMART:
            cnt += 1
            ok = False
            while not ok:
                a, b = choice(src), choice(src)
                n = a * b
                ok = a != b
        elif coin <= SMART + PRIME:
            n = choice(src)
        elif coin <= SMART + PRIME + SQR:
            n = choice(src) ** 2
        else:
            n = randint(MIN, MAX)
        f.write(str(n) + "\n")
    print(f"Хитрых {cnt}")
