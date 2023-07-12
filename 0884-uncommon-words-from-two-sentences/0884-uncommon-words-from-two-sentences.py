class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split(" ") + s2.split(" ")
        d = defaultdict(int)
        missing = []
        for word in words: 
            d[word] += 1
        for word, val in d.items(): 
            if val == 1:
                missing.append(word)
        # for i, word in enumerate(words):
        #     if not d[word] == 1:
        #         words.pop(i)
        return missing
        # return words