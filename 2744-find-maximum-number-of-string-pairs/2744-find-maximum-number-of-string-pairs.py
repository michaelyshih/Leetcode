class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        pair = defaultdict(str)
        count = 0
        for word in words: 
            rev = str(word[::-1])
            if pair[word]: count += 1
            pair[rev] = word
        return count