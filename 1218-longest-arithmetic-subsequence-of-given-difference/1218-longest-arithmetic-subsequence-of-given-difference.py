class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
#         dp = {}
#         answer = 1
#         for a in arr:
#             before_a = dp.get(a - difference, 0)
#             dp[a] = before_a + 1
#             answer = max(answer, dp[a])
            
#         return answer
        dp = defaultdict(int)
        solution = 1
        for num in arr: 
            dp[num] = 1 + dp[num-difference]
            solution = max(solution, dp[num])
        return solution
