class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        prof = 0 
        for i,num in enumerate(prices):
            if num < low: low = num 
            diff = num - low 
            if diff > prof: prof = diff 
        return prof
            
            