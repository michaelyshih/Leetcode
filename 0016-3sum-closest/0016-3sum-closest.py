class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float("inf")
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue 
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if abs(threeSum - target) < abs(closest - target): 
                        closest = threeSum 
                
                if threeSum == target: 
                    return threeSum 
                elif threeSum > target:
                    r -= 1
                else:
                    l += 1
                    while nums[l] == nums[l-1] and l < r: 
                        l += 1
                    
        return closest 