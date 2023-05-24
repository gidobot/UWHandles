# Underwater Handles Dataset (UWHandles_dataset)

his is a meta repository for UWHandles dataset, which can be downloaded from this link:  
[**[UWHandles]**](https://deepblue.lib.umich.edu/data/concern/data_sets/c821gk19x?locale=en)

Dataset Creators: G. Billings, M. Johnson-Roberson

Dataset Contact: Gideon Billings gidobot@umich.edu

Funding: NNX16AL08G (NASA)

## Key Points

- This is a dataset for developing and testing methods for 6D object pose estimation from underwater monocular images captured in natural deep sea environments.
- The dataset was collected with a monocular fisheye camera and provides annotations for raw fisheye images as well as center rectified perspective images projected from the raw images.
- The dataset provides 6D pose and 2D bounding box annotations for 3 different graspable handle objects, typical of the type used for tool manipulation with Remotely Operated Vehicles (ROVs).
- The dataset has 28 unique image sequences with a total of 20,427 annotated images.

## Research Overview

Computer vision in underwater environments is significantly more difficult than in terrestrial environments, due to the physical absorption and scattering properties of water on light. Induced lighting effects like haze, backscatter, caustics and vinnetting all compound to increase the noise and artifacts present in underwater imagery. Underwater datasets are also difficult and expensive to collect in underwater environments, due to the specialized, sealed hardware needed to work in these environemnts. This dataset provides annotated imagery for object pose estimation from deep ocean environments, which are particularly difficult to reach. While this dataset is useful for developing general computer vision methods for object detection and pose estimation for the underwater environment, it is particulary relevant to automating underwater manipulation tasks; if the pose of a handle attached to a known tool type can be accurately estimated, the handle can be autonomously grasped and manipulated to perform a desired manipulation task.

## Methodology

We collected fisheye images of three different types of graspable handles, randomly arranged in different natural seafloor environments of the Costa Rican shelf break. Two of the handle types are actively used by Schmidt Ocean Institute and Woods Hole Oceanographic Institution to manipulate tools with Remotely Operated Vehicles (ROV) during underwater operations. AprilTag fiducials were randomly dispersed throughout the scene and on mount plates attached to the base of the handle objects in order to recover ground truth poses of the camera in the image sequences. The image sequences were then post processed with an annotation tool to obtain labeled 6D object poses and bounding boxes. The camera system was a FLIR BFLY-PGE-50S5C-C with a Fujinon FE185C086HA-1 fisheye lens centered in a dome housing that was mounted on the wrist of a Schilling Titan 4 hydraulic manipulator. The dataset is composed of 25 training image sequences with a total of 18,329 images, 1 validation sequence with 910 images, and 2 testing sequences with 1,188 images.

## Files Contained Here

For each sequence, the images are numbered incrementally starting from 0 as .png. The fisheye camera was calibrated using the Kalibr toolbox with the equidistant distortion model, and the calibration yaml files for both the raw fisheye and the center rectififed images are in the format output by Kalibr (https://github.com/ethz-asl/kalibr/wiki/camera-imu-calibration).

THe camera_poses.txt CSV file for each sequence gives a globally referenced camera pose for each image in the sequence, with the line format ", x, y, z, qw, qx, qy, qz", where [x,y,z] is the translation in meters and [qw,qx,qy,qz] is the rotation as a quaternion. The annotation json files use COCO sytle 6D pose and 2D bounding box annotations (https://cocodataset.org/#home). These annotations were generated with the VisPose tool (https://github.com/gidobot/VisPose) that was created as part of this work. VisPose can be used to visualize the annotations. Note that the VisPose version used to generate this dataset has the commit date May 13, 2020.

The object models were created in Blender and use material definitions for realistic textures when creating renders.

Visualized below is a sample annotated sequence, showing center rectified fisheye images for visualization of the model handle projections.

![Output sample](https://github.com/gidobot/gifs/raw/master/VisPose_Reviewer.gif)

Globally consistent camera poses for input to the VisPose annotation tool were generated using the ROS based [**TagSLAM**](https://berndpfrommer.github.io/tagslam_web/) package. Below is a sample sequence showing the AprilTag detector and TagSLAM estimated camera poses.

![Output sample](https://github.com/gidobot/gifs/raw/master/VisPose_AprilSLAM.gif)

## File Structure
 ```
UWHandles
└───calibration
│ │ fisheye_calib.yaml -> calibration file for fisheye
│ │ rectified_calib.yaml -> calibration file for rectified fisheye
└───data
│ └───set#
│ │ camera_poses.txt -> CSV file of globally referenced camera poses for each image in sequence, with each line formated as $, x, y, z, qw, qx, qy, qz$
│ └───images
│ │ annotations.json -> COCO style 6D pose and 2D bounding box annotations generated by the VisPose annotation tool for the rectified image sequence
│ │ annotations_culled.json -> culled annotations with bounding boxes for rectified images
│ │ annotations_fisheye_culled.json -> culled annotations with bounding boxes regenerated for raw fisheye images
│ └───raw -> folder containing raw fisheye images
│ └───rect -> folder containing center rectified images
└───image_sets -> contains text files which list the image sets for training, testing, and validation
└───models
└───
│ textured_real.obj -> obj files for the 3 different handle objects in the dataset
│ textured_real.mtl -> material definition for obj file
```
## Use and Access

This data set is made available under a Creative Commons Public Domain license (CC0 1.0).

## How to Cite
```
@ARTICLE{9091344,
 author={G. {Billings} and M. {Johnson-Roberson}},
 journal={IEEE Robotics and Automation Letters},
 title={SilhoNet-Fisheye: Adaptation of A ROI-Based Object Pose Estimation Network to Monocular Fisheye Images},
 year={2020},
}
```
