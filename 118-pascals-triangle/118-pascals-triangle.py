class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tr = []*numRows

        for i in range(0, numRows):
            t = []*i
            for j in range(i+1):
                if j == 0 or j == i:
                    t.append(1)
                else:
                    t.append(tr[i-1][j-1] + tr[i-1][j])
            tr.append(t)
        return tr