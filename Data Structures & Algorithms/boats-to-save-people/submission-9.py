class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0
        
        while l <= r:
            curWeight = people[l] + people[r]
            if (l == r) or curWeight <= limit:
                res += 1
                l += 1
                r -= 1

            elif curWeight > limit:
                res += 1
                r -= 1
        return res

        [1,2,2,3,3  ]
    