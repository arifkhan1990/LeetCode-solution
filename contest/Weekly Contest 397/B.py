def max_energy(energy, k):
    n = len(energy)
    max_energy = float('-inf')
    
    for i in range(n):
        window_sum = 0
        j = i
        while j < n:
            window_sum += energy[j]
            j += k
        max_energy = max(max_energy, window_sum)
    
    return max_energy

# Example usage:
energy1 = [5, 2, -10, -5, 1]
k1 = 3
print(max_energy(energy1, k1))  # Output: 3

energy2 = [-2, -3, -1]
k2 = 2
print(max_energy(energy2, k2))  # Output: -1
