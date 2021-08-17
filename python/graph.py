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

  def findPath(self, start, end, path = []):
    path = path + [start]

    # Is my starting point the same as my end point? If so, I'm done! :)
    if start == end:
      return path

    shortest = None

    # We're going to go through each node in the graph, starting from the start node til the end node:
    for node in self.graph[start]:

      # If the node we are on is not in the path go visit it
      if node not in path:

        # Using recursion over iteration
        newPath = self.findPath(node, end, path)

        # If newPath exists (Not falsy)
        if newPath:
          # Check if shortest is None OR if length of newPath is less than current shortest
          if not shortest or len(newPath) < len(shortest):

            # if our new path length is lesser than the current shortest, replace it
            shortest = newPath
    
    return shortest

  
directedGraph = Graph()

directedGraph.addEdge("a", "b")
directedGraph.addEdge("a", "c")
directedGraph.addEdge("b", "c")
directedGraph.addEdge("c", "d")
directedGraph.addEdge("c", "e")
directedGraph.addEdge("c", "f")
directedGraph.addEdge("d", "g")
directedGraph.addEdge("d", "e")


print(directedGraph.generate_edges())

print(directedGraph.findPath("a", "g"))

print(directedGraph.graph)