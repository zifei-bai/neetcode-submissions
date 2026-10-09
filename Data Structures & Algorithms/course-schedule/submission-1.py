class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        g = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            in_degree[u] += 1
            g[v].append(u)
        if all(in_d != 0 for in_d in in_degree):
            return False
        print(in_degree)
        dq = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                dq.append(i)
        count = 0
        processed = []
        while dq:
            if count > numCourses:
                return False
            course = dq.popleft()
            processed.append(course)
            for depend in g[course]:
                in_degree[depend] -= 1
                if in_degree[depend] == 0:
                    dq.append(depend)
            count += 1
        # print(f'dq: {dq}, count: {count}')
        while len(dq) == 0 and len(processed) < numCourses:
            return False
        return True
