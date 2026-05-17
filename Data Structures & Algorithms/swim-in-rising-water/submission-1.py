import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set([(0,0)])
        heap = [(grid[0][0],(0,0))]
        heapq.heapify(heap)
        while heap:
            val, point = heapq.heappop(heap)
            if point == (len(grid)-1,len(grid[0])-1):
                return val
            direction = [[1,0],[0,1],[-1,0],[0,-1]]
            for dx,dy in direction:
                newx = point[0]+dx
                newy= point[1]+dy
                if 0<=newx<len(grid) and 0<=newy<len(grid[0]):
                    if (newx,newy) not in visited:
                        newval = max(val,grid[newx][newy])
                        visited.add((newx,newy))
                        heapq.heappush(heap,(newval,(newx,newy)))