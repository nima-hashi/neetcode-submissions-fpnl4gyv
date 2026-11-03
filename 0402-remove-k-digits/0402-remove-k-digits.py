class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for digit in num:
            while stack and k > 0 and digit < stack[-1]:
                    stack.pop()
                    k -= 1
        
            if not stack and digit == "0":
                continue 

            stack.append(digit)
        
        while stack and k > 0:
            stack.pop()
            k -= 1
        
        
        return "".join(stack) or "0"


        