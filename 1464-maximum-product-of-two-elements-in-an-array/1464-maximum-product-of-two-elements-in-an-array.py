import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heapq._heapify_max(nums)
        max1, max2 = heapq._heappop_max(nums), heapq._heappop_max(nums)
        return (max1 - 1)* (max2 - 1)