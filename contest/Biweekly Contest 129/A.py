def count_B_in_2x2(matrix, ch):
    count_list = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            submatrix = [row[j:j+2] for row in matrix[i:i+2]]
            count = sum(row.count(ch) for row in submatrix)
            if count > 2:
                return 1
    return 0

matrix = [["W","W","B"],["W","B","B"],["B","B","B"]]
print(1 if count_B_in_2x2(matrix, 'B') == 1 or  count_B_in_2x2(matrix, 'W') == 1 else 0)
