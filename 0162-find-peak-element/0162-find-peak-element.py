class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
#         l, r = 0 , len(nums) - 1
        
#         while l < r: 
#             m = l + (r - l) // 2 
            
#             if nums[m] < nums[m +1]:
#                 l = m + 1
#             else:
#                 r = m
        
#         return l

        def _search(l,r):
            if l == r : return l 

            m = l + (r - l) // 2
            if nums[m] < nums[m+1]:
                return _search(m+1,r)
            else:
                return _search(l,m)

        return _search(0,len(nums)-1)