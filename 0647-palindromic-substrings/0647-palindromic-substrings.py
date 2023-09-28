#       helper for palidrome 
#       check if the [aaa] is palindrom
#       could potentially return how many palindrome there are inside and call recursively
#       [aa] [a]


# different branch of starting index 
# left pointer and right pointer starting at l and ending at l + 1 
# if they are palidrome, then subparts are palidrom 
# when down to single letter, they are always palidrome 
# add to counter when you peel away at an end 
#  essentially counting the peeled away because they are aplidrome at 1 
#  index the a where the initial index stores the aray 

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res