class Solution:
    def merge(self, nums, l, r, m):
        left = nums[l:m+1]
        right = nums[m+1:r+1]
        i, j, k = 0, 0, l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j] 
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j] 
            j += 1
            k += 1


    def mergeSort(self, nums, l, r):
        if l == r:
            return nums
        m = (l + r) // 2
        self.mergeSort(nums, l, m)
        self.mergeSort(nums, m + 1, r)
        self.merge(nums, l, r, m)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)


    

    # solution below uses extra memory 
    # def merge(self,left, right):
    #     res = []

    #     i, j = 0,0
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

    # def mergeSort(self,nums):
    #     if len(nums) <= 1:
    #         return nums
        
    #     mid = len(nums) // 2
    #     left = self.mergeSort(nums[:mid])
    #     right = self.mergeSort(nums[mid:])
    #     return self.merge(left, right)

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     return self.mergeSort(nums)


        