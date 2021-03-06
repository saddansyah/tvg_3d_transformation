import numpy as np
from geometry import *

class Cube(Geometry):
    def __init__(self, cube):
                         
        super().__init__(cube, 1280, 720)

        self.__width = 1280
        self.__height = 720
        self.init_screen()

    def init_screen(self):
        self.win = GraphWin("My Window", self.__width, self.__height)
        self.win.setBackground(color_rgb(218, 91, 91))
        self.__origin = np.zeros(3)
        self.draw_geometry(self.projected_cube())
    
    def draw_cartesian(self, marginx, marginy):

        self.__cartesian_line = [
            Line(Point(self.__origin[0] + marginx, self.__origin[1] + marginy), 
                 Point(self.__origin[0] + marginx + self.__width, self.__origin[1] + marginy)),
            Line(Point(self.__origin[0] + marginx, self.__origin[1] + marginy), 
                 Point(self.__origin[0] + marginx, self.__origin[1] + marginy - self.__height)),
            Line(Point(self.__origin[0] + marginx, self.__origin[1] + marginy), 
                 Point(self.__origin[0] + marginx - self.__width, self.__origin[1] + marginy + self.__width)),
            Line(Point(self.__origin[0] + marginx, self.__origin[1] + marginy), 
                 Point(self.__origin[0] + marginx - self.__width, self.__origin[1] + marginy)),
            Line(Point(self.__origin[0] + marginx, self.__origin[1] + marginy), 
                 Point(self.__origin[0] + marginx, self.__origin[1] + marginy + self.__height)),
            Line(Point(self.__origin[0] + marginx, self.__origin[1] + marginy), 
                 Point(self.__origin[0] + marginx + self.__width, self.__origin[1] + marginy - self.__width)),
        ]

        for line in  self.__cartesian_line:
            line.setOutline("black")
            line.setWidth(2)
            line.draw(self.win)

        for i in range(-9, 9):
            text = Text(Point(self.__origin[0] + marginx + 80*i, self.__origin[1] + marginy + 10), str(i))
            text.draw(self.win)

        for i in range(-5, 0):
            text = Text(Point(self.__origin[0] + marginx - 10, self.__origin[1] + marginy - 80*i), str(i))
            text.draw(self.win)

        for i in range(1, 5):
            text = Text(Point(self.__origin[0] + marginx - 10, self.__origin[1] + marginy - 80*i), str(i))
            text.draw(self.win)

        for i in range(1, 13):
            text = Text(Point(self.__origin[0] + marginx + 28.5*i, self.__origin[1] + marginy - 18 - 28.5*i), str(i*-1))
            text.draw(self.win)

        for i in range(-14, 0):
            text = Text(Point(self.__origin[0] + marginx + 28.5*i, self.__origin[1] + marginy - 18 - 28.5*i), str(i*-1))
            text.draw(self.win)

    def get_coord(self):
        return super().get_coord()

    def cube_translation(self, tx, ty, tz):
        return super().geometry_translation(tx, ty, tz)

    def cube_scaling(self, sx, sy, sz):
        return super().geometry_scaling(sx, sy, sz)

    def cube_shearing(self, shx, shy, shz, sh_type):
        return super().geometry_shearing(shx, shy, shz, sh_type)

    def cube_rotating(self, rx, ry, rz, r_type, r_axisx, r_axisy, r_axisz):
        return super().geometry_rotation(rx, ry, rz, r_type, r_axisx, r_axisy, r_axisz)

    def projected_cube(self):
        return super().projected_geometry()

    def draw_geometry(self, point: list):
        marginx = self.__width/2
        marginy = self.__height/2

        self.draw_cartesian(marginx, marginy)

        self.__lines = [
            Line(Point(point[0][0] + marginx, point[0][1] + marginy), Point(point[1][0] + marginx, point[1][1] + marginy)),
            Line(Point(point[1][0] + marginx, point[1][1] + marginy), Point(point[2][0] + marginx, point[2][1] + marginy)),
            Line(Point(point[2][0] + marginx, point[2][1] + marginy), Point(point[3][0] + marginx, point[3][1] + marginy)),
            Line(Point(point[3][0] + marginx, point[3][1] + marginy), Point(point[0][0] + marginx, point[0][1] + marginy)),

            Line(Point(point[4][0] + marginx, point[4][1] + marginy), Point(point[5][0] + marginx, point[5][1] + marginy)),
            Line(Point(point[5][0] + marginx, point[5][1] + marginy), Point(point[6][0] + marginx, point[6][1] + marginy)),
            Line(Point(point[6][0] + marginx, point[6][1] + marginy), Point(point[7][0] + marginx, point[7][1] + marginy)),
            Line(Point(point[7][0] + marginx, point[7][1] + marginy), Point(point[4][0] + marginx, point[4][1] + marginy)),

            Line(Point(point[0][0] + marginx, point[0][1] + marginy), Point(point[4][0] + marginx, point[4][1] + marginy)),
            Line(Point(point[1][0] + marginx, point[1][1] + marginy), Point(point[5][0] + marginx, point[5][1] + marginy)),
            Line(Point(point[2][0] + marginx, point[2][1] + marginy), Point(point[6][0] + marginx, point[6][1] + marginy)),
            Line(Point(point[3][0] + marginx, point[3][1] + marginy), Point(point[7][0] + marginx, point[7][1] + marginy))
        ]
        
        for line in self.__lines:
            line.setOutline("white")
            line.setWidth(3)
            line.draw(self.win)

    def undraw_geometry(self):
        for line in self.__lines:
            line.undraw()

    

