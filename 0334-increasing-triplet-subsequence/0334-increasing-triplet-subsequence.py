class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i,j = float("inf"), float("inf")
        for idx in range(len(nums)):
            if nums[idx] <= i: 
                i = nums[idx]
            elif nums[idx] <= j:
                j = nums[idx]
            else: 
                return True
                
        return False 