class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1, h2 = {}, {}

        def helper(h,letter):
            for i in letter:
                if i in h:
                    h[i] += 1
                else:
                    h[i] = 1
            return h

        h1 = helper(h1,s)
        h2 = helper(h2,t)
        print(h1)
        print(h2)

        return h1 == h2
            
        
        
        