class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter = min(str1,str2)
        longer = max(str1,str2)
        end = len(shorter)
        while end > 0:
            res = shorter[:end] 
            print(res, end)
            if res * int(len(longer)/ len(res)) == longer and res * int(len(shorter)/ len(res)) == shorter:
                return res
            end -= 1
        return ""