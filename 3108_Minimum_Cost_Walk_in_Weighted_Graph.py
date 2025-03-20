class Solution:
    def findRoot(self, node, parent):
        if parent[node] != node:
            parent[node] = self.findRoot(parent[node], parent)

        return parent[node]    

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = list(range(n))
        minPathCost = [-1] * n

        for source, target, weight in edges:
            sourceRoot = self.findRoot(source, parent)
            targetRoot = self.findRoot(target, parent)

            minPathCost[sourceRoot] = weight if minPathCost[sourceRoot] == -1 else minPathCost[sourceRoot] & weight
            minPathCost[targetRoot] = weight if minPathCost[targetRoot] == -1 else minPathCost[targetRoot] & weight

            if sourceRoot != targetRoot:
                parent[sourceRoot] = targetRoot
                minPathCost[targetRoot] &= minPathCost[sourceRoot]

        result = []
        for start, end in query:
            if start == end:
                result.append(0)
            elif self.findRoot(start, parent) != self.findRoot(end, parent):
                result.append(-1)
            else:
                result.append(minPathCost[self.findRoot(start, parent)])

        return result
    
    
# ! Explanation:
# * This function calculates the minimum cost of a walk in a weighted graph.
# * 1. Initialize the parent list with the indices of the nodes.
# * 2. Initialize the minPathCost list with -1 values for each node.
# * 3. Iterate through the edges of the graph.
#     * Find the root of the source and target nodes.
#     * Update the minimum path cost of the source and target nodes.
#     * If the source and target nodes have different roots, update the parent of the source node and the minimum path cost of the target node.
# * 4. Initialize an empty list called result.
# * 5. Iterate through the queries.
#     * If the start and end nodes are the same, append 0 to the result list.
#     * If the start and end nodes have different roots, append -1 to the result list.
#     * Otherwise, append the minimum path cost of the start node to the result list.
# * 6. Return the result list.

# ? Time Complexity:
# * The time complexity of this approach is O(n + m + q), where n is the number of nodes, m is the number of edges, and q is the number of queries.
# * This is because we iterate through the edges once to update the parent and minimum path cost lists and iterate through the queries to find the minimum path cost of each query.

# ? Space Complexity:
# * The space complexity of this approach is O(n), where n is the number of nodes.
# * This is because we use the parent and minPathCost lists to store the parent nodes and minimum path costs of each node.    
    