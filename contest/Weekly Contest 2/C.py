# Define the message
message = "MY FAVOURITE HOBBY IS GARDENING"

# Remove spaces and convert to uppercase
# message = message.replace(" ", "").upper()

# Define the matrix A
A = [[1, -1, 1],
     [1, 1, 0],
     [1, 2, 1]]

# Function to perform matrix multiplication
def matrix_multiply(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            val = 0
            for k in range(len(B)):
                val += A[i][k] * B[k][j]
            row.append(val)
        result.append(row)
    return result

# Convert the message to a matrix of numbers
message_matrix = [[ord(char) - 65 for char in message]]

# Pad the message with zeros if needed
remainder = len(message_matrix[0]) % 3
if remainder != 0:
    padding = 3 - remainder
    message_matrix[0].extend([0] * padding)

# Reshape the message matrix to match the dimensions of A
rows = len(message_matrix[0]) // 3
message_matrix = [message_matrix[0][i:i+3] for i in range(0, len(message_matrix[0]), 3)]

# Encode the message by multiplying with matrix A
encoded_message_matrix = matrix_multiply(message_matrix, A)
for x in encoded_message_matrix:
    print(x)
# print(encoded_message_matrix)
# Convert the encoded message matrix back to characters
# encoded_message = ''.join([chr(int(num) + 65) for sublist in encoded_message_matrix for num in sublist])

# print("Encoded Message:", encoded_message)
