class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0 
        for i in range(k):
            total += nums[i]
        maxSum = total 
        
        s,e = 0,k
        
        while e < len(nums):
            total -= nums[s]
            s+= 1
            
            total += nums[e]
            e+=1
            
            maxSum = max(maxSum, total)
            
        return maxSum / k
        
        
#         l,r = 0, 0
#         currSum = nums[r]
#         maxSum = 0
        
#         if len(nums) <= k:
#             return sum(nums) / k
#         while r < k -1: 
#             r += 1 
#             currSum += nums[r]
            
#         maxSum = currSum
        
#         while r < len(nums) - 1:
#             r += 1 
#             currSum += nums[r]
#             currSum -= nums[l]
#             l += 1 
#             maxSum = max(maxSum, currSum)
            
#         return maxSum / k

