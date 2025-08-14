def minScorePerm(nums):
    n = len(nums)
    min_perm = list(range(n))
    min_score = float('inf')
    
    # Function to calculate the score of a permutation
    def calculate_score(perm):
        score = 0
        for i in range(n):
            score += abs(perm[i] - nums[perm[(i + 1) % n]])
        return score
    
    # Recursive function to generate permutations
    def dfs(perm, score):
        nonlocal min_score, min_perm
        
        # Base case: If all elements are placed in the permutation
        if len(perm) == n:
            if score < min_score:
                min_score = score
                min_perm = perm[:]
            return
        
        # Try placing each remaining element at the current position
        for i in range(n):
            if i not in perm:
                next_perm = perm + [i]
                next_score = score + abs(perm[-1] - nums[i]) if perm else 0
                dfs(next_perm, next_score)  # Update score calculation
    
    # Start DFS with an initial permutation containing 0
    dfs([0], 0)
    
    return min_perm


# Test cases
print(minScorePerm([1, 0, 2]))  # Expected output: [0, 1, 2]
print(minScorePerm([0, 2, 1]))  # Expected output: [0, 2, 1]
print(minScorePerm([1, 3, 2, 0]))  # Expected output: [0, 3, 1, 2]
print(minScorePerm([2, 0, 1]))  # Expected output:
