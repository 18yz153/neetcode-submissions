from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) !=n-1:
            return False
        seen= set([0])
        vector=defaultdict(list)
        for i in range(0,len(edges)):
            u,v=edges[i]
            vector[u].append(v)
            vector[v].append(u)
        queue =deque([0])
        while queue:
            for _ in range(len(queue)):
                s=queue.popleft()
                for e in vector[s]:
                    if e not in seen:
                        queue.append(e)
                        seen.add(e)
        return len(seen) ==n

        