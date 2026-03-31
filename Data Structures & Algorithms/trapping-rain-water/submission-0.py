class Solution:
    def trap(self, height: List[int]) -> int:

        maxA = 0

        for i in range(len(height)):
            maxL = max(height[:i], default=0)
            maxR = max(height[i:], default=0)

            area = min(maxL, maxR) - height[i]
            if area > 0:
                maxA += area

        return maxA
