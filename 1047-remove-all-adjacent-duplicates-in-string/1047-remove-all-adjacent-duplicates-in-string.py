class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []
        for elm in s:
            if stack and stack[-1] == elm:
                stack.pop()
            else:
                stack.append(elm)
        
        return "".join(stack)
        