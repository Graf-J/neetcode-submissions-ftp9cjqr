from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize Queue
        dec_queue = deque() # Stores Indices
        for i in range(k):
            while dec_queue and nums[dec_queue[-1]] < nums[i]:
                dec_queue.pop()
            dec_queue.append(i)

        # Move Window
        result = [nums[dec_queue[0]]]
        for r in range(k, len(nums)):
            while dec_queue and nums[dec_queue[-1]] < nums[r]:
                dec_queue.pop()
            dec_queue.append(r)
            
            l = r - k + 1
            if dec_queue[0] < l:
                dec_queue.popleft()

            result.append(nums[dec_queue[0]])

        return result

        