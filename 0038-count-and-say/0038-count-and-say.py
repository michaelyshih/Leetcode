# from collections import defaultdict
class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1: return "1"
        # hash = defaultdict(int)
        count = 1
        string = self.countAndSay(n-1)
        result = ""
        i = 0 
        print(string)
        while i < len(string): 
            while i < len(string) - 1 and string[i + 1] == string[i]:
                count += 1
                i += 1
            result += str(count) + string[i]
            count = 1
            i+=1
        #     hash[substring] += 1
        # for substring, count in hash.items(): 
        #     result += str(count) + substring
        return result