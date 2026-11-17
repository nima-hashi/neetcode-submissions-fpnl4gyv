class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxA = 0

        while l < r:
            h = min(heights[l], heights[r])
            w = r - l

            curA = h * w
            maxA = max(curA, maxA)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxA

        