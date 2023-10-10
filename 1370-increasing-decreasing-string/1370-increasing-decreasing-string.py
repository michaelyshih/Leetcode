class Solution:
    def sortString(self, s: str) -> str:
        l1 = []
        for i in s:
            l1.append(i)
            r = ""
        while len(l1)>0:
            l2 = set(l1)
            l2 = list(l2)
            l2.sort()
            for i in l2 :
                if i in l1:
                    r = r+i
                    l1.remove(i)
            l2 = l2[::-1]
            for i in l2:
                if i in l1:
                    r = r+i
                    l1.remove(i)
        return r