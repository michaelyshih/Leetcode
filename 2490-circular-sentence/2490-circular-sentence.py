class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[-1].lower != sentence[0].lower: return False
        words = sentence.split()
        lastChar = words[0][-1]
        for word in words[1:]: 
            if word[0] != lastChar: return False 
            lastChar = word[-1]
        return True