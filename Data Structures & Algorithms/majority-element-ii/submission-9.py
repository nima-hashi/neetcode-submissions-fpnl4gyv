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

        possibleMajElm = {}

        for num in nums:
            if len(possibleMajElm) < 2 or num in possibleMajElm:
                possibleMajElm[num] = possibleMajElm.get(num, 0) + 1
            else:
                deleteElms = []
                for k in possibleMajElm:
                    possibleMajElm[k] -= 1
                    if possibleMajElm[k] == 0:
                        deleteElms.append(k)

                for d in deleteElms:
                    del possibleMajElm[d]
        
        actMaj = []
        for k in possibleMajElm:
            if nums.count(k) > len(nums) // 3:
                actMaj.append(k)
        return actMaj


        
        