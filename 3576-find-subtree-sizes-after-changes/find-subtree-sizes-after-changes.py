
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Build original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Modified parent array
        new_parent = parent[:]

        # Stores nearest ancestor for each character
        last_seen = [-1] * 26

        # Stores previous last_seen value for backtracking
        old_seen = [-1] * n

        # Iterative DFS: (node, exiting)
        stack = [(0, False)]

        while stack:
            node, exiting = stack.pop()
            c = ord(s[node]) - ord('a')

            if not exiting:
                old_seen[node] = last_seen[c]

                # Find closest matching ancestor
                if node != 0 and last_seen[c] != -1:
                    new_parent[node] = last_seen[c]

                # Update current path
                last_seen[c] = node

                stack.append((node, True))

                for child in reversed(children[node]):
                    stack.append((child, False))

            else:
                # Restore previous state while backtracking
                last_seen[c] = old_seen[node]

        # Build modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Calculate subtree sizes using postorder
        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        # Initially, every node has size 1
        ans = [1] * n

        # Process children before their parents
        for node in reversed(order):
            if node != 0:
                ans[new_parent[node]] += ans[node]

        return ans
