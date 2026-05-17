class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        temp = self.timemap.get(key,[])
        temp.append([timestamp,value])
        self.timemap[key] = temp

    def get(self, key: str, timestamp: int) -> str:
        timelist = self.timemap.get(key,[])
        if timelist == [] or timelist[0][0]>timestamp:
            return ''
        l = 0
        r = len(timelist)-1
        while l <=r:
            mid = (l+r)//2
            if timelist[mid][0] == timestamp:
                return timelist[mid][1]
                break
            elif timelist[mid][0] > timestamp:
                r = mid-1
            else:
                l=mid+1

        return self.timemap[key][r][1]
