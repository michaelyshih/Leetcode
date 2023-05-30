class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter = str1 if len(str1) < len(str2) else str2
        longer = str1 if not shorter == str1 else str2
        end = len(shorter)
        while end > 0:
            res = shorter[:end] 
            print(res, end)
            if res * int(len(longer)/ len(res)) == longer and res * int(len(shorter)/ len(res)) == shorter:
                return res
            end -= 1
        return ""
    
#         len(res * len(res/len(res))) = len(long)