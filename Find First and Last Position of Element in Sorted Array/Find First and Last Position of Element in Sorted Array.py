class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftnum(nums,target):
            left=-1
            l,r=0,len(nums)-1
            while l <= r:
                mid=(l+r)//2
                if nums[mid]==target:
                    left=mid
                    r=mid-1
                elif nums[mid] > target:
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
            return left

        def rightnum(nums,target):
            right=-1
            l,r=0,len(nums)-1
            while l <= r:
                mid=(l+r)//2
                if nums[mid]==target:
                    right=mid
                    l=mid+1
                elif nums[mid] > target:
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
            return right
    
        left=leftnum(nums,target)
        right=rightnum(nums,target)

        return(left,right)
    
