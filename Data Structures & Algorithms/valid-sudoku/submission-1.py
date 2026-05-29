class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for i in range(length):
            for j in range(length):
                # check row and column
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3,j//3)]:
                    return False
                if board[i][j] == '.':
                    continue
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3, j//3)].add(board[i][j])
        return True

                
               
                
                