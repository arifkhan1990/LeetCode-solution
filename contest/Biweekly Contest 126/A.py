def largest_digit(num):
    return max(int(digit) for digit in str(num))

def encrypt(x):
    largest = largest_digit(x)
    if largest == 0:
        largest = 1
    return int(str(largest) * len(str(x)))

def sum_of_encrypted(nums):
    total_sum = 0
    for num in nums:
        total_sum += encrypt(num)
    return total_sum

# Taking user input for the integer array
nums = [10,21,31]

# Calculating and printing the sum of encrypted elements
result = sum_of_encrypted(nums)
print("Sum of encrypted elements:", result)
