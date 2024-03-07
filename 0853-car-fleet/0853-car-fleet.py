# positiove, speed => arr same length of n 
# position[i] is position of i car and speed[i] us speed of i mph
# cannot pass but stack 
# distance is ignored => same position 
# if same position becomes one fleet
# if reach end together, still one fleet 
# return number of car fleets at destination 

# stack 
# [3(1),0,0,5(3),0,4(1),0,0,2(4),0,1(2),0,end]
# [0,1,0,0,0,0,0,4(1),0,0,0,0,1(2)]
# cars position and speed iterate through cars starting from last position 
# if next car pass prev car then merge 
# if hits end then pop stack and result +1


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         organize of tuple of cars (position, speed)
        carsV = [(p, s) for p, s in zip(position, speed)]
        carsV.sort(reverse=True)
#         some variable to store prev car 
#         velocity target from the current position 
#         divide that by speed of how many units will pass before hitting the end 
        res = [] 
    
        for p, s in carsV: 
            carV = (target - p)/s
            res.append(carV)
            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()
        print (res)
        return len(res)