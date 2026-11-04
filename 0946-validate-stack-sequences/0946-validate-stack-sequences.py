class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:

        stack = []
        c = 0

        for elm in pushed:
            stack.append(elm)
            while stack and stack[-1] == popped[c]:
                stack.pop()
                c += 1
        
        while stack:
            if stack.pop() != popped[c]:
                return False
            
            c += 1
        
        return stack == []


        