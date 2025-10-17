class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n

        curr=2
        prev=1
        for i in range(2, n):
            curr,prev=prev+curr,curr
        return curr

        
