import bpy
import bmesh
from math import sqrt
from mathutils import Vector

context = bpy.context
scene = context.scene
me = bpy.data.meshes.new("tetstar")
bm = bmesh.new()
bm.from_mesh(me)
TOL = 0.001
# add triangle cone
bmesh.ops.create_cone(bm,
        diameter1=1,
        diameter2=0,
        cap_ends=True,
        depth=sqrt(2),
        segments=3)
# fix the origin
o = sum((v.co for v in bm.verts), Vector()) / len(bm.verts)
for v in bm.verts:
    v.co -= o
# keep track of centres.
centres = [f.calc_center_median() for f in bm.faces]
sub = bmesh.ops.subdivide_edges(bm,
        edges=bm.edges,
        use_grid_fill=True,
        use_single_edge=True,
        cuts=1)
# use original tetra faces to find sub middle faces  
new_faces = [f for f in sub["geom_inner"] 
        if isinstance(f, bmesh.types.BMFace)
        and any((f.calc_center_median() - c).length < TOL for c in centres) ]
# and poked vert
poke = bmesh.ops.poke(bm, faces=new_faces)
verts = [v for v in poke["verts"] 
        if any((v.co - c).length < TOL for c in centres)]    
# scale them out
for v in verts:
    v.co *= 3
# write mesh and create object.    
bm.to_mesh(me) 
ob = bpy.data.objects.new("TetraStar", me)
scene.objects.link(ob)