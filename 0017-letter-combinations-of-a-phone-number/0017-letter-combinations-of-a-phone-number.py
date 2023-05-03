class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        alpha = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        def _bt (i , curStr):
            if len(curStr) == len (digits):
                res.append(curStr)
                return 
            for c in alpha[digits[i]]:
                _bt(i+1, curStr + c)
            
        if digits:
            _bt(0,"")
        
        return res