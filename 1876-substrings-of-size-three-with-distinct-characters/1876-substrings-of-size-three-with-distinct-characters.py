class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3: return 0
        window = [s[0],s[1]]
        # wSet = set(window)
        count = 0
        for char in s[2:]:
            window.append(char)
            # wSet.add(char)
            print(window, set(window))
            if len(window) == len(set(window)): count += 1
            firstChar = window.pop(0)
            # if firstChar in wSet: wSet.remove(firstChar)
            
        return count