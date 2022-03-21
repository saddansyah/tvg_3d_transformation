import numpy as np
from graphics import *
import math
from transform import *


class Cube:
    def __init__(self):
        self.__scaling = 100
        self.__cube = np.array([[0, 0, 0],
                                [1, 0, 0],
                                [1, 0, 1],
                                [0, 0, 1],
                                [0, 1, 0],
                                [1, 1, 0],
                                [1, 1, 1],
                                [0, 1, 1]])*self.__scaling

    def get_coord(self):
        return self.__cube

    def cube_translation(self, tx, ty, tz):
        translated_cube = np.empty((0, 3))

        for point in self.__cube:
            translated_cube = np.append(translated_cube, Transform.translation(
                point, tx, ty, tz).reshape((1, 3)), axis=0)

        self.__cube = translated_cube

    def cube_scaling(self, sx, sy, sz):
        scaled_cube = np.empty((0, 3))

        for point in self.__cube:
            scaled_cube = np.append(scaled_cube, Transform.scaling(
                point, sx, sy, sz).reshape((1, 3)), axis=0)

        self.__cube = scaled_cube

    # method to project 3d point to 2d point
    # @staticmethod
    def projection(self, point3D):
        # if(len(point3D) < 4):
        #     point3D = np.append(point3D, 1)

        x = point3D[0]
        y = point3D[1]
        z = point3D[2]
        angle = math.pi/6

        projection_matrix = np.array([[1, 0, 0.5*math.cos(angle)],
                                      [0, 1, -0.5*math.sin(angle)],
                                      [0, 0, 0]])

        point2D = projection_matrix @ point3D

        return point2D

    # method to return 3d cube to 2d cube
    # @staticmethod
    def projected_cube(self):

        cube = self.__cube
        projected_cube = []

        for point in cube:
            projected_cube.append(self.projection(point).tolist())

        print(projected_cube)
        return projected_cube

    @staticmethod
    def draw_cube(point: list):
        width = 1200
        height = 720
        margin = 100
        point *= 100

        win = GraphWin("My Window", width, height)
        win.setBackground(color_rgb(218, 91, 91))

        back = Rectangle(Point(point[3][0] + margin, point[3][1] + margin),
                         Point(point[6][0] + margin, point[6][1] + margin))
        back.setOutline("white")
        back.setWidth(5)
        back.draw(win)

        front = Rectangle(Point(point[0][0] + margin, point[0][1] + margin),
                          Point(point[5][0] + margin, point[5][1] + margin))
        front.setOutline("grey")
        front.setWidth(5)
        front.draw(win)

        ln1 = Line(Point(point[4][0] + margin, point[4][1] + margin),
                   Point(point[7][0] + margin, point[7][1] + margin))
        ln1.setOutline("blue")
        ln1.setWidth(5)
        ln1.draw(win)

        ln2 = Line(Point(point[5][0] + margin, point[5][1] + margin),
                   Point(point[6][0] + margin, point[6][1] + margin))
        ln2.setOutline("yellow")
        ln2.setWidth(5)
        ln2.draw(win)

        ln3 = Line(Point(point[1][0] + margin, point[1][1] + margin),
                   Point(point[2][0] + margin, point[2][1] + margin))
        ln3.setOutline("green")
        ln3.setWidth(5)
        ln3.draw(win)

        ln4 = Line(Point(point[0][0] + margin, point[0][1] + margin),
                   Point(point[3][0] + margin, point[3][1] + margin))
        ln4.setOutline("red")
        ln4.setWidth(5)
        ln4.draw(win)

        win.getMouse()
        win.close()


# pemanggilan class
cube1 = Cube()

# transformasi
# translasi kubus 35 satuan/pixel ke arah x+, 25 satuan/pixel ke arah y+, dan 25 ke arah z+
cube1.cube_translation(35, -25, 25)
cube1.cube_scaling(4, 4, 4)  # perbesaran kubus dengan faktor perbesaran = 4

# display cube
print(cube1.get_coord())
projected_cube1 = cube1.projected_cube()
cube1.draw_cube(projected_cube1)
