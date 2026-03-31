class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0

        while l <= r:
            mid = (l+r)//2
            if mid**2 == x:
                return mid
            if mid**2 < x:
                l = mid + 1
                res = mid
            else:
                r = mid - 1
        
        return res
