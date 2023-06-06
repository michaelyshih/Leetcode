class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        res = [0,1,1]
        while len(res) <= n:
            res.append(sum(res[(len(res))-3:]))
        
        return res[-1]
        