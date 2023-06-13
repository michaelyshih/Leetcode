class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ones, longest, run = 0, nums[0], 0
        for i in  range(1, len(nums)):
            run = nums[i] * max(run + 1, ones + 1)
            ones = nums[i-1] * (ones +1)
            longest = max(longest,run)
        return longest