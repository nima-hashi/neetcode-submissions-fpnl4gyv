class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxHeight = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                start = index
                possibleHeight = (i-index) * height
                maxHeight = max(maxHeight, possibleHeight)
            stack.append([start, h])

        for i, h in stack[::-1]:
            possibleHeight = (len(heights)-i) * h
            maxHeight = max(maxHeight, possibleHeight)
        
        return maxHeight
            
        