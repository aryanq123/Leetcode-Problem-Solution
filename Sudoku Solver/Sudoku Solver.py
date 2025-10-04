class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def isvalid(nums,row,col):
            for i in range(9):
                if (board[row][i]==nums
                or board[i][col]==nums
                or board[3*(row//3)+i//3][3*(col//3)+i%3]==nums):
                    return False
            return True
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j]==".":
                        for nums in map(str,range(1,10)):
                            if isvalid(nums,i,j):
                                board[i][j]=nums
                                if  solve():
                                    return True
                                board[i][j]="."
                        return False
            return True
        solve()
        """
        Do not return anything, modify board in-place instead.
        """
        
