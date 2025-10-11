class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i , val in enumerate(numbers):
            
            ans= target-numbers[i]
            if ans in seen :
                return (seen[ans]+1,i+1)
            else:
                seen[val]=i
            
        
