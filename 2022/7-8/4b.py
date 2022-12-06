from time import perf_counter_ns

m, n = map(int, input().split())

start = perf_counter_ns()

sieve = [True]*(n+1)
sieve[1] = False

for num in range(2, int(n**0.5)+1):
    if sieve[num]:
        for mul in range(num*2, n+1, num):
            sieve[mul] = False

primes = list(filter(lambda x: sieve[x], range(m, n+1)))
if len(primes) == 0:
    print("Absent")
else:
    for num in primes:
        print(num)

end = perf_counter_ns()
print((end-start) / 1e3, "us")
