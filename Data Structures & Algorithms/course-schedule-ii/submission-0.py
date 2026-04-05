class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap={}
        for i in range(numCourses):
            courseMap[i] = []
        for c, req  in prerequisites:
            courseMap[c].append(req)
        ordering = []
        visited = set()
        path = []
        def dfs(c):
            if c in visited:
                return True
            if c in path:
                return False
            path.append(c)
            for dep in courseMap[c]:
                if not dfs(dep):
                    return False
            path.pop()
            visited.add(c)
            ordering.append(c)
            return True
        for c in range(numCourses):
            # path.append(c)
            if not dfs(c):
                return []
            # path.pop()
        return ordering
            