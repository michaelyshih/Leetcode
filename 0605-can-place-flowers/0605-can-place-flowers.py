class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = n
        i = 0
        while count > 0 and i < len(flowerbed):
            if flowerbed[i] == 0:
                
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1 
                    count -= 1 
                    if count < 1:
                        return True 
            i += 1
        return count == 0