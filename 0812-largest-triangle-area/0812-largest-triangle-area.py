from itertools import combinations
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a,b,c):
            return abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2
        triples = combinations(points,3)
        maxArea = 0
        for triple in triples:
            maxArea = max(maxArea, area(*triple))
        return maxArea