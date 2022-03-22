import numpy as np
from graphics import *
import math
from transform import *


class Cube:
    def __init__(self, screen_width, screen_height):
        self.__scaling = 100
        self.__cube = np.array([[0,0,0],
                                [1,0,0],
                                [1,0,1],
                                [0,0,1],
                                [0,1,0],
                                [1,1,0],
                                [1,1,1],
                                [0,1,1]])*self.__scaling
        
        self.__origin = np.zeros(3)
        self.__width = screen_width
        self.__height = screen_height
        self.__win = GraphWin("My Window", self.__width, self.__height)
        self.__win.setBackground(color_rgb(218, 91, 91))

    def __draw_cartesian(self, marginx, marginy):
        x = Line(Point(self.__origin[0] + marginx, self.__origin[1] + marginy), 
                 Point(self.__origin[0] + marginx + self.__width, self.__origin[1] + marginy))
        x.setOutline("black")
        x.setWidth(2)
        x.draw(self.__win)   

        y = Line(Point(self.__origin[0] + marginx, self.__origin[1] + marginy), 
                 Point(self.__origin[0] + marginx, self.__origin[1] + marginy - self.__height))
        y.setOutline("black")
        y.setWidth(2)
        y.draw(self.__win) 

        z = Line(Point(self.__origin[0] + marginx, self.__origin[1] + marginy), 
                 Point(self.__origin[0] + marginx - self.__width, self.__origin[1] + marginy + self.__height))
        z.setOutline("black")
        z.setWidth(2)
        z.draw(self.__win) 

    def get_coord(self):
        return self.__cube

    def cube_translation(self, tx, ty, tz):
        translated_cube = np.empty((0, 3))

        for point in self.__cube:
            translated_cube = np.append(translated_cube, Transform.translation(
                point, tx, ty, tz).reshape((1, 3)), axis=0)

        self.__cube = translated_cube

    def cube_scaling(self, sx, sy, sz):
        scaled_cube = np.empty((0,3))

        for point in self.__cube:
            scaled_cube = np.append(scaled_cube, Transform.scaling(point, sx, sy, sz).reshape((1,3)), axis=0)
        
        self.__cube = scaled_cube

    def cube_shearing(self, shx, shy, shz, sh_type):
        sheared_cube = np.empty((0,3))

        for point in self.__cube:
            sheared_cube = np.append(sheared_cube, Transform.shear(point, (shx, shy, shz), sh_type).reshape((1,3)), axis=0)
        
        self.__cube = sheared_cube

    # method to return 3d cube to 2d cube
    # @staticmethod
    def projected_cube(self):

        cube = self.__cube
        projected_cube = []

        for point in cube:
            projected_cube.append(Transform.projection(point).tolist())

        print(projected_cube)
        return projected_cube
    
    def draw_cube(self, point: list):
        marginx = 350
        marginy = 500
        # point *= 100

        self.__draw_cartesian(marginx, marginy)

        # back side

        back_ln1 = Line(Point(point[7][0] + marginx, point[7][1] + marginy), Point(point[6][0] + marginx, point[6][1] + marginy))
        back_ln1.setOutline("grey")
        back_ln1.setWidth(5)
        back_ln1.draw(self.__win)  

        back_ln2 = Line(Point(point[6][0] + marginx, point[6][1] + marginy), Point(point[2][0] + marginx, point[2][1] + marginy))
        back_ln2.setOutline("grey")
        back_ln2.setWidth(5)
        back_ln2.draw(self.__win)

        back_ln3 = Line(Point(point[2][0] + marginx, point[2][1] + marginy), Point(point[3][0] + marginx, point[3][1] + marginy))
        back_ln3.setOutline("grey")
        back_ln3.setWidth(5)
        back_ln3.draw(self.__win)

        back_ln4 = Line(Point(point[3][0] + marginx, point[3][1] + marginy), Point(point[7][0] + marginx, point[7][1] + marginy))
        back_ln4.setOutline("grey")
        back_ln4.setWidth(5)
        back_ln4.draw(self.__win)

        # side      

        ln1 = Line(Point(point[4][0] + marginx, point[4][1] + marginy), Point(point[7][0] + marginx, point[7][1] + marginy))
        ln1.setOutline("blue")
        ln1.setWidth(5)
        ln1.draw(self.__win)

        ln2 = Line(Point(point[5][0] + marginx, point[5][1] + marginy), Point(point[6][0] + marginx, point[6][1] + marginy))
        ln2.setOutline("yellow")
        ln2.setWidth(5)
        ln2.draw(self.__win)

        ln3 = Line(Point(point[1][0] + marginx, point[1][1] + marginy), Point(point[2][0] + marginx, point[2][1] + marginy))
        ln3.setOutline("green")
        ln3.setWidth(5)
        ln3.draw(self.__win)

        ln4 = Line(Point(point[0][0] + marginx, point[0][1] + marginy), Point(point[3][0] + marginx, point[3][1] + marginy))
        ln4.setOutline("red")
        ln4.setWidth(5)
        ln4.draw(self.__win)

        # front side side

        front_ln1 = Line(Point(point[4][0] + marginx, point[4][1] + marginy), Point(point[5][0] + marginx, point[5][1] + marginy))
        front_ln1.setOutline("white")
        front_ln1.setWidth(5)
        front_ln1.draw(self.__win)

        front_ln2 = Line(Point(point[5][0] + marginx, point[5][1] + marginy), Point(point[1][0] + marginx, point[1][1] + marginy))
        front_ln2.setOutline("white")
        front_ln2.setWidth(5)
        front_ln2.draw(self.__win)

        front_ln3 = Line(Point(point[1][0] + marginx, point[1][1] + marginy), Point(point[0][0] + marginx, point[0][1] + marginy))
        front_ln3.setOutline("white")
        front_ln3.setWidth(5)
        front_ln3.draw(self.__win)

        front_ln4 = Line(Point(point[0][0] + marginx, point[0][1] + marginy), Point(point[4][0] + marginx, point[4][1] + marginy))
        front_ln4.setOutline("white")
        front_ln4.setWidth(5)
        front_ln4.draw(self.__win)        

        self.__win.getMouse()
        self.__win.close()  

# instance objek cube1 
cube1 = Cube(1280, 720)

# obj cube1 dikenai transformasi seperti di bawah
cube1.cube_translation(0, 0, 0)
# cube1.cube_scaling(3,3,3)
cube1.cube_shearing(0.5,0.5,0.5,'xz')

# koordinat 3d cube1 diprojeksikan menggunakan cabinet projection method biar bisa ditampilin di 2d (di layar)
cube1.draw_cube(cube1.projected_cube())

