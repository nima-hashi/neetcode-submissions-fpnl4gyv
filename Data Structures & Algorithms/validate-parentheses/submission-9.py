class Solution:
    def isValid(self, s: str) -> bool:

        matches = {")":"(", "]":"[", "}":"{"}

        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)        
            else:
                if not stack or stack.pop() != matches[c]:
                    return False
        
        if stack:
            return False
        return True
        