class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxC = max(candies)
        return list(map(lambda x: x + extraCandies >= maxC, candies))