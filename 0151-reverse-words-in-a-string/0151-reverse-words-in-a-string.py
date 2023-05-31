class Solution:
    def reverseWords(self, s: str) -> str:
        lst = reversed(s.split(" "))
        newlst = list(filter(lambda e: e != "", lst))
        print(newlst)
        return " ".join(newlst)