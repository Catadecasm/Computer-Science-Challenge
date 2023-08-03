"""The main loop in the shortestPathLength function iterates over all nodes in the graph once, which takes O(V) time, where V is the number of nodes (vertices) in the graph.
The DFS algorithm has a time complexity of O(V + E) because each node and edge is visited once during the traversal.
"""

"""The space complexity mainly depends on the visitedNode array used to keep track of visited nodes during DFS.
 This array has a size of V (number of nodes) and is created and reset for each DFS run. Therefore, it contributes O(V) space complexity to each DFS call.
"""
#Time complexity is O(V * (V + E)), and the space complexity is O(V)

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        def DepthFirstSearch(current, depthLevel, visitedNode):
            count = depthLevel
            visitedNode[current] = True
            for i in graph[current]:
                if not visitedNode[i]:
                    count = max(count, DepthFirstSearch(i, depthLevel + 1, visitedNode))
                    if count == len(graph) - 1:
                        break
            visitedNode[current] = False
            return count

        count2 = 0
        for i in range(len(graph)):
            visitedNode = [False] * len(graph)
            count2 = max(count2, DepthFirstSearch(i, 0, visitedNode))

        return 2 * (len(graph) - 1) - count2
