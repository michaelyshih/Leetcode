class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        M = [[0 for _ in range(n)] for _ in range(m)]
        for ri, ci in indices:
            M[ri] = [v + 1 for v in M[ri]]
            for i in range(m):
                M[i][ci] += 1
        return len([M[i][j] for i in range(m) for j in range(n) if M[i][j] % 2 == 1])