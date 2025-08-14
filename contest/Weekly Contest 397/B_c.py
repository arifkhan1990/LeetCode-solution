energy1 = [5, 2, -10, -5, 1,9, -3]
k = 3

result = []
for i in range(0, len(energy1), k):
    subarray = energy1[i:i+k]
    if len(subarray) == k:
        result.append(tuple(subarray))

print(result)