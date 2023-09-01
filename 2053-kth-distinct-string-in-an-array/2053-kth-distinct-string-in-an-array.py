class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        recur = defaultdict(int)
        for word in arr: 
            recur[word] += 1
        res = []
        for word in arr: 
            if recur[word] <= 1:
                res.append(word)
        return res[k-1] if k <= len(res) else ''