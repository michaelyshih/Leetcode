class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = Counter()
        window = []
        for i, num in enumerate(nums):
            window.append(num)
            if len(window) > k + 1:
                last = window.pop(0)
                count[last] -= 1
            if count[num] >= 1: return True 
            count[num] += 1 
        return False