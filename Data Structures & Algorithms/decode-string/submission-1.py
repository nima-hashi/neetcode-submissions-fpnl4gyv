class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for elm in s:
            if elm != "]":
                stack.append(elm)
            else:
                subS = []
                popped = stack.pop()
                while popped != "[":
                    subS.append(popped)
                    popped = stack.pop()
                correctSubS = "".join(subS[::-1])
                subNum = []
                while stack and stack[-1].isdigit():
                    subNum.append(stack.pop())
                correctSubNum = int("".join(subNum[::-1]))
                stack.append(correctSubNum * correctSubS)
        
        final = []
        while stack:
            final.append(stack.pop())
        return "".join(final[::-1])


    




        