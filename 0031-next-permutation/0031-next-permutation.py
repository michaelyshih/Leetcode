class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if(n==1): return
        
        i = 1 
        lstInc = -1 
        while i < n:
            if nums[i] > nums[i-1]:
                lstInc = i
            i+=1
        
        if lstInc == -1:
            for i in range(n//2):
                nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
            return
        
        mn = nums[lstInc]
        index = lstInc
        for i in range(lstInc,n):
            if nums[i] > nums[lstInc-1] and nums[i] < nums[index]:
                index = i
                
        nums[lstInc-1],nums[index] = nums[index], nums[lstInc-1]
        nums[lstInc:] = sorted(nums[lstInc:])