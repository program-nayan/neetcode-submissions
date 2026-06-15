class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])

        for i in range(9):
            col_set = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in col_set:
                    return False
                col_set.add(board[j][i])
        
        for i in range(9):
            box_set = set()
            for j in range(9):
                row = j % 3 + (i // 3) * 3
                col = j // 3 + (i % 3)*3
                if board[row][col] == ".":
                    continue
                elif board[row][col] in box_set:
                    return False
                box_set.add(board[row][col])
        return True