class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        v = self.store.get(key, [])
        if v == []:
            return res
        l ,r = 0, len(v) - 1
        while l <= r:
            mid = (l + r)//2
            if v[mid][1] == timestamp:
                return v[mid][0]
            elif v[mid][1] > timestamp:
                r = mid -1
            else:
                l = mid + 1
                res = v[mid][0]
        return res
        
        
        
