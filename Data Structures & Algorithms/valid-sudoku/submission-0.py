from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blks = defaultdict(set)
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] !='.':
                    val = board[i][j]
                    ind = (i//3*3)+j//3
                    print(ind)
                    if val in rows[i] or val in cols[j] or val in blks[ind]:
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    blks[ind].add(val)
        return True