from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        rows = [set() for _ in range(row)]
        cols = [set() for _ in range(col)]
        sqrs = defaultdict(set)

        for i in range(row):
            for j in range(col):
                if board[i][j]==".":
                    continue
                elem = int(board[i][j])
                if (elem in rows[i] or
                    elem in cols[j] or 
                    elem in sqrs[(i//3,j//3)]):
                    return False
                else:
                    rows[i].add(elem)
                    cols[j].add(elem)
                    sqrs[(i//3,j//3)].add(elem)
        return True 
        