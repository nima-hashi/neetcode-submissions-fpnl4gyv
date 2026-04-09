class Solution:
    def trap(self, height: List[int]) -> int:

        totalArea = 0
        for i in range(1, len(height)-1):
            water = min(max(height[:i]), max(height[i+1:])) - height[i]
            totalArea += max(water, 0)
        return totalArea


        #water[i] = min(maxLeft[i], maxRight[i]) - height[i]

        
