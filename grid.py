from collections import deque

class Grid:
  def __init__(self, rows = 0, columns = 0) -> None:
    self.rows = rows
    self.columns = columns
    self.maximum_squares = rows * columns
    self.default_value = 1
    self.grid = self.generate_grid()
    self.column_queue = deque([])
    self.row_queue = deque([])


  def generate_grid(self, grid = []):
    for row in range(self.rows):
      new_row = [self.default_value] * self.columns
      grid.append(new_row)
    return grid
  
  def display_grid(self):
    grid_to_string = ""

    for row in self.grid:
      string_to_row = f"{row}"
      print(string_to_row)

  def add_blockers(self, row, colStart, colEnd):
    if row < 1 or row > self.rows + 1:
      return print(f"Please select row within range of 1 - {self.rows}")
      
    if colStart < 1 or colStart > self.columns + 1:
      return print(f"Please select a column within range of 1 - {self.columns}")

    if colEnd < colStart:
      return print("The endpoint must be equal or higher than the startpoint")

    if colEnd > self.columns:
      return print(f"The endpoint must be less than or equal to {self.columns}")

    working_row = self.grid[row - 1]

    for column in range(colStart, colEnd + 1):
      # 0 indicates a cell that cannot be traversed
      working_row[column - 1] = 0

  def findShortestPath(self, start = [0, 0], end = [0, 0]):
    move_count = 0
    nodes_in_current_layer = 1
    nodes_in_next_layer = 0

    reached_end = False

    visitedNodes = self.generate_grid()

    north_south_direction_vector = [-1, 1, 0, 0] # Move North or South
    east_west_direction_vector = [0, 0, 1, -1]

    startingNode = self.grid[start[0]][start[1]]
    endNode = self.grid[end[0]][end[1]]

    # Start on first node
    

    # Log each node I can touch to memory (only 4 coordinates N.S.E.W.)

    # Find
  
  def breadthFirstGridSearch(self, start_row, start_column):
    row_queue = self.row_queue.append(start_row)
    column_queue = self.column_queue.append(start_column)

new_grid = Grid(10, 10)

new_grid.add_blockers(4, 4, 6)
new_grid.add_blockers(5, 4, 4)
new_grid.add_blockers(5, 6, 6)
new_grid.add_blockers(6, 4, 4)
new_grid.add_blockers(6, 6, 6)


new_grid.display_grid()