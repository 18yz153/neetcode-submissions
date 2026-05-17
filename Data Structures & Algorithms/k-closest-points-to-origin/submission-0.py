import heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for cord in points:
            x,y= cord
            dis = (x)**2 + (y)**2
            distance.append((dis,cord))
        heapq.heapify(distance)
        res = []
        while len(res)<k:
            dis = heapq.heappop(distance)
            cord = dis[1]
            res.append(cord)
        return res

