class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        for i in range(1, len(nums)):
            cur = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > cur:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = cur
        return nums
        

        # MERGE SORT

        # def merge(left, right):
            
        #     res = []
        #     i = 0
        #     j = 0
        #     while i < len(left) and j < len(right):
        #         if left[i] <= right[j]:
        #             res.append(left[i])
        #             i += 1
        #         else:
        #             res.append(right[j])
        #             j += 1
        #     res.extend(left[i:])
        #     res.extend(right[j:])
        #     return res


        # def mergeSort(arr):

        #     if len(arr) <= 1:
        #         return arr
            
        #     mid = len(arr)//2
        #     left = mergeSort(arr[:mid])
        #     right = mergeSort(arr[mid:])
        #     return merge(left, right)


        # return mergeSort(nums)
        