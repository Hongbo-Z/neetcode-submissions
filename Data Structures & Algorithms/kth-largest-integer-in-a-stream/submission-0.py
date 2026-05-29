class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.miniHeap, self.k = nums, k
        heapq.heapify(self.miniHeap)
        while len(self.miniHeap) > k:
            heapq.heappop(self.miniHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.miniHeap, val)
        while len(self.miniHeap) > self.k:
            heapq.heappop(self.miniHeap)
        return self.miniHeap[0]  
