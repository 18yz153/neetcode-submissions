import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        vectors = defaultdict(list)
        for t in times:
            frm,to,cost = t
            vectors[frm].append([to,cost])
        start= []
        for to,cost in vectors[k]:
            start.append((cost,to))
        visited = set([k])
        heapq.heapify(start)
        while len(visited)<n and start:
            cost, to = heapq.heappop(start)
            if to not in visited:
                for t,c in vectors[to]:
                    heapq.heappush(start,(c+cost,t))
                visited.add(to)
        if len(visited)<n:
            return -1
        return cost