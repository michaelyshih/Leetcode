class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0,len(nums),2):
            res += min(nums.pop(), nums.pop())
        return res