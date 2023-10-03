class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        a,b = Counter(word1),Counter(word2) 
        for x in a: 
            for y in b:
                length1 = len(a)
                length2 = len(b)
                if a[x] == 1 and x != y:
                    length1 -= 1
                if b[y] == 1 and x != y:
                    length2 -= 1
                    
                if y not in a:
                    length1 += 1
                if x not in b:
                    length2 += 1
                    
                if length1 == length2:
                    return True
                
        return False