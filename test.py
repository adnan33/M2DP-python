import pickle
import numpy as np
import pandas as pd
import open3d as o3d
from open3d import JVisualizer
from open3d.open3d.geometry import voxel_down_sample,estimate_normals
import cmath
from m2dp.M2DP import *
with open('3d_dataset.pickle', 'rb') as file:
    pcd_data=pickle.load(file)
    linestring_data=pickle.load(file)
    centerpoints_data=pickle.load(file)
    label=pickle.load(file)


a=np.array(pcd_data[0])
print(M2DP(a))
