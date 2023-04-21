class Node: 
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            # i = ord(char) - ord("a")
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        
        def _dfs(idx,root):
            curr = root

            for i in range(idx, len(word)):
                # i = ord(char) - ord("a")
                char = word[i]
                if char == ".":
                    for child in curr.children.values():
                        if _dfs(i + 1, child ):
                            return True
                    return False
                else: 
                    if char not in curr.children: 
                        return False 
                    curr = curr.children[char]
                    
            return curr.endOfWord
        
        return _dfs(0, self.root)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)