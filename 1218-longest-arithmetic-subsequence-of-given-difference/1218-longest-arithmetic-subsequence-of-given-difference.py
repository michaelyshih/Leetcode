class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        print(arr)
        for num in arr: 
            dp[num] = 1 + dp[num-difference]
        print(dp)
        return max(dp.values())