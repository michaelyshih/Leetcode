class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = defaultdict(int)
        window = []
        for i in range(len(nums)):
            num = nums[i]
            window.append(num)
            if len(window) > k + 1:
                last = window.pop(0)
                count[last] -= 1
            if count[num] >= 1: return True 
            count[num] += 1 
        return False