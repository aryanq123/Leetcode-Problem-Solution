class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_Sum = float('-inf')   # ✅ correct way to write negative infinity
        current_sum = 0           # ✅ start with 0, not nums[0]
        
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_Sum = max(max_Sum, current_sum)
        
        return max_Sum
