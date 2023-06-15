from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict(int)
        for num in arr: 
            count[num] += 1
        countSet = set(count.values())
        if len(count.keys()) == len(countSet):
            return True 
        return False 