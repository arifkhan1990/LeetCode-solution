def solve(s, k):
    stack = []

    for d in s:
        while k > 0 and stack and stack[-1] > d:
            stack.pop()
            k -= 1
        stack.append(d)

    while k > 0:
        stack.pop()
        k -= 1

    while stack and stack[0] == '0':
        stack.pop(0)

    return '0' if not stack else ''.join(stack)

print(solve("10200", 1))
    