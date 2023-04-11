class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
# same color are adjacent red 0 , white 1 , blue 2
        counts = [0] * 3    
        for num in nums:
            counts[num] += 1
        i = 0
        for freq in range(len(counts)):
            for c in range(counts[freq]):
                nums[i] = freq
                i += 1
            