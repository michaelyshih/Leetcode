class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r, l, dr, dl = 0,0, len(s) / 2, len(s)/ 2
        count = 0
        for char in s: 
            if char == "R":
                r += 1
                dr -= 1
            else: 
                l += 1
                dl -= 1
            # print(r,l, dr, dl)
            if r == l and dr == dl: 
                count += 1
        return count