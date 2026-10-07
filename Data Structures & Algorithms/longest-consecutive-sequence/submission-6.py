class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        check = set(nums)
        longest = 1

        for num in nums:
            length = 1
            if num - 1 in check:
                continue
            while num + length in check:
                length += 1
            
            longest = max(longest, length)
        
        return longest