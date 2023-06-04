class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        maxAltPos = 0
        currentAlt = 0
        prevAlt = 0
        for i, netGain  in enumerate(gain):
            currentAlt += netGain
            if i == 0 and currentAlt > 0:
                maxAlt = currentAlt
            if currentAlt > maxAlt: 
                maxAlt = currentAlt 
                maxAltPos = i + 1 
            print(currentAlt,maxAlt, maxAltPos)
        return maxAlt
                
                