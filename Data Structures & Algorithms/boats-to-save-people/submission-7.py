class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        boats = 0
        l = 0
        r = len(people) - 1


        while l <= r:
            remainingSpace = limit - people[r]
            boats += 1
            r -= 1
            if l <= r and remainingSpace >= people[l]:
                l += 1
        return boats 

        [1,2,4,5]
