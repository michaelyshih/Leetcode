from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]
        
#         for n in nums: 
#             count[n] = 1 + count.get(n,0)
#         for n, c in count.items():
#             freq[c].append(n)
        
#         res = []
#         for i in range( len(freq)- 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k: 
#                     return res
        res=[]
        dict = collections.Counter(nums)
        for val, count in dict.items():
            if len(res)<k:
                heapq.heappush(res,(count,val))
            else:
                heapq.heappushpop(res,(count,val))

        return [val for count, val in res]
        