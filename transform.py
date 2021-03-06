import numpy as np
import math


class Transform:

    __scaling = 0

    def __init__(self):
        pass

    @staticmethod
    def projection(point3D):
        angle = math.pi/4

        projection_matrix = np.array([[1, 0, 0.5*math.cos(angle)],
                                      [0, 1, -0.5*math.sin(angle)],
                                      [0, 0, 0]])

        reflection_matrix = np.array([[1, 0, 0],
                                      [0, -1, 0],
                                      [0, 0, 1]])

        return projection_matrix @ reflection_matrix @ point3D

    @staticmethod
    def translation(point: np.ndarray, tx, ty, tz, scaling):
        __scaling = scaling

        if(len(point) < 4):
            point = np.append(point, 1)

        translation_matrix = np.array([[1, 0, 0, tx*__scaling],
                                       [0, 1, 0, ty*__scaling],
                                       [0, 0, 1, tz*__scaling],
                                       [0, 0, 0, 1]])
        return (translation_matrix @ point)[:-1]

    @staticmethod
    def scaling(point: np.ndarray, sx, sy, sz):
        if(len(point) < 4):
            point = np.append(point, 1)

        scaling_matrix = np.array([[sx, 0, 0, 0],
                                   [0, sy, 0, 0],
                                   [0, 0, sz, 0],
                                   [0, 0, 0, 1]])

        # slicing index terakhir biar hasilnya [x,y,z] instead of [x,y,z,1]
        return (scaling_matrix @ point)[:-1]

    @staticmethod
    def shearxy(point: np.ndarray, shx, shy):
        if(len(point) < 4):
            point = np.append(point, 1)

        shearxy_matrix = np.array([[1, 0, shx, 0],
                                   [0, 1, shy, 0],
                                   [0, 0, 1, 0],
                                   [0, 0, 0, 1]])
        # slicing index terakhir biar hasilnya [x,y,z] instead of [x,y,z,1]
        return (shearxy_matrix @ point)[:-1]

    @staticmethod
    def shearyz(point: np.ndarray, shy, shz):
        if(len(point) < 4):
            point = np.append(point, 1)

        shearyz_matrix = np.array([[1, 0, 0, 0],
                                   [shy, 1, 0, 0],
                                   [shz, 0, 1, 0],
                                   [0, 0, 0, 1]])
        # slicing index terakhir biar hasilnya [x,y,z] instead of [x,y,z,1]
        return (shearyz_matrix @ point)[:-1]

    @staticmethod
    def shearxz(point: np.ndarray, shx, shz):
        if(len(point) < 4):
            point = np.append(point, 1)

        shearxz_matrix = np.array([[1, shx, 0, 0],
                                   [0, 1, 0, 0],
                                   [0, shz, 1, 0],
                                   [0, 0, 0, 1]])
        # slicing index terakhir biar hasilnya [x,y,z] instead of [x,y,z,1]
        return (shearxz_matrix @ point)[:-1]

    @classmethod
    def shear(cls, point: np.ndarray, sh_factor: tuple, sh_type: str):
        if(len(point) < 4):
            point = np.append(point, 1)

        if sh_type == "xy":
            return cls.shearxy(point, sh_factor[0], sh_factor[1])
        elif sh_type == "yz":
            return cls.shearyz(point, sh_factor[1], sh_factor[2])
        elif sh_type == "xz":
            return cls.shearxz(point, sh_factor[0], sh_factor[2])

    @staticmethod
    def rotationx(point: np.ndarray, rotax):
        if(len(point) < 4):
            point = np.append(point, 1)

        rotatex_matrix = np.array([[1, 0, 0, 0],
                                   [0, np.cos(np.radians(rotax)), -
                                    np.sin(np.radians(rotax)), 0],
                                   [0, np.sin(np.radians(rotax)),
                                    np.cos(np.radians(rotax)), 0],
                                   [0, 0, 0, 1]])
        return (rotatex_matrix @ point)[:-1]

    @staticmethod
    def rotationy(point: np.ndarray, rotay):
        if(len(point) < 4):
            point = np.append(point, 1)

        rotatey_matrix = np.array([[np.cos(np.radians(rotay)), 0, np.sin(np.radians(rotay)), 0],
                                   [0, 1, 0, 0],
                                   [-np.sin(np.radians(rotay)), 0,
                                    np.cos(np.radians(rotay)), 0],
                                   [0, 0, 0, 1]])
        return (rotatey_matrix @ point)[:-1]

    @staticmethod
    def rotationz(point: np.ndarray, rotaz):
        if(len(point) < 4):
            point = np.append(point, 1)

        rotatez_matrix = np.array([[np.cos(np.radians(rotaz)), -np.sin(np.radians(rotaz)), 0, 0],
                                   [np.sin(np.radians(rotaz)), np.cos(
                                       np.radians(rotaz)), 0, 0],
                                   [0, 0, 1, 0],
                                   [0, 0, 0, 1]])
        return (rotatez_matrix @ point)[:-1]

    @classmethod
    def rotation(cls, point: np.ndarray, r_factor: tuple, r_type: str, r_axis:tuple):
        if(len(point) < 4):
            point = np.append(point, 1)

        point = cls.translation(point, -r_axis[0], -r_axis[1], -r_axis[2], cls.__scaling)

        if r_type == "x":
            point = cls.rotationx(point, r_factor[0])
        elif r_type == "y":
            point = cls.rotationy(point, r_factor[1])
        elif r_type == "z":
            point =  cls.rotationz(point, r_factor[2])

        return cls.translation(point, r_axis[0], r_axis[1], r_axis[2], cls.__scaling)
