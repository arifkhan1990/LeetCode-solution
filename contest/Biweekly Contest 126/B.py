import heapq

def sum_of_unmarked(nums, queries):
        N = len(nums)
        
        total = sum(nums)
        h = []
        marked = [False] * N
        
        for index, x in enumerate(nums):
            heapq.heappush(h, (x, index))
            
        ans = []
        
        for i, k in queries:
            if not marked[i]:
                total -= nums[i]
                marked[i] = True
            
            while k > 0 and len(h) > 0:
                x, index = heapq.heappop(h)
                
                if not marked[index]:
                    k -= 1
                    marked[index] = True
                    total -= x
            ans.append(total)
        return ans


# Example usage:
nums = [15,15,20,15,14,14,13,17,13,14,1,15,15,14,18,1,16,4,9,20]
queries = [[11,3],[10,4],[12,4],[18,4],[9,2],[16,4],[9,3],[15,1],[13,4],[17,1],[8,2],[0,2],[4,1],[14,0],[19,1]]
print(sum_of_unmarked(nums, queries))  # Output: [242, 193, 121, 58, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

