class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # count = Counter()
        # for i, num in enumerate(nums):
        #     if i > k:
        #         last = nums[i-k-1]
        #         count[last] -= 1
        #     if count[num] >= 1: return True 
        #     count[num] += 1 
        # return False
        # Create hset for storing previous of k elements...
        hset = {}
        # Traverse for all elements of the given array in a for loop...
        for idx in range(len(nums)):
            # If duplicate element is present at distance less than equal to k, return true...
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            hset[nums[idx]] = idx
        # If no duplicate element is found then return false...
        return False