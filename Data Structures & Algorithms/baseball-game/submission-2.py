class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for op in operations:
            if op not in {"+", "C", "D"}:
                stack.append(int(op))

            if op == "+":
                stack.append(stack[-1] + stack[-2])

            if op == "C":
                stack.pop()

            if op == "D":
                stack.append(stack[-1] * 2)
        
        return sum(stack)
        