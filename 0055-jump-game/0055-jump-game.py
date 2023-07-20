class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums)- 1
        dp = {}
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= end:
                end = i 
        return end == 0 
                