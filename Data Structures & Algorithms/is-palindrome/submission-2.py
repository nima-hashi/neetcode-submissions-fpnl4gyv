class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        print(s)
        split = len(s) // 2

        firstHalf = s[:split]
        secondHalf = None

        if len(s) % 2 == 0:
            secondHalf = s[split:]
        else:
            secondHalf = s[split + 1:]
        
        secondHalf = secondHalf[::-1]

        return firstHalf == secondHalf


        # Properly determine secondHalf, skipping the middle character if the length is odd
        #secondHalf = s[split + (len(s) % 2):]


