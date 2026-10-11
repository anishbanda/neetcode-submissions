class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        speed = r

        def eatingSpeed(m: int) -> int:
            hours = 0
            for pile in piles:
                hours += (pile + m - 1) // m
            return hours

        while l <= r:
            m = (l+r)//2
            if eatingSpeed(m) <= h:
                r = m-1
                speed = min(speed, m)
            else:
                l = m+1
        
        return speed