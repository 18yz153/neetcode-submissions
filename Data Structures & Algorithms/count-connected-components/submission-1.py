from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vectors = defaultdict(list)
        for f,t in edges:
            vectors[f].append(t)
            vectors[t].append(f)
        visited = set()
        res = 0
        while len(visited)< n:
            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    res+=1
                    stack=[i]
                    while stack:
                        f=stack.pop()
                        for t in vectors[f]:
                            if t not in visited:
                                visited.add(t)
                                stack.append(t)
        
        return res
