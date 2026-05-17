from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seq = [x for x in range(n)]
        count = n
        def find(i):
            if i!=seq[i]:
                seq[i]=find(seq[i])
            return seq[i]
        for i in range(len(edges)):
            f,t=edges[i]
            root_i = find(f)
            root_j = find(t)
            if root_i != root_j:
                seq[root_j] = root_i
                count-=1
        return count

