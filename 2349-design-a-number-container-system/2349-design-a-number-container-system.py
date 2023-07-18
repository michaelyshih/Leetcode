from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.lookup = {}
        self.s = defaultdict(lambda: SortedList())

    def change(self, index: int, number: int) -> None:
        if index in self.lookup:
            prev = self.lookup[index]
            self.s[prev].remove(index)
        self.lookup[index] = number
        self.s[number].add(index)
        

    def find(self, number: int) -> int:
        if number not in self.s or len(self.s[number]) == 0:
            return -1
        return self.s[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)