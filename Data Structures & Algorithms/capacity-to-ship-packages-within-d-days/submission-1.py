class Solution:
    def canShip(self, cap, weights, days):
        d = 1
        count = 0
        
        for w in weights:
            if count + w <= cap:
                count += w
            else:
                count = w
                d += 1
        return d <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        while l <= r:
            cap = (l + r) // 2
            if self.canShip(cap, weights, days):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res