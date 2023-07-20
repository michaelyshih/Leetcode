class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0 
        k = float(-inf)
        for x,y in intervals:
            if x >= k: 
                k =y
            else:
                ans += 1
        return ans
        
#         intervals.sort()
#         print(intervals)
        
#         prevEnd = intervals[0][1]
#         count = 0
#         for start, end in intervals[1:]:
#             if start >= prevEnd: 
#                 prevEnd = end
#             else: 
#                 count += 1
#                 prevEnd = min(end, prevEnd)
                
#         return count