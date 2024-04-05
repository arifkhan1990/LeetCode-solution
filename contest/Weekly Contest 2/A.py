def findTheDifference(s, t):
    s = sorted(s)
    t = sorted(t)
    
    for i in range(len(s)):
        if s[i] !=  t[i]:
            return t[i]
    return t[len(s)]

s = "a"
t = "aa"
print(findTheDifference(s, t))