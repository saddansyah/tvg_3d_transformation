from graphics import *
import numpy as np

#TRANSLASI
def translasi(tx,ty,tz):
    global matrix
    trans = np.array([[1,0,0,tx],
                      [0,1,0,ty],
                      [0,0,1,tz],
                      [0,0,0,1]])
    return trans

#SCALE
def scale(sx,sy,sz):
    global matrix
    scale = np.array([[sx,0,0,0],
                      [0,sy,0,0],
                      [0,0,sz,0],
                      [0,0,0,1]])
    return scale

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
def shearxy(shx,shy):
    global matrix
    sxy = np.array([[1,0,shx,0],
                    [0,1,shy,0],
                    [0,0,1,0],
                    [0,0,0,1]])
    return sxy

#SHEAR YZ
def shearyz(shy,shz):
    global matrix
    syz = np.array([[1,0,0,0],
                    [0,shy,0,0],
                    [0,shz,1,0],
                    [0,0,0,1]])
    return syz

#SHEAR XZ
def shearxz(shx,shz):
    global matrix
    sxz = np.array([[shx,0,0,0],
                    [0,1,0,0],
                    [shz,0,1,0],
                    [0,0,0,1]])
    return sxz
