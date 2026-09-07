class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        while k > 0:
            num = heapq.heappop(heap)
            k -= 1
        return -num