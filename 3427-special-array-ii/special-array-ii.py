class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        # Step 1: Create a same_parity list
        same_parity = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                same_parity[i] = 1

        # Step 2: Create a prefix sum array from the same_parity list
        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + same_parity[i - 1]

        # Step 3: Answer each query using the prefix sum array
        ans = []
        for x, y in queries:
            # Check if there are any same-parity pairs in the range [x, y-1]
            if prefix_sum[y] - prefix_sum[x] > 0:
                ans.append(False)
            else:
                ans.append(True)
        
        return ans