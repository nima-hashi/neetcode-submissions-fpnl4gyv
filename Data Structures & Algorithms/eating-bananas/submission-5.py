import math
class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(mid):
            hoursNeeded = 0
            rate = mid

            for p in piles:
                hoursNeeded += math.ceil(p / rate)
            if hoursNeeded > h:
                return (False, hoursNeeded)
            return (True, hoursNeeded)   

        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            mid = (l + r) // 2
            check, hours = valid(mid)
            if check:
                res = min(res, mid)
            if hours <= h:
                r = mid - 1
            else:
                l = mid + 1
        return res
            
            

        