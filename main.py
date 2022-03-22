from cube import *

# instance objek cube1 
cube1 = Cube()

# obj cube1 dikenai transformasi seperti di bawah
cube1.cube_translation(120, 120, 120)
# cube1.cube_scaling(3,3,3)
# cube1.cube_shearing(0.2,0.2,0.2,'xz')
# cube1.cube_shearing(0.2,0.2,0.2,'yz')
# cube1.cube_scaling(0.5, 0.2, 0.5)
cube1.cube_rotating(0, 0, 0, 'x')

print(cube1.get_coord())

# koordinat 3d cube1 diprojeksikan menggunakan cabinet projection method biar bisa ditampilin di 2d (di layar)

cube1.draw_geometry(cube1.projected_cube())
