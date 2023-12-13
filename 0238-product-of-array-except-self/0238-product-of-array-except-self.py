class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]* (len(nums))
        
        prefix = 1 
#         first pass through to add all the prefix products into the res
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        postfix = 1 
#         second pass through on the pre-existing prefix to multiply it to the postfix product
        for i in range (len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res