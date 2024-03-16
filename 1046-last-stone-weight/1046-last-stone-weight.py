class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] #only a min heap... flip to use for max heap /ruby has both
        heapq.heapify(stones) # O(n)
        while len(stones) > 1: # O(n)
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: 
                heapq.heappush(stones, first-second) #O(log n)
        stones.append(0)
        return abs(stones[0])