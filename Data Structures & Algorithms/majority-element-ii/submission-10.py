class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # count = {}
        # majElm = []

        # for num in nums:
        #     count[num] = count.get(num, 0) + 1

        # for k in count:
        #     if count[k] > len(nums)//3:
        #         majElm.append(k)
        
        # return majElm

        # sol 2
        
        # possibleMajElm = {}

        # for num in nums:
        #     if len(possibleMajElm) < 2 or num in possibleMajElm:
        #         possibleMajElm[num] = possibleMajElm.get(num, 0) + 1
        #     else:
        #         deleteElms = []
        #         for k in possibleMajElm:
        #             possibleMajElm[k] -= 1
        #             if possibleMajElm[k] == 0:
        #                 deleteElms.append(k)

        #         for d in deleteElms:
        #             del possibleMajElm[d]
        
        # actMaj = []
        # for k in possibleMajElm:
        #     if nums.count(k) > len(nums) // 3:
        #         actMaj.append(k)
        # return actMaj


        #sol 3

        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []

        for candidate in (candidate1, candidate2):
            if candidate is not None and nums.count(candidate) > len(nums) // 3:
                result.append(candidate)

        return result



        
        