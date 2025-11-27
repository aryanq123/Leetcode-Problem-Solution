class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda intervals :intervals[0])
        merges=[]
        for interval in intervals:
            if  not merges or interval[0]>merges[-1][1]:
                merges.append(interval)
            else:
                merges[-1]=[merges[-1][0], max(interval[1], merges[-1][1])]
        return merges

