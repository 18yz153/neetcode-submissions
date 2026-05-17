"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            newnode = Node(node.val)
            newnode.neighbors = []
            oldToNew[node]=newnode
            for n in node.neighbors:
                newnode.neighbors.append(dfs(n))
            return newnode

        return dfs(node)