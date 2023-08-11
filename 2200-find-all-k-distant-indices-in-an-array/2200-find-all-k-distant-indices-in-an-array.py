class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        i, j = 0, 0
        while i < len(nums):
            if i-j > k: j += 1
            while j < len(nums) and not nums[j] == key: 
                j += 1    
            print(abs(i-j))
            if j < len(nums) and abs(i-j) <= k: 
                res.append(i)
                i += 1
            else:
                i+=1
        return res
            