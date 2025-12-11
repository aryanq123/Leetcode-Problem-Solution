class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r,t,b,res=0,len(matrix[0]),0,len(matrix),[]
        while l<r and t<b:
            for i in range(l,r):
                res.append(matrix[t][i])
            t+=1
            for j in range(t,b):
                res.append(matrix[j][r-1])
            r -=1
            if not (l<r and t<b):break
            for  j in range(r-1,l-1 ,-1):
                res.append(matrix[b-1][j])
            b-=1
            for i in range(b-1,t-1,-1):
                res.append(matrix[i][j])
            l+=1
        return res


        
