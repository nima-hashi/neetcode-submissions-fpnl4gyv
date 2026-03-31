class TimeMap:

    def __init__(self):
        self.time = {} # {(alice,1): happy}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = [[value, timestamp]]
        else:
            self.time[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        search = self.time.get(key, [])
        res = ""

        l, r = 0, len(search) - 1
        while l <= r:
            mid = (l + r) // 2
            # if search[mid][1] == timestamp:
            #     return search[mid][0]
            if search[mid][1] > timestamp:
                r = mid - 1
            else:
                res = search[mid][0]
                l = mid + 1
        return res
        


