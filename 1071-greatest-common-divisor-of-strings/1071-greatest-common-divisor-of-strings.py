class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # shorter = min(str1,str2)
        # longer = max(str1,str2)
        # end = len(shorter)
        # while end > 0:
        #     res = shorter[:end] 
        #     print(res, end)
        #     if res * int(len(longer)/ len(res)) == longer and res * int(len(shorter)/ len(res)) == shorter:
        #         return res
        #     end -= 1
        # return ""
        
        
        len1, len2 = len(str1), len(str2)
        
#         check to see if bot str can be divided up to length l
        def isDivisor(l):
            if len1 % l or len2 % l: 
                return False 
            f1, f2 = len1 // l , len2 // l 
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2
            
        for l in range( min(len1,len2),0,-1):
            if isDivisor(l):
                return str1[:l]
        
        return ""