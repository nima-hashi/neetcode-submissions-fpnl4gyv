class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = 500

        while l <= r:
            shipCapacity = (l+r) // 2
            daysNeeded = 0
            curWeight = 0
            for package in weights:
                if curWeight + package <= shipCapacity:
                    curWeight += package
                else:
                    curWeight = package
                    daysNeeded += 1
            if curWeight > 0:
                daysNeeded += 1
            
            if daysNeeded > days:
                l = shipCapacity + 1
            else:
                r = shipCapacity - 1
                res = shipCapacity 
        
        return res     