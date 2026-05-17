from collections import Counter,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        t = []
        for key,value in d.items():
            t.append((-value,key))
        heapq.heapify(t)
        visited = deque()
        res = 0 
        while t or visited:
            
            res +=1
            if t:
                value, key = heapq.heappop(t)
                value += 1
                if value !=0:
                    visited.append((value,res+n,key))
            if visited and visited[0][1] == res:
                val,_,key = visited.popleft()
                heapq.heappush(t,(val,key))
        return res

            

            

