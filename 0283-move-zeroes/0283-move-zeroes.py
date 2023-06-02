class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNoneZero = 0 
        while  lastNoneZero < len(nums) and not nums[lastNoneZero] == 0:
            lastNoneZero += 1 
        
        for i in range(lastNoneZero + 1,len(nums)):
            if not nums[i] == 0: 
                nums[lastNoneZero], nums[i] = nums[i], nums[lastNoneZero]
                lastNoneZero+=1
        return nums
        