import bpy
from math import sqrt
from itertools import combinations

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

vertices_4d = [
    [1, 1, 0, 0], [1, -1, 0, 0], [-1, 1, 0, 0], [-1, -1, 0, 0],
    [1, 0, 1, 0], [1, 0, -1, 0], [-1, 0, 1, 0], [-1, 0, -1, 0],
    [1, 0, 0, 1], [1, 0, 0, -1], [-1, 0, 0, 1], [-1, 0, 0, -1],
    [0, 1, 1, 0], [0, 1, -1, 0], [0, -1, 1, 0], [0, -1, -1, 0],
    [0, 1, 0, 1], [0, 1, 0, -1], [0, -1, 0, 1], [0, -1, 0, -1],
    [0, 0, 1, 1], [0, 0, 1, -1], [0, 0, -1, 1], [0, 0, -1, -1]
]

D = 5
vertices_3d = []
for v in vertices_4d:
    x, y, z, w = v
    x_3d = x / (1 - w/D)
    y_3d = y / (1 - w/D)
    z_3d = z / (1 - w/D)
    vertices_3d.append([x_3d, y_3d, z_3d])

def create_material(name, color):
    material = bpy.data.materials.new(name=name)
    material.use_nodes = True
    material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (*color, 1)
    return material

vertex_material = create_material("VertexMaterial", (0, 0, 1))  
edge_material = create_material("EdgeMaterial", (1, 0, 0))      

def create_vertex(location, radius=0.05):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=location)
    sphere = bpy.context.active_object
    sphere.data.materials.append(vertex_material)
    return sphere

def create_edge(start, end, radius=0.02):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    dz = end[2] - start[2]
    dist = sqrt(dx*dx + dy*dy + dz*dz)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=dist)
    cylinder = bpy.context.active_object
    cylinder.data.materials.append(edge_material)
      
    mid_point = [(start[i] + end[i])/2 for i in range(3)]
    cylinder.location = mid_point
      
    from math import acos, atan2, pi
    phi = atan2(dy, dx)
    theta = acos(dz/dist)
    cylinder.rotation_euler[1] = theta
    cylinder.rotation_euler[2] = phi
    
    return cylinder

vertex_objects = [create_vertex(loc) for loc in vertices_3d]

def squared_distance_4d(v1, v2):
    return sum((a - b) ** 2 for a, b in zip(v1, v2))

edges = []
for i, j in combinations(range(24), 2):
    if squared_distance_4d(vertices_4d[i], vertices_4d[j]) == 2:
        edges.append((i, j))

for edge in edges:
    start, end = edge
    create_edge(vertices_3d[start], vertices_3d[end])

bpy.ops.object.camera_add(location=(5, 5, 5))
camera = bpy.context.active_object
camera.rotation_euler = (0.9, 0, 2.3)

bpy.ops.object.light_add(type='SUN', location=(5, 5, 5))

scene = bpy.context.scene