# Kelompok 10 :
# 1. Christina Angraeni Panellah    - 456840
# 2. Faizah Bestiyana Darmawati     - 456364
# 3. Imam Arif Hadi Pramono         - 460546
# 4. Luthfi Izzuddin Hanif          - 463605
# 5. Saddan Syah Akbar              - 460566

from cube import *
import os

# interface
def interface(geometry):
    while True:
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        print("-----------------------------------------------------")
        transform = (input(
            """What kind of transformation would you like to do? 
            1. translation
            2. scale
            3. shear
            4. rotation
            \ntype the number of transformation you want to choose, \ntype 'stop or STOP' to stop\nyour choice : """))

        if transform.lower() == 'stop':
            break

        x = float(input('x: '))
        y = float(input('y: '))
        z = float(input('z: '))

        if (transform == '4'):
            print("x = y = z = 0 if translate from origin point (0,0,0)")
            r_axisx = float(input('rotate from x: '))
            r_axisy = float(input('rotate from y: '))
            r_axisz = float(input('rotate from z: '))
            print(f"rotate from point = ({round(r_axisx, 2)}, {round(r_axisy, 2)}, {round(r_axisz, 2)})")
            type = input('choose: x / y / z ? ')
            geometry.cube_rotating(x,y,z,type,r_axisx,r_axisy,r_axisz)
            geometry.undraw_geometry()
            geometry.draw_geometry(geometry.projected_cube())
        elif (transform == '3'):
            type = input('choose: xy / yz / xz ? ')
            geometry.cube_shearing(x,y,z, type)
            geometry.undraw_geometry()
            geometry.draw_geometry(geometry.projected_cube())
        elif (transform == '1'):
            geometry.cube_translation(x,y,z)
            geometry.undraw_geometry()
            geometry.draw_geometry(geometry.projected_cube())
        elif (transform == '2'):
            geometry.cube_scaling(x,y,z)
            geometry.undraw_geometry()
            geometry.draw_geometry(geometry.projected_cube())
        else:
            print("error on input, please try again")

# kubus
def cube():
    cube_points = np.array([[0,0,0],
                    [1,0,0],
                    [1,0,1],
                    [0,0,1],
                    [0,1,0],
                    [1,1,0],
                    [1,1,1],
                    [0,1,1]])

    cuboid_points = np.array([[0,0,0],
                         [1.5,0,0],
                         [1.5,0,1.5],
                         [0,0,1.5],
                         [0,1,0],
                         [1.5,1,0],
                         [1.5,1,1.5],
                         [0,1,1.5]])
    
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    what_cube = input('''What cube?
                     1. Predefined cube (1x1x1 cube)
                     2. Predefined cuboid
                     3. Userdefined cube (input your own cube)
                ''')

    if(what_cube == '1'):
        cube1 = Cube(cube_points)
    elif(what_cube== '2'):
        cube1 = Cube(cuboid_points)
    elif(what_cube == '3'):
        for i in range(8):
            print(f"Point - {i+1}")
            for j in range(3):
                point = int(input(f'Coordinate-{chr(j+120)}: '))
                cube_points[i][j] = point
        cube1 = Cube(cube_points)

    interface(cube1)
        
cube()
