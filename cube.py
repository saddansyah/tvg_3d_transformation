import numpy as np
from graphics import *
from geometry import *

class Cube(Geometry):
    def __init__(self):
        self.__scaling = 100
        cube = np.array([[0,0,0],
                         [1,0,0],
                         [1,0,1],
                         [0,0,1],
                         [0,1,0],
                         [1,1,0],
                         [1,1,1],
                         [0,1,1]])
                         
        super().__init__(cube, 1280, 720)

        self.__width = 1280
        self.__height = 720
        self.init_screen()

    def init_screen(self):
        self.win = GraphWin("My Window", self.__width, self.__height)
        self.win.setBackground(color_rgb(218, 91, 91))
        self.__origin = np.zeros(3)
    
    def draw_cartesian(self, marginx, marginy):
        x = Line(Point(self.__origin[0] + marginx, self.__origin[1] + marginy), 
                 Point(self.__origin[0] + marginx + self.__width, self.__origin[1] + marginy))
        
        x.setOutline("black")
        x.setWidth(2)
        x.draw(self.win)   

        y = Line(Point(self.__origin[0] + marginx, self.__origin[1] + marginy), 
                 Point(self.__origin[0] + marginx, self.__origin[1] + marginy - self.__height))
        
        y.setOutline("black")
        y.setWidth(2)
        y.draw(self.win) 

        z = Line(Point(self.__origin[0] + marginx, self.__origin[1] + marginy), 
                 Point(self.__origin[0] + marginx - self.__width, self.__origin[1] + marginy + self.__height))
        
        z.setOutline("black")
        z.setWidth(2)
        z.draw(self.win) 

    def get_coord(self):
        return super().get_coord()

    def cube_translation(self, tx, ty, tz):
        return super().geometry_translation(tx, ty, tz)

    def cube_scaling(self, sx, sy, sz):
        return super().geometry_scaling(sx, sy, sz)

    def cube_shearing(self, shx, shy, shz, sh_type):
        return super().geometry_shearing(shx, shy, shz, sh_type)

    def projected_cube(self):
        return super().projected_geometry()

    def draw_geometry(self, point: list):
        marginx = 350
        marginy = 500
        # point *= 100

        self.draw_cartesian(marginx, marginy)

        lines = [
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
        
        for line in lines:
            line.setOutline("white")
            line.setWidth(3)
            line.draw(self.win)

        self.win.getMouse()
        self.win.close()
    

