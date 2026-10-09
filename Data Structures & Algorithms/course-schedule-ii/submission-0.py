class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        g = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            in_degree[u] += 1
            g[v].append(u)
        schedule = []
        dq = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                dq.append(i)
        while dq:
            course = dq.popleft()
            schedule.append(course)
            for depend in g[course]:
                in_degree[depend] -= 1
                if in_degree[depend] == 0:
                    dq.append(depend)
        if len(schedule) == numCourses:
            return schedule
        return []