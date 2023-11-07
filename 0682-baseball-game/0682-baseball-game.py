class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for val in operations: 
            if val == "C": 
                scores.pop()
                continue
            if val =="D":
                scores.append(scores[-1] * 2)
                continue
            if val =='+':
                scores.append(scores[-1]+ scores[-2])
                continue
            scores.append(int(val))
        return sum(scores)