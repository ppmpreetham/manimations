import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

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

def squared_distance_4d(v1, v2):
    return sum((a - b) ** 2 for a, b in zip(v1, v2))

edges = []
for i, j in combinations(range(24), 2):
    if squared_distance_4d(vertices_4d[i], vertices_4d[j]) == 2:
        edges.append((i, j))

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(vertices_3d[:, 0], vertices_3d[:, 1], vertices_3d[:, 2], 
          color='blue', s=50)

for edge in edges:
    start, end = edge
    ax.plot([vertices_3d[start, 0], vertices_3d[end, 0]],
            [vertices_3d[start, 1], vertices_3d[end, 1]],
            [vertices_3d[start, 2], vertices_3d[end, 2]], 
            color='red', linewidth=1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(elev=20, azim=45)

plt.show()