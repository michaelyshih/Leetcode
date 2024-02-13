from collections import defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # amount = combination  return fewest min (fewest, coin count)
        # want to loop from the back 
        # after loop, amount never equals to combination return -1 
        # 0 count as a number
        
#         def _dfs(rem):
#             if rem == 0: return 0 
#             if rem in memo: return memo[rem]
            
#             memo[rem] = float("inf")
            
#             for coin in coins: 
#                 if rem - coin >= 0:
#                     memo[rem] = min(memo[rem], _dfs(rem - coin)+1)
            
#             return memo[rem]
        
#         memo = defaultdict(int)
#         result = _dfs(amount)
        
#         return result if result != float("inf") else -1  

        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0
        
        for value in range(1, amount +1):
            for coin in coins: 
                if value - coin >= 0: 
                    dp[value] = min(dp[value], dp[value-coin] + 1)
        return -1 if dp[amount] == float("inf") else dp[amount]
