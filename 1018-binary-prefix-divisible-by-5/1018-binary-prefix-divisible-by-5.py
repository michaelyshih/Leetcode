class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        currBinary, result = 0, []
        for bit in nums:
            currBinary = (currBinary * 2 + bit) % 5 
            result.append(currBinary == 0)
        return result