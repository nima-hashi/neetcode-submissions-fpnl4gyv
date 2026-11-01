class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        s = []

        for a in asteroids:
            alive = True

            while alive and a < 0 and s and s[-1] > 0:
                if abs(a) == abs(s[-1]): # both explode
                    s.pop()
                    alive = False
                elif abs(a) > abs(s[-1]): # top explodes, keep checking
                    s.pop()
                else:
                    alive = False # a explodes
            
            if alive:
                s.append(a)

        return s


        