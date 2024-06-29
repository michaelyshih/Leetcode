class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # go through every node once in a dfs and continue while children
        # backtrack up parent if parent is unvisited? 
        
        adjacency_list = [[] for _ in range(n)]
        ans = [[] for _ in range(n)]
        
        for edge in edges:
            from_node = edge[0]
            to_node = edge[1]
            adjacency_list[from_node].append(to_node)
        for i in range(n):
            self.find_ancestors_DFS(i, adjacency_list, i, ans)

        return ans

    def find_ancestors_DFS(self, ancestor, adjacency_list, current_node, ans ):
        
        for child_node in adjacency_list[current_node]:
            # Check if the ancestor is already added to avoid duplicates
            if (
                not ans[child_node]
                or ans[child_node][-1] != ancestor
            ):
                ans[child_node].append(ancestor)
                self.find_ancestors_DFS(
                    ancestor, adjacency_list, child_node, ans
                )
    