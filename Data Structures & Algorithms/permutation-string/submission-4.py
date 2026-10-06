class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        for c in s1:
            count1[ord(c) - ord('a')] += 1
        
        left = 0
        count2 = [0] * 26
        for right in range(len(s1), len(s2)+1):
            for c in s2[left:right]:
                count2[ord(c) - ord('a')] += 1
            if count1 == count2:
                return True
            else:
                count2 = [0] * 26
                left += 1
        return False