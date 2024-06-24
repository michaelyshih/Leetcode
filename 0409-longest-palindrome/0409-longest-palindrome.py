class Solution:
    def longestPalindrome(self, s: str) -> int:
        # start count at 1 since 1 is valid
        n = 0
        freq_map = {}
        
        for c in s: 
            freq_map[c] = freq_map.get(c,0) + 1 
            
            n = n + 1 if freq_map[c] % 2 == 1 else n - 1
        
        return len(s) - n + 1 if n > 0 else len(s)