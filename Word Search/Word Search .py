class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Row ,Col=len(board),len(board[0])
        
        def dfs(r,c,i):
            if len(word)==i:
                return True
            if r<0 or r>=Row or c<0 or c >=Col or board[r][c]=="#" or word[i]!=board[r][c]:
                return 0
            board[r][c]="#"
            res=(dfs(r+1,c,i+1) or
            dfs(r-1,c,i+1) or
            dfs(r,c+1,i+1) or
            dfs(r,c-1,i+1) 
            )
            board[r][c]=word[i]
            return res

        for r in range(Row):
            for c in range(Col):
                if dfs(r,c,0):
                    return True
        return False

        
        
