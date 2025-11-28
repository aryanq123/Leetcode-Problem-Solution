class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval:interval[0])
        marges=[]
        for interval in intervals:
            if  not marges or marges [-1][1]<interval[0]:
                marges.append(interval)

            else:
                marges[-1]=[marges[-1][0],max(marges[-1][1],interval[1])]
        return marges
        
