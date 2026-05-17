from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        start = []
        m, n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    start.append((i,j))
        start = deque(start)
        step = 1
        while start:
            for _ in range(0,len(start)):
                s = start.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for d in directions:
                    newi=d[0]+s[0]
                    newj = d[1]+s[1]
                    if 0<=newi<m and 0<=newj <n:
                        if grid[newi][newj] == 2147483647:
                            grid[newi][newj] = step
                            start.append((newi,newj))
            step +=1
        