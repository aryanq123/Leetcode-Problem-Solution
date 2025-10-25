class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(self.helper(nums[1:]),self.helper(nums[:-1]),nums[0])
 

    def helper(self,nums):
        curr,prev=0,0
        for num in nums:
            temp=max(prev,curr+num)
            curr=prev
            prev=temp
        return prev
