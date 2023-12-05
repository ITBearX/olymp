def power(heads):
    if heads <= 3:
        return heads
    return max(
        power(heads-2) * 2,
        power(heads-3) * 3
    )


h = int(input())
print(power(h))
