class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # res = []
        # l = 0
        # r = len(arr) - 1

        # while (r - l + 1) > k:
        #     if abs(arr[l] - x) <= abs(arr[r] - x):
        #         r -= 1
        #     else:
        #         l += 1
        # return arr[l:r + 1]

        # l = 0
        # r = len(arr) - k

        # while l < r:
        #     mid = (l + r) // 2
        #     if (x - arr[mid]) <= (arr[mid + k] - x):
        #         r = mid
        #     else:
        #         l = mid + 1
        # return arr[l: l + k]

        arr.sort(key=lambda num: (abs(num - x), num))
        return sorted(arr[:k])


        # [(), ()]
        # arr.aort(key lambda x: x[0])


            
        