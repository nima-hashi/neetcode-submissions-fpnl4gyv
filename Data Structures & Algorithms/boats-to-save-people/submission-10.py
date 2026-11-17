class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0
        
        while l < r:
            curWeight = people[l] + people[r]
            if curWeight <= limit:
                l += 1
            res += 1
            r -= 1
        
        if l == r:
            res += 1
        return res
    