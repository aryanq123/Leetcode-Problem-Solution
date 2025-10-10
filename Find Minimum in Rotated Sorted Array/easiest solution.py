class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=nums
        n.sort()
        return nums[0]
