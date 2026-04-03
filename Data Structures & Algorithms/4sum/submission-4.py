class Solution:
    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     nums.sort()
    #     res = []
    #     n = len(nums)

    #     for i in range(n):
    #         # skip duplicates
    #         if i > 0 and nums[i] == nums[i-1]:
    #             continue
            
    #         for j in range(i+1,n):
    #             # skip duplicates
    #             if (j > i + 1) and nums[j] == nums[j-1]:
    #                 continue
    #             # if j > i+1 and nums[j] == nums[j-1]:
    #             #     continue

    #             l = j+1
    #             r = n - 1

    #             while l < r:
    #                 total = nums[i] + nums[j] + nums[l] + nums[r]
    #                 if total == target:
    #                     res.append([nums[i], nums[j], nums[l], nums[r]])
    #                     l += 1
    #                     r -= 1
    #                     while l < r and nums[l] == nums[l-1]:
    #                         l += 1
    #                     while l < r and nums[r] == nums[r+1]:
    #                         r -= 1
    #                 elif total > target:
    #                     r -= 1
    #                 else:
    #                     l += 1
    #     return res
            

    def kSum(self, nums, target, k, start):
        res = []

        # 🔹 Base case: 2Sum (two pointers)
        if k == 2:
            l, r = start, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]

                if total == target:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif total < target:
                    l += 1
                else:
                    r -= 1

            return res

        # 🔹 Recursive case
        for i in range(start, len(nums)):
            # skip duplicates
            if i > start and nums[i] == nums[i-1]:
                continue

            # pick current number
            for subset in self.kSum(nums, target - nums[i], k - 1, i + 1):
                res.append([nums[i]] + subset)

        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4, 0)
        