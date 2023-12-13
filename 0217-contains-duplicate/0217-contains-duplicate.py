from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for num in nums: 
            if count[num] == 1: 
                return True
            count[num] += 1
            
        return False
        # dupSet = set()
        # for num in nums: 
        #     if num in dupSet: 
        #         return True
        #     dupSet.add(num)
        # return False