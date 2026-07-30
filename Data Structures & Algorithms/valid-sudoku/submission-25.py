class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            d = {}
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                num = board[i][j]
                if num in d:
                    return False
                d[num] = 1
        
        for i in range(len(board)):
            d = {}
            for j in range(len(board[i])):
                if board[j][i] == '.':
                    continue
                num = board[j][i]
                if num in d:
                    return False
                d[num] = 1

        def round_judge(i: int, j: int) -> bool:
            print(f"round_judge:{i} {j}")
            d = {}
            for x in range(3):
                for y in range(3):
                    num = board[i+x][j+y]
                    if num == '.':
                        continue
                    if num in d:
                        return False
                    d[num] = 1
            return True

        li = [(0,0), (0,3), (0,6)
        , (3,0), (3,3), (3,6)
        , (6,0), (6,3), (6,6)]

        for x,y in li:
            if not round_judge(x,y):
                return False

        return True

            
        