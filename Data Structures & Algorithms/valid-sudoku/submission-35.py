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

        dd = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j] 
                if num == '.':
                    continue
                index = int((i // 3) * 3 + (j // 3))
                if index not in dd:
                    print(f'{i}-{j} dd[{index}]=empty')
                    dd[index] = {}
                if num in dd[index]:
                    return False
                dd[index][num] = 1
        return True

            
        