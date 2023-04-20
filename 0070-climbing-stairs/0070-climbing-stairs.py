class Solution:
    def climbStairs(self, n: int) -> int:
        if (n < 2): return n
        first, last = 1,2 
        for val in range(2,n):
            next = first + last 
            first = last 
            last = next 
        return last 