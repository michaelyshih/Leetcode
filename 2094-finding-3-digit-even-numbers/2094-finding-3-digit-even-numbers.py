class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # count = Counter(digits)
        # res = []
        # for i in range(100,1000,2):
        #     digits = Counter((i//100, i//10%10, i%10))
        #     if not digits - count: 
        #         res.append(i)
        # return res
                
        cnt = Counter(digits)
        return [n for n in range(100, 1000, 2) if not Counter((n//100, n//10%10, n%10))-cnt]