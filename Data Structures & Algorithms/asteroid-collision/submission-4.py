class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        s = []

        for a in asteroids:

            while a < 0 and s and s[-1] > 0:
                if abs(a) == abs(s[-1]): # both explode
                    s.pop()
                    a = 0
                elif abs(a) > abs(s[-1]): # top explodes, keep checking
                    s.pop()
                else:
                    a = 0 # a explodes
            
            if a:
                s.append(a)

        return s


        