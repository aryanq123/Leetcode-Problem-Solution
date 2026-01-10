class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i , n in enumerate(nums):
            nums[i]=str(n)
        def compare(s1,s2):
            if s1+s2>s2+s1:
                return -1
            else:
                return 1
        nums=sorted(nums,key=cmp_to_key(compare))
        return str(int("".join(nums)))   
