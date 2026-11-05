class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        r = 0

        for bracket in s:
            if bracket == ")":
                if stack:
                    stack.pop()
                else:
                    r += 1
            else:
                stack.append(bracket)
            
        return r + len(stack)
        