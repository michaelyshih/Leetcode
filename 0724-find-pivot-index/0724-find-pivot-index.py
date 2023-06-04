class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightTotal = sum(nums)
        leftTotal = 0
        for i, num in enumerate(nums):
            rightTotal -= num
            if leftTotal == rightTotal:
                return i 
            leftTotal += num
        return -1