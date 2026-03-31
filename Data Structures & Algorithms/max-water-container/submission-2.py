class Solution:
    def maxArea(self, heights: List[int]) -> int:

        finalMax = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            finalMax = max(finalMax, w*h)

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return finalMax



            

        