class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        d = collections.deque()
        l = 0
        res = []
        for i, num in enumerate(nums):
            if d and d[0][0] < (i-k+1):
                d.popleft()
            while d and d[-1][1] <= num:
                d.pop()
            d.append([i, num])
            if i-l+1 == k:
                res.append(d[0][1])
                l += 1
        return res
        