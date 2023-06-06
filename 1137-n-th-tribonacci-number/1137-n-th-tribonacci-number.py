class Solution:
    def tribonacci(self, n: int) -> int:
#         if n == 0: return 0
#         res = [0,1,1]
#         while len(res) <= n:
#             res.append(sum(res[(len(res))-3:]))
        
#         return res[-1]
        t = [0,1,1]
        if n < 3: 
            return t[n]
        for i in range(3, n+1):
            t[0], t[1],t[2] = t[1],t[2], sum(t)
        return t[2]