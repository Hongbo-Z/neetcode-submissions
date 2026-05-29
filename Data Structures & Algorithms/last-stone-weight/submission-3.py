class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x - y > 0:
                heapq.heappush(heap, y - x)
        return -heap[0] if heap else 0