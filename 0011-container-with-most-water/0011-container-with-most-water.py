class Solution:
    def maxArea(self, height: List[int]) -> int:
        end = len(height) - 1 
        start = 0 
        maxA = 0
        
        while start < end:
            limitI = 0 
            limitI = start if height[end] > height[start] else end 
            currA = height[limitI] * (end - start)
            if maxA < currA: 
                maxA = currA
            if limitI == start:
                start += 1
            else: 
                end -= 1
        
        return maxA