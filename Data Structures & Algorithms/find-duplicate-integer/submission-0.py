class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num in count:
                return num
            count[num] = 1