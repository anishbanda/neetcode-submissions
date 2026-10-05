class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            anagrams[sortedS].append(s)
        return list(anagrams.values())