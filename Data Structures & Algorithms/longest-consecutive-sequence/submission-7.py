class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numSet = set(nums)
        maxLength = 0

        for num in nums:
            if num - 1 not in numSet:
                currLength = 1

                while num + currLength in numSet:
                    currLength += 1
                
                maxLength = max(maxLength, currLength)
        
        return maxLength