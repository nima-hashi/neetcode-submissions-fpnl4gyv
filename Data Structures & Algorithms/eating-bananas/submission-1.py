import math

class Solution:
    def hoursTakeToEatBananas(self, piles, rate):
        return sum(math.ceil(p / rate) for p in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            rate = (l + r) // 2
            hours = self.hoursTakeToEatBananas(piles, rate)
            if hours <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1

        return res
