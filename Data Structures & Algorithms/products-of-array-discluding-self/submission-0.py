class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = [1 for i in range(len(nums))]
        prefix = 1
        for i in range(len(nums)):
            answers[i] *= prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, 0, -1):
            answers[i] *= suffix
            suffix *= nums[i]
        
        answers[0] *= suffix

        return answers
