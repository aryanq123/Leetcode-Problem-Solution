class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        max_area=0
        l=0
        r=n-1
        while l<r:
            w=r-l
            h=min(height[l],height[r])
            area=w*h
            max_area=max(area,max_area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_area
        
