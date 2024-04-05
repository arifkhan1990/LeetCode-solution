def solve(data):
    cnt = 0
    for b in data:
        if cnt == 0:
            if b >> 5 == 0b110:
                cnt = 1
            elif b >> 4 == 0b1110:
                cnt = 2
            elif b >> 3 == 0b11110:
                cnt = 3
            elif b >> 7:
                return False
        else:
            if b >> 6 != 0b10:
                return False
            cnt -= 1
    return cnt == 0

# Test cases
print(solve([197,130,1]))  # Output: True
print(solve([235,140,4]))  # Output: False