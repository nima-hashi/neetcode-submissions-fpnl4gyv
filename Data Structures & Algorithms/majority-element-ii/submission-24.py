class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maxHeap = {}
        for num in nums:
            maxHeap[num] = maxHeap.get(num, 0) + 1
            if len(maxHeap) > 2:
                for k in list(maxHeap):
                    maxHeap[k] -= 1
                    if maxHeap[k] == 0:
                        del maxHeap[k]
        
        res = []
        for k in maxHeap:
            if nums.count(k) > len(nums)//3:
                res.append(k)
        
        return res




