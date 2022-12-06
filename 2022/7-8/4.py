from time import perf_counter_ns

m, n = map(int, input().split())

start = perf_counter_ns()

primes = [2]
result = [2] if m <= 2 else []

for num in range(3, n+1, 2):
    is_prime = True
    for div in primes:
        if div * div > num:
            break
        if num % div == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
        if num >= m:
            result.append(num)

if result == []:
    print("Absent")
else:
    for num in result:
        print(num)

end = perf_counter_ns()
print((end-start) / 1e3, "us")
