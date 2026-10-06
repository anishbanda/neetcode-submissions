class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        characters = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in characters:
                characters.remove(s[left])
                left += 1
            characters.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest
