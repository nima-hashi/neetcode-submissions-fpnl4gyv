class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            subString = []
            if c == "]":
                while stack[-1] != "[":
                    subString.append(stack.pop())
                stack.pop()
                subString = "".join(subString[::-1])
                n = []
                while stack and stack[-1].isdigit():
                    n.append(stack.pop())
                n = n[::-1]
                n = "".join(n)

                stack.append(int(n) * subString)
        
            else:
                stack.append(c)
            
        return "".join(stack)

        