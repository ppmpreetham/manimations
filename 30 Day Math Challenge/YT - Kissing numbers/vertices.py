import numpy as np
import matplotlib.pyplot as plt

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
    
    x_3d = x / (1 - w / D)
    y_3d = y / (1 - w / D)
    z_3d = z / (1 - w / D)
    vertices_3d.append([x_3d, y_3d, z_3d])

vertices_3d = np.array(vertices_3d)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(vertices_3d[:, 0], vertices_3d[:, 1], vertices_3d[:, 2])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
