class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        res=nums1+nums2
        res.sort()
        if len(res)==1:
            return res[0]
        n=len(res)
        v=len(res)-1
        if n%2==0:
            median=(1+n)//2
            ans=(res[median-1]+res[median])/2
            return ans
        else:
            ans=v //2
            return res[ans]
