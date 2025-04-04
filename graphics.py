from tkinter import BOTH, Canvas, Tk

class Window:
      def __init__(self, width, height):
            self.__root = Tk()
            self.__root.title("Graphical Maze Solver")
            self.__root.protocol("WM_DELETE_WINDOW", self.close)
            self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
            self.__canvas.pack(fill=BOTH, expand=1)
            self.__is_running = False
      
      def redraw(self):
            self.__root.update_idletasks()
            self.__root.update()
      
      def wait_for_close(self):
            self.__is_running = True
            while self.__is_running:
                  self.redraw()
            print("window closed...")
      
      def close(self):
            self.__is_running = False
      
      def draw_line(self, line, fill_color="black"):
            line.draw(self.__canvas, fill_color)

class Point:
      def __init__(self, x, y):
            self.x = x
            self.y = y

class Line:
      def __init__(self, point1, point2):
            self.point_1 = point1
            self.point_2 = point2
      
      def draw(self, canvas, fill_color="black"):
            canvas.create_line(
                  self.point_1.x, 
                  self.point_1.y, 
                  self.point_2.x, 
                  self.point_2.y, 
                  fill=fill_color, 
                  width=2
            )
            
      

