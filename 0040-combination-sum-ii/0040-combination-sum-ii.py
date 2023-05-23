class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def _bts(pos, subset, target):
            if target == 0: 
                res.append(subset.copy())
            if target <= 0: 
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                
                subset.append(candidates[i])
                _bts(i+1,subset, target - candidates[i])
                subset.pop()
                prev = candidates[i]
        
        _bts(0,[],target)
        return res
    