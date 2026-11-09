class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 0

        while fast < len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        else: 
            return None
        
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        