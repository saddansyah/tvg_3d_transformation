# Kelompok 10 :
# 1. Christina Angraeni Panellah    - 456840
# 2. Faizah Bestiyana Darmawati     - 456364
# 3. Imam Arif Hadi Pramono         - 460546
# 4. Luthfi Izzuddin Hanif          - 463605
# 5. Saddan Syah Akbar              - 460566

from cube import *
import os

# kubus
def cube():
    # membuat objek cube1
    cube1 = Cube()

    while True:
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        print("-----------------------------------------------------")
        transform = (input(
            """What kind of transformation would you like to do ? 
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
            cube1.cube_rotating(x,y,z,type,r_axisx,r_axisy,r_axisz)
            cube1.undraw_geometry()
            cube1.draw_geometry(cube1.projected_cube())
        elif (transform == '3'):
            type = input('choose: xy / yz / xz ? ')
            cube1.cube_shearing(x,y,z, type)
            cube1.undraw_geometry()
            cube1.draw_geometry(cube1.projected_cube())
        elif (transform == '1'):
            cube1.cube_translation(x,y,z)
            print(cube1.get_coord())
            cube1.undraw_geometry()
            cube1.draw_geometry(cube1.projected_cube())
        elif (transform == '2'):
            cube1.cube_scaling(x,y,z)
            cube1.undraw_geometry()
            cube1.draw_geometry(cube1.projected_cube())
        else:
            print("error on input, please try again")

cube()
