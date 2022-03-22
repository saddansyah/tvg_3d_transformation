import numpy as np
import math

class Transform:
    def __init__(self):
        pass
    
    @staticmethod
    def translation(point: np.ndarray, tx, ty, tz):
        # ty dibuat minus karena pergerakannya pada sumbu kartesian berbalik arah
        # misal ty += 100, maka akan digeser kebawah 100 satuan tidak seperti kartesian yang digeser ke atas 100 satuan

        if(len(point) < 4):
            point = np.append(point, 1)
            
        translation_matrix = np.array([[1,0,0,tx],
                                    [0,1,0,ty],
                                    [0,0,1,tz],
                                    [0,0,0,1]])
        return (translation_matrix @ point)[:-1]

    @staticmethod
    def scaling(point: np.ndarray, sx, sy, sz):
        if(len(point) < 4):
            point = np.append(point, 1)

        scaling_matrix = np.array([[sx,0,0,0],
                                [0,sy,0,0],
                                [0,0,sz,0],
                                [0,0,0,1]])

        return (scaling_matrix @ point)[:-1] #slicing index terakhir biar hasilnya [x,y,z] instead of [x,y,z,1]

    @staticmethod
    def shearxy(point: np.ndarray, shx, shy):
        if(len(point) < 4):
            point = np.append(point, 1)

        shearxy_matrix = np.array([[1,0,shx,0],
                                [0,1,shy,0],
                                [0,0,1,0],
                                [0,0,0,1]])
        return (shearxy_matrix @ point)[:-1] #slicing index terakhir biar hasilnya [x,y,z] instead of [x,y,z,1]

    @staticmethod
    def shearyz(point: np.ndarray, shy, shz):
        if(len(point) < 4):
            point = np.append(point, 1)

        shearyz_matrix = np.array([[1,0,0,0],
                                [shy,1,0,0],
                                [shz,0,1,0],
                                [0,0,0,1]])
        return (shearyz_matrix @ point)[:-1] #slicing index terakhir biar hasilnya [x,y,z] instead of [x,y,z,1]

    @staticmethod
    def shearxz(point: np.ndarray, shx, shz):
        if(len(point) < 4):
            point = np.append(point, 1)

        shearxz_matrix = np.array([[1,shx,0,0],
                                [0,1,0,0],
                                [0,shz,1,0],
                                [0,0,0,1]])
        return (shearxz_matrix @ point)[:-1] #slicing index terakhir biar hasilnya [x,y,z] instead of [x,y,z,1]
        
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
