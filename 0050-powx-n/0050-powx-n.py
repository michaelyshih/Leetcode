class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case, to stop recursive calls.
        if n == 0:
            return 1
       
        # Handle case where, n < 0.
        if n < 0:
            return 1.0 / self.myPow(x, -1 * n)
       
        # Perform Binary Exponentiation.
        # If 'n' is odd we perform Binary Exponentiation on 'n - 1' and multiply result with 'x'.
        if n % 2 == 1:
            return x * self.myPow(x * x, (n - 1) // 2)
        # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
        else:
            return self.myPow(x * x, n // 2)

        # if n  == 0: return float(1)
        # if n < 0: 
        #     x = 1/x
        #     n = abs(n)
        # base = x
        # for i in range(1,n):
        #     x *= base
        # return x
        