class Solution:
    def isValid(self, s: str) -> bool:

        opens = ["(", "{", "["]
        stack = []

        for elm in s:
            if elm in opens:
                stack.append(elm)

            else:
            
                if not stack:
                    return False

                popped = stack.pop()
                
                if elm == ")":
                    if popped != "(":
                        return False
                
                elif elm == "}":
                    if popped != "{":
                        return False
                
                elif elm == "]":
                    if popped != "[":
                        return False
        if stack:
            return False
        return True

        