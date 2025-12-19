class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        Rows , Cols=len(board),len(board[0])
        def countNeighbors(r,c):
            nei=0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if i<0 or i>=Rows or j>=Cols or j<0 or (i==r and j==c):
                        continue
                    if  board[i][j] in [1,3]:
                        nei+=1
            return nei

        #padd1
        for r in range(Rows):
            for c in range(Cols):
                nei= countNeighbors(r,c)
                if board[r][c]==1:
                    if nei==2 or nei==3:
                        board[r][c]=3
                    else:
                        board[r][c]=1
                elif board[r][c]==0:
                    if nei==3:
                        board[r][c]=2

        #second pass 
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] in [2,3]:
                    board[r][c]=1
                else:
                    board[r][c]=0
                
                
