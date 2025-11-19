from collections import deque
from typing import List, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        # Queues and visited sets for both oceans
        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        # Pacific: top row and left column
        for j in range(n):
            p_que.append((0, j))
            p_seen.add((0, j))
        for i in range(1, m):          # start at 1 to avoid duplicating (0,0)
            p_que.append((i, 0))
            p_seen.add((i, 0))

        # Atlantic: right column and bottom row
        for i in range(m):
            a_que.append((i, n - 1))
            a_seen.add((i, n - 1))
        for j in range(n - 1):        # up to n-2 to avoid duplicating (m-1, n-1)
            a_que.append((m - 1, j))
            a_seen.add((m - 1, j))

        # BFS (reverse flow): from ocean inward, move to neighbors with height >= current
        def get_coords(que: deque, seen: set):
            while que:
                i, j = que.popleft()
                for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < m and 0 <= c < n and \
                       (r, c) not in seen and \
                       heights[r][c] >= heights[i][j]:
                        seen.add((r, c))
                        que.append((r, c))

        get_coords(p_que, p_seen)
        get_coords(a_que, a_seen)

        # intersection -> convert to list of [i,j]
        res = [[i, j] for (i, j) in p_seen.intersection(a_seen)]
        return res
