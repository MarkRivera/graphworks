
class Grid:
  def __init__(self, rows = 0, columns = 0) -> None:
    self.rows = rows
    self.columns = columns
    self.default_value = 1
    self.grid = self.generate_grid()
    

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


new_grid = Grid(10, 10)

new_grid.add_blockers(4, 4, 6)
new_grid.add_blockers(5, 4, 4)
new_grid.add_blockers(5, 6, 6)
new_grid.add_blockers(6, 4, 4)
new_grid.add_blockers(6, 6, 6)


new_grid.display_grid()