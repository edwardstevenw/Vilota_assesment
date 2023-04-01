import open3d as o3d
import numpy as np
import copy

if __name__ == "__main__":
    pcl = o3d.geometry.PointCloud()
    arr = np.array([[0,0,0],[1,0,0],[1,0,1],[0,0,1],[0.5,0.2,0.5]])  # the shape of the model
    pcl.points = o3d.utility.Vector3dVector(arr)

    R = pcl.get_rotation_matrix_from_zyx((np.pi, 0, np.pi*5/4)) # rotate about Z-axis by 180 and then X-axis by 225
    R2 = pcl.get_rotation_matrix_from_xyz((np.pi/4, 0, 0)) # rotate about X-axis by 45
    
    pcl2 = copy.deepcopy(pcl)

    pcl.rotate(R, center=(0, 0, 0)).translate((1, 1, -2)) # translate X axis by 1, and Z axis by -2 (of the world axis)
    hull, _ = pcl.compute_convex_hull()
    hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
    hull_ls.paint_uniform_color((1, 0, 0))

    
    pcl2.rotate(R2, center=(0, 0, 0))
    hull2, _ = pcl2.compute_convex_hull()
    hull_ls2 = o3d.geometry.LineSet.create_from_triangle_mesh(hull2)
    hull_ls2.paint_uniform_color((0, 1, 0))
    
    o3d.visualization.draw(
        [pcl, pcl2, hull_ls, hull_ls2])