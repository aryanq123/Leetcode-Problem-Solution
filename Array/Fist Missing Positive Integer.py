class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        n=len(nums)
        expected =1
        for num in nums:
            if num==expected:
                expected+=1
            elif num>num:
                return expected
        return expected
