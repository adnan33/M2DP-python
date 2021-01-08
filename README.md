# M2DP python
 python implementation of the M2DP algorithm. Original repository can be found [here](https://github.com/LiHeUA/M2DP).
 

## Introduction:
 Multiview 2D projection (M2DP) is a global descriptor of input point cloud.
 
 ```
  Input:
       data        n*3     Point cloud. Each row is [x y z]
 Output:
       desM2DP     192*1   M2DP descriptor of the input cloud data
       A           64*128  Signature matrix
 ```
 Details of M2DP can be found in the following paper:

 Li He, Xiaolong Wang and Hong Zhang, M2DP: A Novel 3D Point Cloud 
 Descriptor and Its Application in Loop Closure Detection, IROS 2016.

 Li He, Dept. of Computing Science, University of Alberta
 lhe2@ualberta.ca
 
## Requirement
- Python 3.6
- Numpy 
- Scikit-Learn


## usage 

**Follow the below format to extract features from pointcloud:**

```
from m2dp import M2DP
des,A=M2DP(point_cloud)

```

## Acknowledgement

Thanks to  [@jubaer145](https://github.com/jubaer145) for your help in this project.

## Reference

		@inproceedings{he2016m2dp,
	  title={M2DP: A novel 3D point cloud descriptor and its application in loop closure detection},
	  author={He, Li and Wang, Xiaolong and Zhang, Hong},
	  booktitle={2016 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
	  pages={231--237},
	  year={2016},
	  organization={IEEE}
	}


## Copyright
See [LICENSE](LICENSE) for details.
