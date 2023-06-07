class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
#         passed = set([])
#         obtainedKeys = set([0])
        
#         def _dfs(rooms, obtainedKeys, passed):

#             for roomNum, room in enumerate(rooms):
#                 if not roomNum in passed and roomNum in obtainedKeys:
#                     print("checking room:", roomNum)
#                     passed.add(roomNum)
#                     print("passed:", list(passed))
#                     for key in room:
#                         print("nextrooms:", key)
#                         obtainedKeys.add(key)
#                         _dfs(rooms,obtainedKeys, passed)
#                     if len(passed) == len(rooms): return True
                    
#             return False 
        
#         return _dfs(rooms,obtainedKeys, passed)
        visited = set()
        def _dfs(room):
            visited.add(room)
            for i in rooms[room]:
                if i not in visited:
                    _dfs(i)
        _dfs(0)
        
        return len(visited) == len(rooms)
        
                