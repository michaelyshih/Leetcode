class Solution:
    def sortString(self, s: str) -> str:
        res = []
        
        # frequence
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
        
        while True:
            #increase round
            for i in range(26):
                ch = chr(ord('a') + i)
                if d[ch] > 0:
                    res.append(ch)
                    d[ch] -= 1
            
            #decrease round
            for i in range(26):
                ch = chr(ord('z') - i)
                if d[ch] > 0:
                    res.append(ch)
                    d[ch] -= 1
            
            # check quit condition
            stop = True
            for key in d:
                if d[key] > 0:
                    stop = False
                    break
            
            if stop:
                return "".join(x for x in res)