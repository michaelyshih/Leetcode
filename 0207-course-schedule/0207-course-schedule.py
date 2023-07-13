from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preCourse = defaultdict(list)
        for pre in prerequisites:
             preCourse[pre[0]].append(pre[1])
        print(preCourse)
        visited = set()
        
        def _dfs(crs):
            if crs in visited: 
                return False 
            if preCourse[crs] == []:
                return True
            visited.add(crs)
            for pre in preCourse[crs]:
                if not _dfs(pre) : return False
            visited.remove(crs)
            preCourse[crs] = []
            return True
        for crs in range(numCourses):
            if not _dfs(crs): return False
        return True
        
#         q = deque()
#         q.append(prerequisites[0][0])
        
        
        
#         while len(q) > 0:
#             if numCourses <= 0:
#                 return False
#             curr = q.popleft()
#             numCourses -= 1
#             if curr in visited: 
#                 return False
#             for course in preCourse[curr]:
#                 print("required:", course)
#                 q.append(course)
#             visited.add(curr)

#         return True
#         indegree = [0] * numCourses
#         adj = [[] for _ in range(numCourses)]

#         for prerequisite in prerequisites:
#             adj[prerequisite[1]].append(prerequisite[0])
#             indegree[prerequisite[0]] += 1

#         queue = deque()
#         for i in range(numCourses):
#             if indegree[i] == 0:
#                 queue.append(i)

#         nodesVisited = 0
#         while queue:
#             node = queue.popleft()
#             nodesVisited += 1

#             for neighbor in adj[node]:
#                 indegree[neighbor] -= 1
#                 if indegree[neighbor] == 0:
#                     queue.append(neighbor)

#         return nodesVisited == numCourses                