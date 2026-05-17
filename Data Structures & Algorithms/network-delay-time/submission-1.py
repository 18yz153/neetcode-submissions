import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        vectors = defaultdict(list)
        for t in times:
            frm,to,cost = t
            vectors[frm].append([to,cost])
        start= [(0,k)]
        visited = set([])
        heapq.heapify(start)
        res = 0
        while len(visited)<n and start:
            cost, to = heapq.heappop(start)
            if to not in visited:
                for t,c in vectors[to]:
                    if t not in visited:
                        heapq.heappush(start,(c+cost,t))
                
                res = cost
                visited.add(to)
        if len(visited)<n:
            return -1
        return res