import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # QUICK SORT
        def partition(arr, low, high):
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

            pivot = arr[high]
            i = low
            for j in range(low, high):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[high] = arr[high], arr[i]
            return i


        def quickSort(arr, low, high):
            if low < high:
                pivot = partition(arr, low, high)
                quickSort(arr, low, pivot - 1)
                quickSort(arr, pivot + 1, high)
        
        quickSort(nums, 0, len(nums)-1)
        return nums
        
        # INSERTION SORT 


        # for i in range(1, len(nums)):
        #     cur = nums[i]
        #     j = i - 1
        #     while j >= 0 and nums[j] > cur:
        #         nums[j+1] = nums[j]
        #         j -= 1
        #     nums[j+1] = cur
        # return nums
        

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
        