def generate_stable_arrays(zero, one, limit):
    def backtrack(arr, remaining_zeros, remaining_ones):
        nonlocal count
        if len(arr) > 1 and (len(arr) - 1) >= limit:
            subarray = arr[-(limit + 1):]
            if subarray.count(0) > limit or subarray.count(1) > limit:
                return

        if remaining_zeros == 0 and remaining_ones == 0:
            count += 1
            return

        if remaining_zeros > 0:
            backtrack(arr + [0], remaining_zeros - 1, remaining_ones)

        if remaining_ones > 0:
            backtrack(arr + [1], remaining_zeros, remaining_ones - 1)

    count = 0
    backtrack([], zero, one)
    return count

# Example usage:
zero = 14
one = 13
limit = 59
result = generate_stable_arrays(zero, one, limit)
print(result)
