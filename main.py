import numpy as np
from graphics import *
import math

class Cube:
    def __init__(self):
        scaling = 100
        self.__cube = np.array([[0,0,0],
                                [1,0,0],
                                [1,0,1],
                                [0,0,1],
                                [0,1,0],
                                [1,1,0],
                                [1,1,1],
                                [0,1,1]])*scaling
    
    def get_coord(self):
        return self.__cube
    
    def translation(self, point, tx, ty, tz) -> np.ndarray:
        if(len(point) < 4):
            point = np.append(point, 1)
            
        translation_matrix = np.array([[1,0,0,tx],
                                    [0,1,0,ty],
                                    [0,0,1,tz],
                                    [0,0,0,1]])
        return (translation_matrix @ point)[:-1]

    def cube_translation(self):
        translated_cube = np.empty((0,3))

        for point in self.__cube:
            translated_cube = np.append(translated_cube, self.translation(point, 22, 22, 22).reshape((1,3)), axis=0)
        
        self.__cube = translated_cube

    # method to project 3d point to 2d point
    # @staticmethod
    def projection(self, point3D):
        # if(len(point3D) < 4):
        #     point3D = np.append(point3D, 1)
        
        x = point3D[0]
        y = point3D[1]
        z = point3D[2]
        angle = math.pi/6

        projection_matrix = np.array([[1,0,0.5*math.cos(angle)],
                                    [0,1,-0.5*math.sin(angle)],
                                    [0,0,0]])

        point2D = projection_matrix @ point3D

        return point2D

    # method to return 3d cube to 2d cube
    #@staticmethod
    def projected_cube(self):

        cube = self.__cube
        projected_cube = []

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

class Transform:
    def __init__(self):
        pass


# pemanaggilan class
cube1 = Cube()
# print(cube1.get_coord())
cube1.cube_translation()
# print(cube1.get_coord())
projected_cube1 = cube1.projected_cube()
# print(cube1.get_coord())
# print(projected_cube1)
cube1.draw_cube(projected_cube1)

