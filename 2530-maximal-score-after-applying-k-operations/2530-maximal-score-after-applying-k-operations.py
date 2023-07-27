import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        res = 0 
        for i in range(k):
            high = nums[0]
            res += high
            high = math.ceil(high / 3) 
            heapq._heapreplace_max(nums,high)
        return res