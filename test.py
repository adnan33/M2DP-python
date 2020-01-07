import pickle
import numpy as np
import pandas as pd
import open3d as o3d
from open3d import JVisualizer
from open3d.open3d.geometry import voxel_down_sample,estimate_normals
import cmath
from m2dp import M2DP
#reading demo 3d model
pcd = o3d.io.read_point_cloud("airplane.ply")
#converting point cloud to numpy array
a=np.array(pcd.points)
#extracting M2DP feature of the point cloud
desM2DP,A=M2DP(a)
