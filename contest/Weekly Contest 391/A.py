def sumOfTheDigitsOfHarshadNumber(self, n: int) -> int:
    x = str(n)
    sm = sum([int(i) for i in x])
    
    if n%sm == 0:
        return sm
    return -1