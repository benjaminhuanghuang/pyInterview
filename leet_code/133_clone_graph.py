'''
133. Clone Graph

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
'''

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph_dfs(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None

        dic = {}
        return self.dfs(node, dic)

    def dfs(self, node, dic):
        if node in dic:
            return dic[node]

        newNode = UndirectedGraphNode(node.label)
        dic[node] = newNode

        for n in node.neighbors:
            newNode.neighbors.append(self.dfs(n, dic))

        return newNode

    def cloneGraph_bfs(self, node):
        if not node:
            return None

        queue = []
        dic = {}

        queue.append(node)
        nodeCopy = UndirectedGraphNode(node.label)
        dic[node] = nodeCopy

        while queue:
            node_source = queue.pop(0)

            for neighbor_source in node_source.neighbors:
                if neighbor_source in dic:
                    dic[node_source].neighbors.append(dic[neighbor_source])
                else:
                    neighborCopy = UndirectedGraphNode(neighbor_source.label)
                    dic[node_source].neighbors.append(neighborCopy)
                    dic[neighbor_source] = neighborCopy
                    queue.append(neighbor_source)

        return nodeCopy