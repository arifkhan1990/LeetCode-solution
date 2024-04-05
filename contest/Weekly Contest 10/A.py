def solve(mat):
    ans = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                ans += 4
                if i > 0 and mat[i-1][j] == 1:  # Check top neighbor
                    ans -= 2
                if j > 0 and mat[i][j-1] == 1:  # Check left neighbor
                    ans -= 2
    return ans 

print(solve([[1,0]]))