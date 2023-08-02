class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        i = 1
        while i < len(s):
            stack.append(s[i])
            if len(stack) > 1 and stack[-1] != stack[-2] and stack[-1].lower() == stack[-2].lower():
                stack.pop()
                stack.pop()
            i+=1
        return "".join(stack)