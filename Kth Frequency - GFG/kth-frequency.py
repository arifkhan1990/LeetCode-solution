from collections import Counter
for _ in range(int(input())):
    n , k = map(int, input().split())
    ar = list(map(int, input().split()))
    count = Counter(ar)
    ans = []
    for i in count:
        if count[i] > k:
            ans.append(i)
    if ans == []:
        print(-1)
    else:
        print(*ans)