class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[r] < nums[m]:
                l = m+1
            else:
                r = m
        
        small = l
        l, r = 0, len(nums)-1

        if target >= nums[small] and target <= nums[r]:
            l = small
        else:
            r = small-1
        
        while l <= r:
            m = (l+r)//2
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        
        return -1