class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def change(r, c): # change the connexted "O" to "T"
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c]!= "O":
                return
            board[r][c] = "T"
            change(r - 1, c)
            change(r + 1, c)
            change(r, c - 1)
            change(r, c + 1)
        
        # Step1: change all boarder connected "O" to "T"
        for r in range(rows): 
            for c in range(cols):
                if board[r][c] == "O" and r in [0, rows -1] or c in [0, cols -1]:
                    change(r, c)
        
        # Step2: change all the "O" to "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # Step3: change "T" back to "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"

        
