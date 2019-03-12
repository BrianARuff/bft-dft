# field verticies tha maps vertex labels to edges
# add vertex method
# add edge method


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        self.vertices[key] = set()

    def add_edge(self, key, value):
        if key not in self.vertices:
            print('error: no vertext')
        else:
            self.vertices[key].add(value)

    def bft(self, start):
        queue = [start]
        visited = set()
        while len(queue) > 0:
            for v in self.vertices[queue[0]]:
                if v not in queue and v not in visited:
                    queue.append(v)
            print(f'VISITED: {queue[0]}')
            visited.add(queue.pop(0))
    
    def dft(self, start):
        stack = [start]
        visited = []
        while stack:
            vertex = stack.pop()
            visited.append(vertex)
            for v in self.vertices[vertex]:
                if v not in visited:
                    stack.append(v)
        print(visited)

g = Graph()
g.add_vertex('3')
g.add_vertex('5')
g.add_vertex('6')
g.add_vertex('2')
g.add_vertex('0')
g.add_vertex('1')
g.add_edge('0','1')
g.add_edge('0', '2')
g.add_edge('1', '3')
g.add_edge('2', '5') 
g.add_edge('2', '6')
g.add_edge('3', '5')
g.add_edge('3', '6')
g.dft('0')