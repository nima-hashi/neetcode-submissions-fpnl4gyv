class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l <= r:
            possibleTarget = numbers[l] + numbers[r]
            if possibleTarget == target:
                return [l + 1, r + 1]
            elif possibleTarget < target:
                l += 1
            else:
                r -= 1
                    