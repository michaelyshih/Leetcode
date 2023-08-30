class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        l = []
        i = 0
        while i < len(nums):
            first = i
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            if i == first:
                l.append(str(nums[first]))
            else:
                l.append(str(nums[first]) + "->" + str(nums[i]))
            i += 1
        
        return l