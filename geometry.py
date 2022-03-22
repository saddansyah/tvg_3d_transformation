import numpy as np
from graphics import *
from transform import *
from abc import ABC, abstractmethod


class Geometry:
        
    def __init__(self, geometry: np.ndarray, screen_width, screen_height):
        self.__scaling = 100
        self.__geometry = geometry * self.__scaling

    def get_coord(self):
        return self.__geometry

    def geometry_translation(self, tx, ty, tz):
        translated_geometry = np.empty((0, 3))

        for point in self.__geometry:
            translated_geometry = np.append(translated_geometry, Transform.translation(
                point, tx, ty, tz).reshape((1, 3)), axis=0)

        self.__geometry = translated_geometry

    def geometry_shearing(self, shx, shy, shz, sh_type):
        sheared_geometry = np.empty((0,3))

        for point in self.__geometry:
            sheared_geometry = np.append(sheared_geometry, Transform.shear(point, (shx, shy, shz), sh_type).reshape((1,3)), axis=0)
        
        self.__geometry = sheared_geometry

    def geometry_scaling(self, sx, sy, sz):
        scaled_geometry = np.empty((0,3))

        for point in self.__geometry:
            scaled_geometry = np.append(scaled_geometry, Transform.scaling(point, sx, sy, sz).reshape((1,3)), axis=0)
        
        self.__geometry = scaled_geometry

    def geometry_rotation(self, rx, ry, rz, r_type, r_axisx, r_axisy, r_axisz):
        rotated_geometry = np.empty((0,3))

        for point in self.__geometry:
            rotated_geometry = np.append(rotated_geometry, Transform.rotation(point, (-rx, -ry, -rz), r_type, (r_axisx, r_axisy, r_axisz)).reshape((1,3)), axis=0)
        
        self.__geometry = rotated_geometry        

    # method to return 3d cube to 2d cube

    def projected_geometry(self):

        geometry = self.__geometry
        projected_geometry = []

        for point in geometry:
            projected_geometry.append(Transform.projection(point).tolist())

        print(projected_geometry)
        return projected_geometry

    @abstractmethod
    def draw_cartesian(self):
        pass
    
    @abstractmethod
    def draw_geometry(self):
        pass