class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return map(lambda x: nums[x], nums)