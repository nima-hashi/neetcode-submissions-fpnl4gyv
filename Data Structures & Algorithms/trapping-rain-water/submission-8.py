class Solution:
    def trap(self, height: List[int]) -> int:

        # totalArea = 0
        # for i in range(1, len(height)-1):
        #     water = min(max(height[:i]), max(height[i+1:])) - height[i]
        #     totalArea += max(water, 0)
        # return totalArea

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


        
