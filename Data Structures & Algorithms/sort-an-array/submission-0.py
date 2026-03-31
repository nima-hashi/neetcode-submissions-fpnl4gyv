class Solution:
    def merge(self, leftArr: List[int], rightArr: List[int]):
        merged = []

        i, j = 0, 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] <= rightArr[j]:
                merged.append(leftArr[i])
                i += 1
            else:
                merged.append(rightArr[j])
                j += 1

        while i < len(leftArr):
            merged.append(leftArr[i])
            i += 1
        
        while j < len(rightArr):
            merged.append(rightArr[j])
            j += 1
        
        return merged

    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        leftArr = self.sortArray(nums[:mid])
        rightArr = self.sortArray(nums[mid:])

        return self.merge(leftArr, rightArr)

        