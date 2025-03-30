from cell import Cell
from graphics import Window
from maze import Maze


def main():
      num_rows = 12
      num_cols = 16
      screen_x = 800
      screen_y = 600
      margin = 50
      cell_size_x = (screen_x - margin * 2) / num_cols
      cell_size_y = (screen_y - margin * 2) / num_rows
      win = Window(screen_x, screen_y)
      maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

      maze._create_cells()

      win.wait_for_close()

main()      