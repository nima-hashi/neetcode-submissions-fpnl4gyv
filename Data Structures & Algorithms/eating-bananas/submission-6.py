import math
class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(mid):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            return hours

        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            mid = (l + r) // 2
            hours = valid(mid)
            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
            
            

        