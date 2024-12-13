from manim import *

class Projected24Cell(ThreeDScene):
    def construct(self):
        vertices_4d = [
            [1, 1, 0, 0], [1, -1, 0, 0], [-1, 1, 0, 0], [-1, -1, 0, 0],
            [1, 0, 1, 0], [1, 0, -1, 0], [-1, 0, 1, 0], [-1, 0, -1, 0],
            [1, 0, 0, 1], [1, 0, 0, -1], [-1, 0, 0, 1], [-1, 0, 0, -1],
            [0, 1, 1, 0], [0, 1, -1, 0], [0, -1, 1, 0], [0, -1, -1, 0],
            [0, 1, 0, 1], [0, 1, 0, -1], [0, -1, 0, 1], [0, -1, 0, -1],
            [0, 0, 1, 1], [0, 0, 1, -1], [0, 0, -1, 1], [0, 0, -1, -1]
        ]
        
        def project_to_3d(vertex, D=5):
            x, y, z, w = vertex
            x_3d = x / (1 - w / D)
            y_3d = y / (1 - w / D)
            z_3d = z / (1 - w / D)
            return [x_3d, y_3d, z_3d]
                
        vertices_3d = [project_to_3d(v) for v in vertices_4d]
    
        edges = [
            (0, 1), (0, 2), (0, 4), (0, 5), (1, 3), (1, 6), (1, 7),
            (2, 3), (2, 8), (2, 9), (3, 10), (3, 11), (4, 5), (4, 12),
            (4, 13), (5, 14), (5, 15), (6, 7), (6, 16), (6, 17), (7, 18),
            (7, 19), (8, 9), (8, 20), (8, 21), (9, 22), (9, 23), (10, 11),
            (10, 16), (10, 17), (11, 18), (11, 19), (12, 13), (12, 20),
            (12, 21), (13, 22), (13, 23), (14, 15), (14, 16), (14, 18),
            (15, 17), (15, 19), (16, 18), (17, 19), (18, 20), (19, 21),
            (20, 22), (21, 23)
        ]
        
        vertices_mobjects = [Dot3D(point=vertex, color=BLUE) for vertex in vertices_3d]
        lines = [
            Line3D(start=vertices_3d[start], end=vertices_3d[end], color=RED)
            for start, end in edges
        ]
        
        # Create a group containing all objects
        cell_group = VGroup()
        for vertex in vertices_mobjects:
            cell_group.add(vertex)
        for line in lines:
            cell_group.add(line)
            
        self.add(cell_group)
        
        # Set initial camera position
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Animate the entire group
        self.play(
            Rotate(cell_group, angle=PI/2, axis=UP),
            run_time=3
        )
        self.wait(1)

if __name__ == "__main__":
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 60
    config.quality = "high"

    scene = Projected24Cell()
    scene.render()