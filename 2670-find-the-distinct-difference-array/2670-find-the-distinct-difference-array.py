class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        ans=[]
        while left<n:
            ans.append(len(set(nums[0:left+1]))-len(set(nums[left+1:right+1])))
            right+=1
            left+=1

        return ans  