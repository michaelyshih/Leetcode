class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0 
        # j = 0
        res = ""
        while i < len(word1) and i < len(word2):
            res += word1[i]
            res += word2[i]
            i+=1
        return "".join(res + word1[i:] + word2[i:])