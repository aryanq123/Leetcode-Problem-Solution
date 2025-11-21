class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longst=0
        for num in s:
            if num-1 not in s:
                total=1

                next_num=num+1
                while next_num in s:
                    next_num+=1
                    total+=1
                longst=max(total,longst)
        return longst
