from graphics import *
import numpy as np

#NILAI MATRIX
def koordinatmatrix():
    baris = int(input("baris: "))
    kolum = int(input("kolom: "))
    Matrix = []
    print("Entries row-wise: ")

    for i in range(baris):
        a = []
        for j in range(kolum):
            a.append(int(input()))
        Matrix.append(a)
    Matrix = np.array(Matrix)
    return Matrix

#TRANSLASI
def translasi():
    tx = int(input("tx: "))
    ty = int(input("ty: "))
    tz = int(input("tz: "))
    trans = np.array([[1,0,0,tx],
                      [0,1,0,ty],
                      [0,0,1,tz],
                      [0,0,0,1]])
    return trans
def translasim(matrix,self):
    translasimtrx = print("Koordinat Translasi: \n", np.dot(matrix,self))
    return translasimtrx
translasimat = translasi()
mekoordinatmatrix = koordinatmatrix()
metranslasi = translasim(translasimat,mekoordinatmatrix)

#SCALE
def scale():
    sx = int(input("sx: "))
    sy = int(input("sy: "))
    sz = int(input("sz: "))
    scale = np.array([[sx,0,0,0],
                      [0,sy,0,0],
                      [0,0,sz,0],
                      [0,0,0,1]])
    return scale
def scalexyz(matrix,self):
    scalemtrx = print("Koordinat Scale: \n", np.dot(matrix,self))
    return scalemtrx
scalematrix = scale()
mekoordinatmatrix = koordinatmatrix()
mescale = scalexyz(scalematrix,mekoordinatmatrix)

#ROTASI X
def rx(degree):
    global matrix
    rx = np.array([[1,0,0,0],
                   [0,np.cos(degree),-np.sin(degree),0],
                   [0,np.sin(degree),np.cos(degree),0],
                   [0,0,0,1]])
    return rx

#ROTASI Y
def ry(degree):
    global matrix
    ry = np.array([[np.cos(degree),0,np.sin(degree),0],
                   [0,1,0,0],
                   [-np.sin(degree),0,np.cos(degree),0],
                   [0,0,0,1]])
    return ry

#ROTASI Z
def rz(degree):
    global matrix
    rz = np.array([[np.cos(degree),-np.sin(degree),0,0],
                   [np.sin(degree),np.cos(degree),0,0],
                   [0,0,1,0],
                   [0,0,0,1]])
    return rz

#SHEAR XY
def shearxy():
    global matrix
    sxy = np.array([[1,0,shx,0],
                    [0,1,shy,0],
                    [0,0,1,0],
                    [0,0,0,1]])
    return sxy

#SHEAR YZ
def shearyz():
    global matrix
    syz = np.array([[1,0,0,0],
                    [0,shy,0,0],
                    [0,shz,1,0],
                    [0,0,0,1]])
    return syz

#SHEAR XZ
def shearxz():
    global matrix
    sxz = np.array([[shx,0,0,0],
                    [0,1,0,0],
                    [shz,0,1,0],
                    [0,0,0,1]])
    return sxz
