from manim import *
import numpy as np
from itertools import combinations

class TwentyFourCell(ThreeDScene):
    def construct(self):
        # Configuration
        config.disable_caching = True
        
        # 24-cell vertices in 4D
        vertices_4d = [
            [1, 1, 0, 0], [1, -1, 0, 0], [-1, 1, 0, 0], [-1, -1, 0, 0],
            [1, 0, 1, 0], [1, 0, -1, 0], [-1, 0, 1, 0], [-1, 0, -1, 0],
            [1, 0, 0, 1], [1, 0, 0, -1], [-1, 0, 0, 1], [-1, 0, 0, -1],
            [0, 1, 1, 0], [0, 1, -1, 0], [0, -1, 1, 0], [0, -1, -1, 0],
            [0, 1, 0, 1], [0, 1, 0, -1], [0, -1, 0, 1], [0, -1, 0, -1],
            [0, 0, 1, 1], [0, 0, 1, -1], [0, 0, -1, 1], [0, 0, -1, -1]
        ]

        # Project 4D to 3D
        def project_to_3d(vertex, D=5):
            x, y, z, w = vertex
            factor = 1 / (1 - w/D)
            return np.array([x * factor, y * factor, z * factor])

        vertices_3d = [project_to_3d(v) for v in vertices_4d]

        # Generate edges based on 4D distance
        edges = [(i, j) for i, j in combinations(range(24), 2)
                if sum((a - b) ** 2 for a, b in zip(vertices_4d[i], vertices_4d[j])) == 2]

        # Create vertex and edge groups
        vertex_group = VGroup(*[
            Dot3D(point=v, color=BLUE_B, radius=0.05)
            for v in vertices_3d
        ])

        edge_group = VGroup(*[
            Line3D(
                start=vertices_3d[i],
                end=vertices_3d[j],
                color=RED_B,
                thickness=0.02
            )
            for i, j in edges
        ])

        # Combine into main group
        cell_group = VGroup(vertex_group, edge_group)

        # Camera and scene setup
        self.set_camera_orientation(
            phi=75 * DEGREES,
            theta=30 * DEGREES,
            zoom=0.8
        )

        # Animation sequence
        self.add(cell_group)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(
            Rotate(cell_group, angle=2*PI, axis=UP),
            run_time=10,
            rate_func=linear
        )
        self.wait(2)

if __name__ == "__main__":
    with tempconfig({
        "quality": "high_quality",
        "preview": True,
        "frame_rate": 60,
        "pixel_width": 1920,
        "pixel_height": 1080
    }):
        scene = TwentyFourCell()
        scene.render()