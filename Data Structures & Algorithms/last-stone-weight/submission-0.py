import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>=2:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            diff = s1 - s2
            heapq.heappush(stones,diff)
        return -stones[0]
