"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    # T: O(n), S: O(n)
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        # Dictionary to store the mapping from original node to its clone
        cloned_nodes = {}

        def dfs(node):
            # If the node is already cloned, return it
            if node in cloned_nodes:
                return cloned_nodes[node]

            # Create a new clone for the current node
            clone = Node(node.val)
            cloned_nodes[node] = clone

            # Recursively clone all the neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        # Start DFS from the original node
        return dfs(node)