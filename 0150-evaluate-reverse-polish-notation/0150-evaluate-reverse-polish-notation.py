class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-*/'
        def operation(v1,v2,expression):
            match expression:
                case "+": return v1 + v2
                case '-': return v1 - v2
                case "*": return v1 * v2
                case "/": return v1 / v2
        for token in tokens: 
            if token not in operators: 
                stack.append(token)
            else: 
                v1 = int(stack.pop())
                v2 = int(stack.pop())
                newV = int(operation(v2,v1,token))
                stack.append(newV)
        return int(stack[0])