class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        count = nums[0]
        top = count
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                count += nums[i]
            else: 
                count = nums[i]
            # print(i, count)
            top = max(top,count)
        return top