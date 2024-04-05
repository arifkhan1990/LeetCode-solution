def generate_lexicographical_numbers(n):
    result = []
    current = 1
    
    for _ in range(n):
        result.append(current)
        
        if current * 10 <= n:
            current *= 10
        elif current % 10 != 9 and current + 1 <= n:
            current += 1
        else:
            while current % 10 == 9 or current == n:
                current //= 10
            current += 1

    return result

# Example usage:
n = 10**9
lexicographical_numbers = generate_lexicographical_numbers(n)
print(lexicographical_numbers[:100])  # Print the first 100 numbers for demonstration
