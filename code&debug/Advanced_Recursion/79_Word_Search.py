class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(board, word, i, j, idx):

            if i < 0 or i>= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
                return False

            if idx == len(word) -1:
                return True 
            
            temp = board[i][j]
            
            board[i][j] = "*"

            res= dfs(board, word, i+1, j, idx+1) or \
                 dfs(board, word, i-1, j, idx+1) or \
                 dfs(board, word, i, j+1, idx+1) or \
                 dfs(board, word, i, j-1, idx+1)
            
            board[i][j] = temp

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j, 0):
                    return True

        return False
