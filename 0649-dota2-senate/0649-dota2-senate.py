# two teams represented by R and D 
# two actions to take: 
#   - remove next person from string 
#   - announce victory if winner

# loop once to count and make queue 
# loop until queue is advantageous
# if numbers is advantageous reutrn winner 
# else remove self from queue and add to end of queue and remove next person queue. 

from collections import defaultdict, deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        senate = deque(senate)
        n = len(senate)
        for i, chair in enumerate(senate): 
            R.append(i) if chair == "R" else D.append(i)
                
        while D and R:
            rTurn = R.popleft()
            dTurn = D.popleft()
            R.append(rTurn + n) if rTurn < dTurn else D.append(dTurn+n)
            n += 1

        return "Radiant" if R else "Dire"