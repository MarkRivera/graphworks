from collections import defaultdict

class Graph:
  def __init__(self) -> None:
    # use dict to represent graph in an   
    self.graph = defaultdict(list) # { a: ["b", "c"] ... etc }
    self.edges = []

  # Add Edges between points
  def addEdge(self, point, secondpoint):
    self.graph[point].append(secondpoint)
  

  def generate_edges(self):
    for node in self.graph:
      # For connected nodes
      for connectedNode in self.graph[node]:

        # edge should exist
        self.edges.append((node, connectedNode))
    
    return self.edges

  def findPath(self, start, end):
    path = [start]
    visited = []
    queue = []

    # Is my starting point the same as my end point? If so, I'm done! :)
    if start == end:
      path.append(start)
      return 

    def breadthFirstSearch(node):
      # Add my node to a visited list, to prevent going to nodes I've already been to
      if node not in visited:
        visited.append(node)
      else:
        return

      # Check which nodes I am connected to and add them to a queue
      for neighbor in self.graph[node]:
        queue.append(neighbor)

      # process those nodes
      while queue:
        breadthFirstSearch(queue.pop(0))

    breadthFirstSearch(start)

    return path
  
directedGraph = Graph()

directedGraph.addEdge("a", "b")
directedGraph.addEdge("a", "c")
# directedGraph.addEdge("b", "c")
# directedGraph.addEdge("c", "d")
# directedGraph.addEdge("c", "e")
# directedGraph.addEdge("c", "f")
# directedGraph.addEdge("d", "g")
# directedGraph.addEdge("d", "e")


print(directedGraph.generate_edges())

print(directedGraph.findPath("a", "c"))

print(directedGraph.graph)