class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        h = {chr(i+ ord("A") - 1):i for i in range(1,27)}
        print(ord("A"))
        s = columnTitle
        n = len(s)
        
        ans = 0 
        mult = 1
        for i in range( n-1, -1, -1):
            ans += h[s[i]] * mult
            mult *= 26
        
        return ans