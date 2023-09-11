class Solution:
    def _isAnagram(self,word1, word2):
        
        return sorted(word1) == sorted(word2)
    
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 0 
        nextI = 1
        resArr = []
        
        while nextI < len(words) or i < len(words):
            while nextI < len(words) and self._isAnagram(words[i],words[nextI]):
                nextI += 1 
            resArr.append(words[i])
            i = nextI
            nextI = i + 1
        if not self._isAnagram(resArr[-1], words[-1]): resArr.append(words[-1])
        return resArr