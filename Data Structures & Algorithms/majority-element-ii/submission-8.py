class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = {}
        majElm = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for k in count:
            if count[k] > len(nums)//3:
                majElm.append(k)
        
        return majElm
        
        