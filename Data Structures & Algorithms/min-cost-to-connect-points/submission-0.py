import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = []
        for i in range(1,len(points)):
            dis = abs(points[0][0]-points[i][0])+abs(points[0][1]-points[i][1])
            dist.append((dis,i))
        heapq.heapify(dist)
        visited=set([0])
        res = 0
        while len(visited)<len(points):
            nxt = heapq.heappop(dist)
            if nxt[1] not in visited:
                visited.add(nxt[1])
                res+=nxt[0]
                for i in range(1,len(points)):
                    if i not in visited:
                        dis = abs(points[nxt[1]][0]-points[i][0])+abs(points[nxt[1]][1]-points[i][1])
                        heapq.heappush(dist,(dis,i))
        return res
