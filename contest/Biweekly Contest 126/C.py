import heapq
import collections
import string
def minimizeStringValue(s):
    f = collections.Counter(s)
    h = []
    for c in string.ascii_lowercase:
        heapq.heappush(h, (f[c], c))
    q = []
    ans = []
    for c in s:
        if c == "?":
            count, now = heapq.heappop(h)
            q.append(now)
            heapq.heappush(h, (count + 1, now))

    q.sort()
    q = collections.deque(q)
    for c in s:
        if c == "?":
            ans.append(q.popleft())
        else:
            ans.append(c)
    return "".join(ans)

print(minimizeStringValue("g?xvgroui??xk?zqb?da?jan?cdhtksme"))  # Output: "eqbumjlasi"