from graphics import Line, Point

# know which walls it has
# where it exisits on the canvas
# hold access to the window for drawing 
class Cell:
      def __init__(self, win=None):
            self.has_left_wall = True
            self.has_right_wall = True
            self.has_top_wall = True
            self.has_bottom_wall = True
            self._x1 = None
            self._x2 = None
            self._y1 = None
            self._y2 = None
            self._win = win
            self.visited = False
      
      def draw(self, x1, y1, x2, y2):
            if self._win is None:
                  return
            self._x1 = x1
            self._x2 = x2
            self._y1 = y1
            self._y2 = y2

            if self.has_left_wall:
                  line = Line(Point(x1, y1), Point(x1, y2))
                  self._win.draw_line(line)
            else:
                  line = Line(Point(x1, y1), Point(x2, y2))
                  self._win.draw_line(line, "white")

            if self.has_right_wall:
                  line = Line(Point(x2, y1), Point(x2, y2))
                  self._win.draw_line(line)
            else:
                  line = Line(Point(x2, y1), Point(x2, y2))
                  self._win.draw_line(line, "white")

            if self.has_top_wall:
                  line = Line(Point(x1, y1), Point(x2, y1))
                  self._win.draw_line(line)
            else:
                  line = Line(Point(x1, y1), Point(x2, y1))
                  self._win.draw_line(line, "white")

            if self.has_bottom_wall:
                  line = Line(Point(x1, y2), Point(x2, y2))
                  self._win.draw_line(line)
            else:
                  line = Line(Point(x1, y2), Point(x2, y2))
                  self._win.draw_line(line, "white")
      
      def draw_move(self, to_cell, undo=False):
            # get the coordinates of center point 
            half_length = abs(self._x2 - self._x1) // 2
            x_center1 = self._x1 + half_length
            y_center1 = self._y1 + half_length

            half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
            x_center2 = to_cell._x1 + half_length2
            y_center2 = to_cell._y1 + half_length2

            # determine line color 
            fill_color = "red"
            if undo:
                  fill_color = "gray"
            
            line = Line(Point(x_center1, y_center1), Point(x_center2, y_center2))
            self._win.draw_line(line, fill_color)