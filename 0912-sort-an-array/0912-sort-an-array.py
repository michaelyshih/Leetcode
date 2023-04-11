class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        mid = len(nums) // 2
        left, right = self.sortArray(nums[:mid]), self.sortArray(nums[mid::])
        return merge(left, right)
        
    def merge(left,right):
        merged = []
        while len(left) and len(right):
            if left[0] < right[0]:
                merged.push(left.shift())
            else:
                merged.push(right.shift())
        return merged + left + right