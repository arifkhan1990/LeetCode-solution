def solve(mxint, target):
    if target <= mxint:
        return 1
    if sum(range(1, mxint + 1)) < target:
        return 0
    
    memo = {}

    def can_win(remaining, visited):
        if visited in memo:
            return memo[visited]
        
        for i in range(1, mxint+1):
            mask = 1 << (i-1)

            if visited & mask == 0:
                if remaining <= i or not can_win(remaining - i, visited | mask):
                    memo[visited] = 1
                    return 1
        memo[visited] = 0
        return 0
    return can_win(target,0)

print(solve(4, 6))