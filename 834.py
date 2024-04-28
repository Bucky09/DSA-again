class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Graph initialization
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Arrays to store subtree size and distance sum
        count = [1] * n
        answer = [0] * n

        # Post-order DFS to populate count and answer
        def postOrder(node, parent):
            for child in graph[node]:
                if child != parent:
                    postOrder(child, node)
                    count[node] += count[child]
                    answer[node] += answer[child] + count[child]

        # Pre-order DFS to adjust answer based on parent's data
        def preOrder(node, parent):
            for child in graph[node]:
                if child != parent:
                    answer[child] = answer[node] - count[child] + n - count[child]
                    preOrder(child, node)

        # Perform post-order and pre-order traversals
        postOrder(0, -1)  # Starting from node 0 and assuming no parent with -1
        preOrder(0, -1)

        return answer
        
