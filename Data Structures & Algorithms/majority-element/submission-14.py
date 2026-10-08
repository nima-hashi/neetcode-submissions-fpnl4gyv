class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majElm = None
        count = 0

        for num in nums:
            if majElm is None:
                majElm = num
                count += 1
            elif num == majElm:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majElm = num
                    count = 1
        return majElm


        