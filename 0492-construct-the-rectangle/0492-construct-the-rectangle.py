class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        a = int(sqrt(area))
        while a < area:
          if area % a == 0:
            b = area // a
            return [max(a, b), min(a, b)]
          a += 1
        return [area, 1]