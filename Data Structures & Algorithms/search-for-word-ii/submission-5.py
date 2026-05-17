from collections import deque
class tree:
    def __init__(self):
        self.child = {}
        self.res =''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = tree()
        for word in words:
            node = root
            for j in range(0,len(word)):
                if word[j] not in node.child:
                    node.child[word[j]] = tree()
                    node = node.child[word[j]]
                else:
                    node = node.child[word[j]]
                if j ==len(word)-1:
                    node.res = word
        result=set()
        def dfs(i,j,node,visited):
            if node.res !='':
                result.add(node.res)
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for dx,dy in directions:
                newi,newj=i+dx,j+dy
                v=(newi,newj)
                if 0<=newi<len(board) and 0<=newj<len(board[0]) and v not in visited:
                    newchar = board[newi][newj]
                    if newchar in node.child:
                        visited.add((newi,newj))
                        dfs(newi,newj,node.child[newchar],visited)
                        visited.remove((newi,newj))
        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] in root.child:
                    visited= set([(i,j)])
                    dfs(i,j,root.child[board[i][j]],visited)
        return list(result)