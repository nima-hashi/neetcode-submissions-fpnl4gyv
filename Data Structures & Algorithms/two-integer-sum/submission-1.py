class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}
        
        for i in range(len(nums)):
            if hashMap == {}:
                hashMap[nums[i]] = i

            else:
                r = target - nums[i]
                if r in hashMap:
                    return [hashMap[r], i]

                hashMap[nums[i]] = i





      
        