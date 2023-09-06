class Solution:
    def numSplits(self, s: str) -> int:
        count = defaultdict(int)
        l = set()
        r = set(s)
        for c in s:
            count[c] += 1
        res = 0 
        for char in s:
            l.add(char)
            count[char] -= 1
            if count[char] == 0:
                r.remove(char)
            if len(r) == len(l):
                res += 1
                
        return res
            