class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}  
        output = []
        output_set = set()
        def insert(word):
            node = root
            for w in word:
                if w not in node:
                    node[w] = {}
                node = node[w]
            node[1]= True 
        
        for word in words:
            insert(word)

        m, n = len(board), len(board[0])

        def dfs(i, j, node, word_list, v):
            if i < 0 or j < 0 or i >= m or j >= n: return
            if v[i][j]: return

            x = board[i][j]
            v[i][j] = True   
            if x in node:  
                word_list.append(x)
                if 1 in node[x]:
                    word = "".join(word_list)
                    output_set.add(word)

                dfs(i, j+1, node[x], word_list, v)
                dfs(i+1, j, node[x], word_list, v)
                dfs(i-1, j, node[x], word_list, v)
                dfs(i, j-1, node[x], word_list, v)
                word_list.pop()
            v[i][j] = False
            
        v = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x = board[i][j] 
                if x in root:
                    dfs(i, j, root, [], v)

        return list(output_set)