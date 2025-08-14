def generate_stable_arrays(zero, one, limit):
    def backtrack(arr, zeros, ones):
        if len(arr) > 1 and len(arr) - 1 >= limit:
            subarray = arr[-(limit + 1):]
            if subarray.count(0) > limit or subarray.count(1) > limit:
                return
            if zeros > limit or ones > limit:
                return

        if zeros == 0 and ones == 0:
            yield arr

        if zeros > 0:
            yield from backtrack(arr + [0], zeros - 1, ones)

        if ones > 0:
            yield from backtrack(arr + [1], zeros, ones - 1)

    yield from backtrack([], zero, one)

# Example usage:
zero = 3
one = 3
limit = 2
result = list(generate_stable_arrays(zero, one, limit))
print(result)
