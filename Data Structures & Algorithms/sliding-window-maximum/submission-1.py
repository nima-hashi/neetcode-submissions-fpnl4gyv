class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        maxElms = []
        window = collections.deque() # stores indices

        l = 0
        for r in range(len(nums)):
            # remove smaller values from the right
            while window and nums[window[-1]] <= nums[r]:
                window.pop()

            window.append(r)

            # remove elements out of window
            if window[0] < l:
                window.popleft()

            # when window hits size k
            if r - l + 1 == k:
                maxElms.append(nums[window[0]])
                l += 1

                # clean up left pointer effect
                if window and window[0] < l:
                    window.popleft()


        return maxElms
               



        