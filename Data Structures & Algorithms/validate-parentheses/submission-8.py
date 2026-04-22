class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        openedBracket = {"{":"}", "[":"]", "(":")"}

        for bracket in s:
            if bracket in openedBracket:
                stack.append(bracket)
            else:
                if stack:
                    b = stack.pop()
                    if openedBracket[b] != bracket:
                        return False
                else:
                    return False
        return len(stack) == 0
        