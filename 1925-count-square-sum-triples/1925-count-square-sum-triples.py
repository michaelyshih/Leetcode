import math
class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1,n):
            for b in range(1,n):
                c = math.sqrt(a * a + b * b) 
                if c.is_integer() and c <= n: res += 1
        return res