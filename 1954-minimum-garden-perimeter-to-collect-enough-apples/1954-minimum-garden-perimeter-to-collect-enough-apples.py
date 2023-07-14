# cordinates x, y has |x| + |j| growing on it 
# alwaays square 
# square plot start at origin 
# return minimum perimiter that has at least neededApples on/in it

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        sum, n =0, 0 
        while sum < neededApples:
            sum += 12* (n**2)
            n+=1
        return 8* (n-1)