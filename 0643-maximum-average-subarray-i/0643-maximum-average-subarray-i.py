class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r = 0, 0
        currSum = nums[r]
        maxSum = 0
        if len(nums) <= k:
            return sum(nums) / k
        while r < k -1: 
            r += 1 
            currSum += nums[r]
        maxSum = currSum
        while r < len(nums) - 1:
            r += 1 
            currSum += nums[r]
            print(currSum)
            currSum -= nums[l]
            l += 1 
            print (nums[l], nums[r], currSum)
            maxSum = max(maxSum, currSum)
            print(maxSum)
        print(maxSum)
        return maxSum / k