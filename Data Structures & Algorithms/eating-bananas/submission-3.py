import math

class Solution:
    def hoursTakeToEatBananas(self, piles, rate):
        return sum(math.ceil(p / rate) for p in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = self.hoursTakeToEatBananas(piles, k)
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res
