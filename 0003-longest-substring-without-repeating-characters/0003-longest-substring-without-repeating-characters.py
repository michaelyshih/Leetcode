class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        high = i = 0
        substring = set();

        for j in range(len(s)):
            while s[j] in substring:
                substring.remove(s[i])
                i += 1
            substring.add(s[j]);
            high = max(high, len(substring))
        return high