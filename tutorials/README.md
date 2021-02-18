## How to use Jupyter Notebooks

The Jupyter Notebook tutorials are intended to help learn concepts relevant to the driver video challenge competition. They can also be a good review for anyone who had had experience working with video data or driver video data in the past. 

Currently this directory contains two jupyter notebook tutorials although more will be added throughout the competition. The sections below will explain how to run the jupyter notebooks although it is recommended to use the provided Binder links which allow the notebooks to be run in your browser without additional setup. It is also an option to set up Jupyter locally which can be explained in the section <b>How to set up Jupyter Locally</b>


## How to set up Juptyer locally

The steps below will help you set up Jupyter on your local environment so that you are able to run the provided notebooks. 

1. First, you should install [Anaconda](https://www.anaconda.com/). The instructions can be found at this [here]( https://docs.anaconda.com/anaconda/install/windows/). 
2. After installing Anaconda you need to open the Anaconda command prompt and use the following command to create a new environment using the environment.yml file provided in the jupyter notebook folder for the notebook you are trying to access: `conda env create -f environment.yml`
3. Once the environment has been created you can type `conda env list` to see all active environments and `conda activate [environment name]` to start the environment
4. To install jupyter notebook in the environment run `conda install -c conda-forge notebook`. Now that the notebook has been installed you can navigate to the desired directory and run the command `jupyter notebook`.

## Run the notebook using Binder

If you do not wish to install the environment using the above method this notebook can be run without local setup at the binder link provided in notebook directory README. Binder can be used to run a jupyter notebook in your browser by building a docker image of a github repository. The links are also provided below in the section titled <b>Binder links</b>.


## Binder Links

[<b> Action Preservation </b>](https://mybinder.org/v2/gh/andrewboka/actionpreservation/main?filepath=action_preservation_gaze_estimator.ipynb)

[<b> Judging </b>](https://mybinder.org/v2/gh/andrewboka/judging/27950dd30ee7e8f9064a66eca616b44d4a1bcad2?filepath=identification_measurement.ipynb)
