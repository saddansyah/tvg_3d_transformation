import numpy as np
import math

# #NILAI MATRIX
# def koordinatmatrix():
#     baris = int(input("baris: "))
#     kolum = int(input("kolom: "))
#     Matrix = []
#     print("Entries row-wise: ")

#     for i in range(baris):
#         a = []
#         for j in range(kolum):
#             a.append(int(input()))
#         Matrix.append(a)
#     Matrix = np.array(Matrix)
#     return Matrix

# #TRANSLASI
# def translasi():
#     tx = int(input("tx: "))
#     ty = int(input("ty: "))
#     tz = int(input("tz: "))
#     trans = np.array([[1,0,0,tx],
#                       [0,1,0,ty],
#                       [0,0,1,tz],
#                       [0,0,0,1]])
#     return trans
# def translasim(matrix,self):
#     translasimtrx = print("Koordinat Translasi: \n", np.dot(matrix,self))
#     return translasimtrx
# translasimat = translasi()
# mekoordinatmatrix = koordinatmatrix()
# metranslasi = translasim(translasimat,mekoordinatmatrix)

# #SCALE
# def scale():
#     sx = int(input("sx: "))
#     sy = int(input("sy: "))
#     sz = int(input("sz: "))
#     scale = np.array([[sx,0,0,0],
#                       [0,sy,0,0],
#                       [0,0,sz,0],
#                       [0,0,0,1]])
#     return scale
# def scalexyz(matrix,self):
#     scalemtrx = print("Koordinat Scale: \n", np.dot(matrix,self))
#     return scalemtrx
# scalematrix = scale()
# mekoordinatmatrix = koordinatmatrix()
# mescale = scalexyz(scalematrix,mekoordinatmatrix)

# #ROTASI X
# def rx(degree):
#     global matrix
#     rx = np.array([[1,0,0,0],
#                    [0,np.cos(degree),-np.sin(degree),0],
#                    [0,np.sin(degree),np.cos(degree),0],
#                    [0,0,0,1]])
#     return rx

# #ROTASI Y
# def ry(degree):
#     global matrix
#     ry = np.array([[np.cos(degree),0,np.sin(degree),0],
#                    [0,1,0,0],
#                    [-np.sin(degree),0,np.cos(degree),0],
#                    [0,0,0,1]])
#     return ry

# #ROTASI Z
# def rz(degree):
#     global matrix
#     rz = np.array([[np.cos(degree),-np.sin(degree),0,0],
#                    [np.sin(degree),np.cos(degree),0,0],
#                    [0,0,1,0],
#                    [0,0,0,1]])
#     return rz

# #SHEAR XY
# def shearxy():
#     global matrix
#     sxy = np.array([[1,0,shx,0],
#                     [0,1,shy,0],
#                     [0,0,1,0],
#                     [0,0,0,1]])
#     return sxy

# #SHEAR YZ
# def shearyz():
#     global matrix
#     syz = np.array([[1,0,0,0],
#                     [0,shy,0,0],
#                     [0,shz,1,0],
#                     [0,0,0,1]])
#     return syz

# #SHEAR XZ
# def shearxz():
#     global matrix
#     sxz = np.array([[shx,0,0,0],
#                     [0,1,0,0],
#                     [shz,0,1,0],
#                     [0,0,0,1]])
#     return sxz

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
                                    [0,1,0,-ty],
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
                                [0,shy,0,0],
                                [0,shz,1,0],
                                [0,0,0,1]])
        return (shearyz_matrix @ point)[:-1] #slicing index terakhir biar hasilnya [x,y,z] instead of [x,y,z,1]

    @staticmethod
    def shearxz(point: np.ndarray, shx, shz):
        if(len(point) < 4):
            point = np.append(point, 1)

        shearxz_matrix = np.array([[shx,0,0,0],
                                [0,1,0,0],
                                [shz,0,1,0],
                                [0,0,0,1]])
        return (shearxz_matrix @ point)[:-1] #slicing index terakhir biar hasilnya [x,y,z] instead of [x,y,z,1]
        
    @classmethod
    def shear(cls, point: np.ndarray, sh_factor: tuple, sh_type):
        if(len(point) < 4):
            point = np.append(point, 1)

        if sh_type == "xy":
            return cls.shearxy(point, sh_factor[0], sh_factor[1])
        elif sh_type == "yz":
            return cls.shearyz(point, sh_factor[1], sh_factor[2])
        elif sh_type == "xz":
            return cls.shearxz(point, sh_factor[0], sh_factor[2])
