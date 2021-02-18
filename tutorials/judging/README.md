## Run locally using Jupyter Notebook

In order to run Jupyter locally it is recommended to first install [Anaconda](https://www.anaconda.com/). The instructions can be found at this [here]( https://docs.anaconda.com/anaconda/install/windows/). 

Once you have installed Anaconda it can be used to install Jupyter Notebook using the command `conda install -c conda-forge notebook`. Once installed, jupyter notebook can be run with the command jupyter notebook from the desired directory.

Some helpful links to get started with jupyter and anaconda environments: 
- https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html
- https://medium.com/@nrk25693/how-to-add-your-conda-environment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084

## Run the notebook using Binder

If you do not wish to install the environment using the above method this notebook can be run without local setup at the following link: https://mybinder.org/v2/gh/andrewboka/judging/27950dd30ee7e8f9064a66eca616b44d4a1bcad2?filepath=identification_measurement.ipynb

Binder can be used to run a jupyter notebook in your browser by building a docker image of a github repository. The repository hosting the binder image is currently located at https://github.com/andrewboka/actionpreservation. You can learn more about binder by visiting their website at https://mybinder.org.


## About the Video folder

The folder Video contains three 'buckets' of data examples: Easy, Medium, and Hard. The assigned difficulty was based on the performance of a custom face characterization algorithm developed in 2017 for FHWA.  There are 240 videos in each bucket.


The names follow the general format: `TXXX_..._YYY.mp4`
- XXX ranges from 002 to 010 and is the participant number.
- YYY is the action performed.

Note that all the participants in these videos agreed to have their facial data shared publicly for research purposes.


The folder "RetinaFaceDetections" also has three buckets of data examples. These buckets and the files correspond to each video in the Video folders.  Each row contains the frame number, the bounding box for the detected face, and five landmark points for each face.  These were detected using the 'RetinaFace' algorithm and implementation.

https://github.com/deepinsight/insightface/tree/master/RetinaFace

Finally, the file Face average-CMU-Intraface.png is provided for any challengers who wish to utilize a source face for identity masking.  If the method attempts to replace a video face with a proxy face, this image is the face that should be used.

