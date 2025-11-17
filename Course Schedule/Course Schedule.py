from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=defaultdict(list)
        courses=prerequisites
        for a,b in courses:
            g[a].append(b)

        unvisited,visiting,visited=0,1,2
        states=[unvisited]*numCourses
        def dfs(node):
            state=states[node]
            if state==visiting:
                return False
            if state==visited:
                return True
            states[node]=visiting
            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node]=visited
            return True
        for i in range(numCourses):
            if states[i]==unvisited:
                if not dfs(i):
                    return False
        return True
