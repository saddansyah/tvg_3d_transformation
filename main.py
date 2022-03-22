from cube import *
import os

# kubus
def cube():
    # membuat objek cube1
    cube1 = Cube()

    while True:
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')

        print("-----------------------------------------------------")
        transform = input("translation/scale/shear/rotation ? (type 'stop or STOP' to stop) ")

        if transform.lower() == 'stop':
            break

        x = float(input('x: '))
        y = float(input('y: '))
        z = float(input('z: '))

        if (transform == 'rotation'):
            print("x = y = z = 0 if translate from origin point (0,0,0)")
            r_axisx = float(input('rotate from x: '))
            r_axisy = float(input('rotate from y: '))
            r_axisz = float(input('rotate from z: '))
            print(f"rotate from point = ({round(r_axisx, 2)}, {round(r_axisy, 2)}, {round(r_axisz, 2)})")
            type = input('x / y / z ?')
            cube1.cube_rotating(x,y,z,type,r_axisx,r_axisy,r_axisz)
            cube1.draw_geometry(cube1.projected_cube())
        elif (transform == 'shear'):
            type = input('xy / yz / xz ?')
            cube1.cube_shearing(x,y,z, type)
            cube1.draw_geometry(cube1.projected_cube())
        elif (transform == 'translation'):
            cube1.cube_translation(x,y,z)
            cube1.draw_geometry(cube1.projected_cube())
        elif (transform == 'scale'):
            cube1.cube_scaling(x,y,z)
            cube1.draw_geometry(cube1.projected_cube())
        else:
            print("error on input, try again")

cube()
