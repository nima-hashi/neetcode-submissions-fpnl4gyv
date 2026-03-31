class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(substring):
            l = 0
            r = len(substring) - 1

            while l < r:
                if substring[l] != substring[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[l:r]) or isPalindrome(s[l+1:r+1])
            l += 1
            r -= 1
        return True

        