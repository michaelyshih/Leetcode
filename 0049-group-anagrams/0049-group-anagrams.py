class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            print(''.join(sorted(word)))
            sortedWord = ''.join(sorted(word))
            # If word is not in dictionary
            if sortedWord not in dictionary:
                dictionary[sortedWord] = [word]
            # If previously it is present that means its anagram
            # was previously present
            else:
                dictionary[sortedWord] += [word]
        return [dictionary[i] for i in dictionary]