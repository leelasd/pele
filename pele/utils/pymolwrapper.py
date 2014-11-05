import pymol
from pymol import cmd, cgo

def start():
    pymol.finish_launching()

def draw_spheres(coords, model, frame, radius=0.5):
    spheres=[]
    for x in coords.reshape(coords.size/3,3):
        spheres.extend([cgo.COLOR, 1.0, 0.0, 0.0])
        spheres.extend([cgo.SPHERE, x[0], x[1], x[2], radius])

    cmd.load_cgo(spheres, model, frame)

# sn402: new function for visualising rigid molecules
def draw_rigid(coords, model, frame, colour, radius=0.5):
    ''' Colour should be a 3-tuple representing the colour for these spheres'''
    spheres=[]
    for x in coords.reshape(coords.size/3,3):
        spheres.extend([cgo.COLOR, colour[0], colour[1], colour[2]])
        spheres.extend([cgo.SPHERE, x[0], x[1], x[2], radius])
        

        cyl_color = [1., 0., 0.]
        cyl_grad = [0., 0., 0.]
        Rcyl = .1

#         spheres.extend([cgo.CYLINDER]
#                        + coords[i-2,:].tolist()
#                        + coords[i  ,:].tolist()
#                        + [Rcyl] + cyl_color + cyl_grad)

    cmd.load_cgo(spheres, model, frame)    