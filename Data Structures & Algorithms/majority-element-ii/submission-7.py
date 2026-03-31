class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # Extended Boyer–Moore (for n/3)

        # count1, count2 = 0, 0
        # candidate1 = candidate2 = None

        # for num in nums:
        #     if num == candidate1:
        #         count1 += 1
        #     elif num == candidate2:
        #         count2 += 1
        #     elif count1 == 0:
        #         candidate1 = num
        #         count1 += 1
        #     elif count2 == 0:
        #         candidate2 = num
        #         count2 += 1
        #     else:
        #         count1 -= 1
        #         count2 -= 1
        
        # res = []
        # if nums.count(candidate1) > (len(nums)//3):
        #     res.append(candidate1)
        # if nums.count(candidate2) > (len(nums)//3):
        #     res.append(candidate2)
        # return res

        hm = {}
        for num in nums:
            if len(hm) < 2 or (num in hm):
                hm[num] = hm.get(num, 0) + 1
            
            else:
                hm2 = {}
                for k in hm:
                    if hm[k] - 1 > 0:
                        hm2[k] = hm[k] - 1
                hm = hm2
        
        res = []
        for k in hm:
            if nums.count(k) > (len(nums)//3):
                res.append(k)
        return res
        

            
        