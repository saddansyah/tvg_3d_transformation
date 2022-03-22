from cube import *
import os

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
        type = input('x / y / z ?')
        cube1.cube_rotating(x,y,z, type)
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