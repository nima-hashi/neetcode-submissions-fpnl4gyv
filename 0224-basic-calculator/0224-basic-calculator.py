class Solution:
    def calculate(self, s: str) -> int:

        curRes = 0 # subprob sol
        sign = 1
        curNum = 0 # cur number like 123
        stack = [] # [curRes, sign]

        for c in s:
            if c.isdigit():
                curNum = curNum * 10 + int(c)
            
            elif c == "+":

                curRes += (curNum * sign)
                curNum = 0
                sign = 1
            
            elif c == "-":
                
                curRes += (curNum * sign)
                curNum = 0
                sign = -1
            
            elif c == "(":
                stack.append([curRes, sign])
                curRes = 0
                sign = 1
            
            elif c == ")":
                curRes += curNum * sign
                curNum = 0

                popped = stack.pop()
                curRes = (curRes * popped[1]) + popped[0]

        return curRes + (curNum * sign)

        
