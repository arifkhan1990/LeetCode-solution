def findNthDigit(n):
    l, cnt , s = 1, 9, 1
    while n > l * cnt:
        n -= l * cnt
        l += 1
        cnt *= 10
        s *= 10
    s += (n-1)//l
    return int(str(s)[(n -1) % l])

print(findNthDigit(11))