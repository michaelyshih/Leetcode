class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k > 0:
            return [sum(islice(cycle(code), i, i+k)) for i in range(1, len(code)+1)]
        if k < 0:
            return [sum(islice(cycle(reversed(code)), i, i-k)) for i in range(len(code), 0, -1)]
        return [0]*len(code)