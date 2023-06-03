from collections import defaultdict
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff = {"res1":[], "res2":[]}
        nums1set = set(nums1)
        nums2set = set(nums2)
        res = []
        for num1 in nums1set:
            if not num1 in nums2set:
                diff["res1"].append(num1)
        for num2 in nums2set: 
            if not num2 in nums1set:
                diff["res2"].append(num2)
        for (numsSet,item) in diff.items():
            res.append(item)
        return res