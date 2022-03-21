import numpy as np
from graphics import *
import math

class Cube:
    def __init__(self):
        self.__cube = np.array([[0,0,0],
                                [1,0,0],
                                [1,0,1],
                                [0,0,1],
                                [0,1,0],
                                [1,1,0],
                                [1,1,1],
                                [0,1,1]])
    

    # method to project 3d point to 2d point
    #@staticmethod
    def projection(self, point3D):
        # if(len(point3D) < 4):
        #     point3D = np.append(point3D, 1)
        
        x = point3D[0]
        y = point3D[1]
        z = point3D[2]
        angle = math.pi/6

        projection_matrix = np.array([[1,0,0.5*math.cos(angle)],
                                    [0,1,0.5*math.sin(angle)],
                                    [0,0,0]])

        point2D = projection_matrix @ point3D

        return point2D

    #@staticmethod
    def projected_cube(self):
        scaling = 200
        tolerance = scaling/2
        cube = self.__cube
        cube *= scaling

        projected_cube = []
        projected_cube

        for point in cube:
            projected_cube.append(self.projection(point).tolist())

        print(projected_cube)
        return projected_cube

    @staticmethod
    def draw_cube(point: list):
        width = 800
        height = 800
        margin = 100
        point *= 100
        
        win = GraphWin("My Window", width, height)
        win.setBackground(color_rgb(218, 91, 91))

        back = Rectangle(Point(point[3][0] + margin, point[3][1] + margin), Point(point[6][0] + margin, point[6][1] + margin))
        back.setOutline("white")
        back.setWidth(5)
        back.draw(win)

        front = Rectangle(Point(point[0][0] + margin, point[0][1] + margin), Point(point[5][0] + margin, point[5][1] + margin))
        front.setOutline("grey")
        front.setWidth(5)
        front.draw(win)

        ln1 = Line(Point(point[4][0] + margin, point[4][1] + margin), Point(point[7][0] + margin, point[7][1] + margin))
        ln1.setOutline("blue")
        ln1.setWidth(5)
        ln1.draw(win)

        ln2 = Line(Point(point[5][0] + margin, point[5][1] + margin), Point(point[6][0] + margin, point[6][1] + margin))
        ln2.setOutline("yellow")
        ln2.setWidth(5)
        ln2.draw(win)

        ln3 = Line(Point(point[1][0] + margin, point[1][1] + margin), Point(point[2][0] + margin, point[2][1] + margin))
        ln3.setOutline("green")
        ln3.setWidth(5)
        ln3.draw(win)

        ln4 = Line(Point(point[0][0] + margin, point[0][1] + margin), Point(point[3][0] + margin, point[3][1] + margin))
        ln4.setOutline("red")
        ln4.setWidth(5)
        ln4.draw(win)

        win.getMouse()
        win.close()  


# pemanaggilan class
cube1 = Cube()
projected_cube1 = cube1.projected_cube()
cube1.draw_cube(projected_cube1)

