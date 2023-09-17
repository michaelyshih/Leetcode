class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        rev = sorted(nums, reverse=True)
        count = 0
        end = len(rev)
        for i in range(end): 
            for j in range(i+1,end):
                for k in range(j+1,end):
                    c,b,a = rev[i],rev[j],rev[k],
                    if a + b <= c: break
                    return sum([a,b,c])
                
        return 0