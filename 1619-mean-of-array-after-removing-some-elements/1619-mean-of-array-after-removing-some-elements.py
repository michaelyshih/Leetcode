class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n=len(arr)
        per5=5/100*n 
        arr.sort() 
        p=arr[int(per5):(n-int(per5))]
        #print (per5)
        return sum(p)/len(p)