import math
def lastRemaining(n):
    remaining = n
    start = 1
    step = 2
    direction = 1

    while remaining > 1:
        if direction == 1 or remaining % 2 == 1:
            start += step // 2
        step *= 2
        remaining //= 2
        direction *= -1

    return start

n = 9
print(lastRemaining(n))