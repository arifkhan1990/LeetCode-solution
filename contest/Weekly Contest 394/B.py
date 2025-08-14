def count_special_letters(word):
    sm = {chr(i): -1 for i in range(ord('a'), ord('z') + 1)}
    la = {chr(i): -1 for i in range(ord('A'), ord('Z') + 1)}
    ans = 0
    for x, i in enumerate(word):
        print(x, i)
        if i >= 'a' and i <= 'z':
            sm[i] = x if sm[i] == -1 else max(sm[i],x)
        else:
            la[i] = x if la[i] == -1 else min(la[i],x)
    print(sm, la, sm.items())
    data = set()
    for ch in word:
        if ch.islower() and ch not in data:
            data.add(ch)
            data.add(ch.upper())
            print(ch,ch.upper(), sm[ch] , la[ch.upper()])
            if sm[ch] > -1 and la[ch.upper()] > -1:
                if sm[ch] < la[ch.upper()]:
                    ans += 1
        elif ch.isupper() and ch not in data:
            data.add(ch)
            data.add(ch.lower())
            print(ch,ch.lower(), sm[ch.lower()] , la[ch])
            if sm[ch.lower()] > -1 and la[ch] > -1:
                if sm[ch.lower()] < la[ch]:
                    ans += 1
    return ans

# Example usage:
word1 = "aaAbcBC"
word2 = "abcXx"
word3 = "EAdEecD"
word4 = "eEb"
word4 = "cDCbc"
print(count_special_letters(word1))  # Output: 3
print(count_special_letters(word3))  # Output: 0
# print(count_special_letters(word3))  # Output: 0

