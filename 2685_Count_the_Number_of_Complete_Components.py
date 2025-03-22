from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n, edges):
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        count = 0

        def dfs(node, component):
            component.add(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i, component)
                if all(len(graph[node]) == len(component) - 1 for node in component):
                    count += 1

        return count
    
   
# ! Explanation:
# * This function counts the number of complete components in a graph.
# * 1. Create a defaultdict called graph to store the adjacency list of the graph.
# * 2. Populate the graph with the given edges.
# * 3. Initialize an empty set called visited to keep track of visited nodes.
# * 4. Initialize a variable called count to store the number of complete components.
# * 5. Define a depth-first search (DFS) function that takes a node and a component set as arguments.
#     * Add the node to the component set.
#     * Mark the node as visited.
#     * Recursively call the DFS function on the neighbors of the node.
# * 6. Iterate through the nodes in the graph.
#     * If the node has not been visited:
#         * Create an empty set called component.
#         * Call the DFS function on the node to find the component.
#         * Check if all the neighbors of the component are in the component set.
#         * If the condition is met, increment the count.
# * 7. Return the count of complete components.

# ? Time Complexity:
# * The time complexity of this approach is O(n + m), where n is the number of nodes and m is the number of edges.
# * This is because we iterate through all the nodes and edges in the graph during the DFS traversal.

# ? Space Complexity:
# * The space complexity of this approach is O(n), where n is the number of nodes.
# * This is because we use the visited set and component set to keep track of visited nodes and components during the DFS traversal.    