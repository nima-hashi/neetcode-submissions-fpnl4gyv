class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def merge(nums,l,r,mid):

            i, j, k = 0,0,l
            left = nums[l:mid+1]
            right = nums[mid+1:r+1]

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


        def mergeSort(nums,l,r):
            if l == r:
                return nums
            mid = (l+r)//2
            mergeSort(nums,l,mid)
            mergeSort(nums,mid+1,r)
            merge(nums,l,r,mid)
            return nums

        return mergeSort(nums,0, len(nums))
        
        