import time
from cell import Cell


class Maze:
      # x, y represents the top and left position of the maze
      def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
      ):
            self._cells = []
            self._x1 = x1
            self._y1 = y1
            self._num_rows = num_rows
            self._num_cols = num_cols
            self._cell_size_x = cell_size_x
            self._cell_size_y = cell_size_y
            self._win = win
      
      # create column-major grid -> cells[col][row]
      def _create_cells(self):
            for _ in range(self._num_cols):
                  row = []
                  for _ in range(self._num_rows):
                        cell = Cell(self._win)
                        row.append(cell)
                  self._cells.append(row)
            for row in range(self._num_cols):
                  for cell in range(self._num_rows):
                        self._draw_cell(row, cell)
      
      def _draw_cell(self, i, j):
            if self._win is None:
                  return
            x1 = self._x1 + i * self._cell_size_x
            y1 = self._y1 + j * self._cell_size_y
            x2 = x1 + self._cell_size_x
            y2 = y1 + self._cell_size_y

            self._cells[i][j].draw(x1, y1, x2, y2)
            self._animate()
      
      def _animate(self):
            if self._win is None:
                  return
            self._win.redraw()
            time.sleep(0.05)
