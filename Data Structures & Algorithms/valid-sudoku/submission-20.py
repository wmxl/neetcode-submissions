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
            num = board[i][j]
            if num != '.' and num in d:
                return False
            else:
                d[num] = 1
            print(num, end="")
            num = board[i][j+1]
            if num != '.' and num in d:
                return False
                d[num] = 1
            print(num, end="")
            num = board[i][j+2]
            if num != '.' and num in d:
                return False
            else:
                d[num] = 1
            print(num)

            num = board[i+1][j]
            if num != '.' and num in d:
                return False
            else:
                d[num] = 1
            print(num, end="")
            num = board[i+1][j+1]
            if num != '.' and num in d:
                return False
            else:
                d[num] = 1
            print(num, end="")
            num = board[i+1][j+2]
            if num != '.' and num in d:
                return False
            else:
                d[num] = 1
            print(num)

            num = board[i+2][j]
            if num != '.' and num in d:
                return False
            else:
                d[num] = 1
            print(num, end="")
            num = board[i+2][j+1]
            if num != '.' and num in d:
                return False
            else:
                d[num] = 1
            print(num, end="")
            num = board[i+2][j+2]
            if num != '.' and num in d:
                return False
            else:
                d[num] = 1
            print(num)
            print(d)
            return True


        li = [(0,0), (0,3), (0,6)
        , (3,0), (3,3), (3,6)
        , (6,0), (6,3), (6,6)]

        for x,y in li:
            if not round_judge(x,y):
                return False

        return True

            
        