class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        trappedWater = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                curA = (min(leftMax, rightMax) - height[l])
                trappedWater += max(0, curA)
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                curA = (min(leftMax, rightMax) - height[r])
                trappedWater += max(0, curA)
                
        return trappedWater




        