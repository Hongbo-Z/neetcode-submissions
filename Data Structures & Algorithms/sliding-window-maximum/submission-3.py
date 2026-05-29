class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic decreasing deque of indices.
        q = collections.deque() # store index with the value in decreasing
        res = []
        l = 0

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            while q and q[0] < l:
                q.popleft()
            
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res


