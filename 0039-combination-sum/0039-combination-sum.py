class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = [] 
        def _bts(i,subset,total):
            if total == target:
                ans.append(subset.copy())
                return 
            if i >= len(candidates) or total > target:
                return 

            subset.append(candidates[i])
            _bts(i,subset,total + candidates[i])
            subset.pop()
            _bts(i+1,subset,total)

        _bts(0,[],0)
        return ans
#             self.ans = [] 
#             return self._bts(0,[],0, candidates,target)
#     def _bts(self,i, subset, total, candidates,target):

#             if total == target:
#                     self.ans.append(subset.copy())
#                     return

#             if i >= len(candidates) or total > target:
#                 return 
        
#             # keep pushing in instance of candidate at i and at the bts of that into the subset

#             subset.append(candidates[i])
#             self._bts(i, subset, total + candidates[i],candidates,target)
#             subset.pop()
#             self._bts(i+1, subset, total,candidates,target)
#             return self.ans

            
#         set up the ans array to catch when combination == target 
#         recursively call the helper and add i into subset to check if that combination == target 
#         two calls, one where end returns, one where you work the other branch 
