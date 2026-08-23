class CountSquares:
    def __init__(self):
        self.points = []
        self.counts = collections.Counter()

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.counts[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for px, py in self.points:
            if abs(px - x) != abs(py - y) or px == x:
                continue
            res += self.counts[(x, py)] * self.counts[(px, y)]
        return res
        
