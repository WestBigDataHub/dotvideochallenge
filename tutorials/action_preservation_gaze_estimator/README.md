# Measuring Action Preservation via Gaze Estimation

Measuring how well actions are preserved in identity-masked driver videos is an essential consideration when anonymizing driver data for further research. The primary goal is to de-identify the subjects in video, however maximizing the action information in the video defines how useful the data can be.

This repository contains an implementation of an action preservation measuring technique using a deep learning based gaze-estimator. 

## Outline

1. [Dependencies and Installation](#Dependencies-and-Installation)
2. [Directory Structure & Usage](#directory-structure--usage)
3. [Testing](#testing)
4. [List of Papers](#list-of-papers)


## Dependencies and Installation


We have tested this code in Google Colab with the following:
* Python 3.6
* PyTorch 1.7
* CUDA 10.1

If used on a cloud-based environment like Google Colab, zip the repository first before upload.

## Run locally using Jupyter Notebook

In order to run Jupyter locally it is recommended to first install [Anaconda](https://www.anaconda.com/). The instructions can be found at this [here]( https://docs.anaconda.com/anaconda/install/windows/). 

Once you have installed Anaconda it can be used to install Jupyter Notebook using the command `conda install -c conda-forge notebook`. Once installed, jupyter notebook can be run with the command jupyter notebook from the desired directory.

Some helpful links to get started with jupyter and anaconda environments: 
- https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html
- https://medium.com/@nrk25693/how-to-add-your-conda-environment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084

## Run the notebook using Binder

If you do not wish to install the environment using the above method this notebook can be run without local setup at the following link: https://mybinder.org/v2/gh/andrewboka/actionpreservation/b606178c26273ef06e1d878c6cb36d93b2ee823c?filepath=action_preservation_gaze_estimator.ipynb

Binder can be used to run a jupyter notebook in your browser by building a docker image of a github repository. The repository hosting the binder image is currently located at https://github.com/andrewboka/judging. You can learn more about binder by visiting their website at https://mybinder.org.



## Directory Structure & Usage

* `models`: Contains neural net gaze estimator and pre-trained weights from [Mobile FaceGaze](https://github.com/glefundes/mobile-face-gaze).
* `mtcnn`: Contains face-detection model from [Mobile FaceGaze](https://github.com/glefundes/mobile-face-gaze).

The repository also provides an example video and Jupyter notebook file of the gaze estimation based action preservation measure implementation. 

For use, run the Jupyter notebook cells in order. The notebook imports necessary packages and input videos. 
## Testing

The action preservation is estimated by extracting the predicted gaze-vectors from both the original un-filtered video and de-identified video and measuring the difference between the two vectors. Scoring closer to 0 implies effective action preservation since the gaze estimation is relatively unchanged. 

Currently the notebook computes this score for one frame of the video, but further code additions will be added to support computation over all frames in the video. Once the difference values are measured for every frame, an average can be computed for a more robust estimate of action preservation.

## List of Papers

The following lists titles of papers from this project.
1. Zhang, X., Sugano, Y., Fritz, M., Bulling, A.: [It's Written All Over Your
Face: Full-Face Appearance-Based Gaze Estimation](https://openaccess.thecvf.com/content_cvpr_2017_workshops/w41/html/Bulling_Its_Written_All_CVPR_2017_paper.html). In: IEEE Conference
on Computer Vision and Pattern Recognition Workshops. pp. 51–60 (2017).
2.  Kaipeng Zhang, Zhanpeng Zhang, Zhifeng Li, and Yu Qiao.
[Joint face detection and alignment using multitask cascaded
convolutional networks](https://arxiv.org/abs/1604.02878). SPL, 2016

