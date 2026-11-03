class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        count = [0] * 26
        for c in s:
            i = ord(c) - ord("a")
            count[i] += 1
        
        stack = []
        seen = set()

        for c in s:

            i = ord(c) - ord("a")
            count[i] -= 1

            if c in seen:
                continue

            while stack and stack[-1] > c and count[ord(stack[-1]) - ord("a")] > 0:
                removed = stack.pop()
                seen.remove(removed)
                
            
            stack.append(c)
            seen.add(c)
        
        return "".join(stack)

        