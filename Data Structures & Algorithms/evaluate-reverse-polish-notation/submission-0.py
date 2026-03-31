class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for ops in tokens:
            if ops == "+":
                stack.append(stack.pop() + stack.pop())
            elif ops == "*":
                stack.append(stack.pop() * stack.pop())
            elif ops == "-":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)
            elif ops == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1 / op2))
            else:
                stack.append(int(ops))
        return stack[-1]
        