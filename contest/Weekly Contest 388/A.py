def min_boxes(apple, capacity):
    sm = sum(apple)
    capacity.sort()
    ans = 0
    for i in range(len(capacity)-1, -1, -1):
        if sm > 0:
            sm -= capacity[i]
            ans += 1
        else:
            break
    return ans

# Example usage
apple = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
print(min_boxes(apple, capacity))  # Output: 2

apple = [5, 5, 5]
capacity = [2, 4, 2, 7]
print(min_boxes(apple, capacity))  # Output: 4
