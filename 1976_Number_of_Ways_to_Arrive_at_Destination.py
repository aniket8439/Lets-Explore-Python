from typing import List
from collections import defaultdict
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Build the graph
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Dijkstra's initialization
        min_heap = [(0, 0)]  # (time, node)
        shortest_time = [float('inf')] * n
        pathCount = [0] * n
        shortest_time[0] = 0
        pathCount[0] = 1

        while min_heap:
            curr_time, u = heapq.heappop(min_heap)

            # Skip if we already found a better time
            if curr_time > shortest_time[u]:
                continue

            for v, t in graph[u]:
                new_time = curr_time + t

                if new_time < shortest_time[v]:
                    shortest_time[v] = new_time
                    pathCount[v] = pathCount[u]
                    heapq.heappush(min_heap, (new_time, v))

                elif new_time == shortest_time[v]:
                    pathCount[v] = (pathCount[v] + pathCount[u]) % MOD

        return pathCount[n - 1] % MOD
    
    
# ! Explanation:    
# * This function counts the number of paths from the starting node to the ending node in a graph.
# * 1. Define the MOD value for the modulo operation.
# * 2. Create a defaultdict called graph to store the adjacency list of the graph.
# * 3. Populate the graph with the given roads.
# * 4. Initialize a min heap called min_heap with the starting node and time.
# * 5. Initialize two lists, shortest_time and pathCount, with infinity and zero values for each node, respectively.
# * 6. Set the shortest time and path count of the starting node to zero and one, respectively.
# * 7. While the min heap is not empty:
#     * Pop the current time and node from the min heap.
#     * Skip if we already found a better time for the node.
#     * Iterate through the neighbors of the node.
#         * Calculate the new time.
#         * If the new time is less than the shortest time of the neighbor:
#             * Update the shortest time of the neighbor.
#             * Update the path count of the neighbor.
#             * Push the new time and neighbor to the min heap. 
#         * If the new time is equal to the shortest time of the neighbor:
#             * Update the path count of the neighbor.
# * 8. Return the path count of the ending node modulo MOD.

# ? Time Complexity:
# * The time complexity of this approach is O((n + m) * log(n)), where n is the number of nodes and m is the number of edges.
# * This is because we iterate through all the nodes and edges in the graph and use a min heap for the Dijkstra's algorithm.

# ? Space Complexity:
# * The space complexity of this approach is O(n), where n is the number of nodes.
# * This is because we use the graph, min_heap, shortest_time, and pathCount lists to store the graph, min heap, shortest time, and path count of each node.    