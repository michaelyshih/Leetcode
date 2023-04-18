class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def _bt(openN, closedN):
            if openN == closedN == n: 
                res.append("".join(stack))
                return 
            
            if openN < n:
                stack.append("(")
                _bt(openN+1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                _bt(openN, closedN+1)
                stack.pop()
            
        _bt(0,0)
        return res