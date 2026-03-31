class Solution:
    def trap( self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        trappedWater = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                trappedWater += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                trappedWater += rightMax - height[r]
              
        return trappedWater