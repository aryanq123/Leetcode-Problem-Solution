class Solution:
    def rob(self, nums: List[int]) -> int:
        prev,curr=0,0
        for num in nums:
            temp=max(prev,curr+num)
            curr=prev
            prev=temp
        return prev
        

        
