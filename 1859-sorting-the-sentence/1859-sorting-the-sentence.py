class Solution:
    def sortSentence(self, s: str) -> str: 
        words = s.split()
        arr = [ 0 for _ in range(len(words))]
        for word in words:
            i = int(word[-1])
            arr[i-1] = word[:-1]
        return ' '.join(arr)