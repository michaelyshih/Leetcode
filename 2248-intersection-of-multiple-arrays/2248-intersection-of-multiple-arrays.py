class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        res = []
        for arr in nums: 
            for num in arr: 
                count[num] += 1
        for (k,v) in count.items(): 
            if v == len(nums):res.append(k) 
        res.sort()
        return res