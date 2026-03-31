class Solution:
    def trap(self, height: List[int]) -> int:
        
        trappedWater = 0

        for i in range(1, len(height)-1):
            leftMax = max(height[:i])
            rightMax = max(height[i+1:])
            trappedWater += max(0, min(leftMax, rightMax) - height[i])
        return trappedWater
        

