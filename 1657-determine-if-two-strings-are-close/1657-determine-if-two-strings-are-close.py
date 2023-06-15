from collections import defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if not len(word1) == len(word2): return False 
        map1 = defaultdict(int)
        for char in word1: 
            map1[char] += 1
        map2 = defaultdict(int)
        for char in word2:
            map2[char] += 1
        if not set(map1.keys()) == set(map2.keys()):
            return False
        sorted1 = sorted(list(map1.values()))
        sorted2 = sorted(list(map2.values()))
        if not sorted1 == sorted2:
            return False 
        return True 