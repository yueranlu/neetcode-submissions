class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check eachh num in ech row
        #check each first row
        for row in range(len(board)):
            seen = set()
            # check each number in the row
            for i in range(len(board[0])):
                if board[row][i] == ".":
                    continue
                
                if board[row][i] in seen:
                    return False

                seen.add(board[row][i])



        # check num in each column
        for col in range(len(board[0])):
            seen = set()
            for j in range(len(board)):
                if board[j][col] == ".":
                    continue
                
                if board[j][col] in seen:
                    return False

                seen.add(board[j][col])

        # check square
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = ((square// 3) * 3) + i
                    col = ((square % 3) * 3) + j

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True