# dfs
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return False
        if len(edges) != n - 1:
            return False

        graph = collections.defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        visited = [False for _ in range(n)]
        circle = self.has_circle(-1, 0, graph, visited)
        return all(visited) and not circle

    def has_circle(self, prev, curr, graph, visited):
        if visited[curr]:
            return True
        visited[curr] = True
        for neighbor in graph[curr]:
            if prev == neighbor:
                continue
            if self.has_circle(curr, neighbor, graph, visited):
                return True
        return False

# bfs
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        visited = [False for _ in range(n)]
        circle = self.has_circle(0, graph, visited)
        print(visited, circle)
        return all(visited) and not circle

    def has_circle(self, node, graph, visited):
        q = collections.deque([node])
        while q:
            curr = q.popleft()
            if visited[curr]:
                return True
            visited[curr] = True
            for neighbor in graph[curr]:
                q.append(neighbor)
                graph[neighbor].remove(curr)
        return False

# union find
class UnionFind:
    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.count = n

    def find(self, node):
        if node == self.father[node]:
            return node
        self.father[node] = self.find(self.father[node])
        return self.father[node]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.count -= 1

    def query(self):
        return self.count

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for start, end in edges:
            if uf.find(start) == uf.find(end):
                return False
            uf.union(start, end)

        return uf.query() == 1
