class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxHeight = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                popped = stack.pop()
                possibleMax = (i - popped[0]) * popped[1]
                maxHeight = max(maxHeight, possibleMax)

                start = popped[0]

            stack.append([start, h])
        
        for i, h in stack:
            possibleMax = (len(heights) - i) * h
            maxHeight = max(maxHeight, possibleMax)
            #stack.pop()
            
        return maxHeight
        