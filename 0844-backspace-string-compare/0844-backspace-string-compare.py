class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s):
            stack = []
            for c in s:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack
        
        stack1 = backspace(s)
        stack2 = backspace(t)

        return stack1 == stack2



        
