class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = Counter()
        for i, num in enumerate(nums):
            if i > k:
                last = nums[i-k-1]
                count[last] -= 1
            if count[num] >= 1: return True 
            count[num] += 1 
        return False