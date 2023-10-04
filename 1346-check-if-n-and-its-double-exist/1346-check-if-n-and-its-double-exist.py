class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        pair = defaultdict(int)
        for i in arr:
            j = 0.5*i
            k =2 * i
            if pair[i]: return True 
            pair[j] = True
            pair[k] = True
        return False