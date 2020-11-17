## Outline


## General Overview of Data

###  What is it?
The data gathered for this challenge uses the same data acquisition system as the <b>SHRP 2 dataset</b>. 

>The SHRP2 dataset was collected as part of the <b>Naturalistic Driving Study (NDS) </b> and contains <b> millions of hours and petabytes of driver video data </b> that can be used by researchers to gain a better understanding about the underlying causes of car crashes.

The videos contained in this folder are not part of the Naturalistic Driving Study and are intended to be used as a test set for this competition. The same data acquisition system was used in order to provide a realistic dataset to study.


### Levels of Difficulty
The videos are organized into folders based on estimated difficulty to perform de-identification. This difficulty is based on a combination of video quality as well as the action being performed in the video. Generally, Level 1 data should be easier to perform de-identification and action preservation than Level 2, which should also be easier than Level 3. Some individual videos in each Level may stand out as being particularly difficult but in general the overall performance for each Level will be more important than performance on one particular video.

## How to Use Video Parser Script

### Purpose
The provided video_parser.exe script will organize the videos according to their actions within each level. For example, running the video parser in the initial data folder will create 3 new folders: 1) Level 1 actions, 2) Level 2 actions, 3) Level 3 actions. Each folder will contain sub-folders titled according to the actions present in the videos contained within each folder. This is included as participants may find it useful to have some of the video data organized according to actions in order to test their implementation on specific actions.

### Windows
If you have Python installed, simply open the command prompt, navigate to the appropriate folder and type the command `python video_parser.py` . Sometimes you may be required to use `python3` instead of `python` when executing this command.

Alternatively, you can navigate to the same folder and simply run the `video_parser.exe` file.

<b>Note:</b> Do not move the scripts to a different location

### Mac
Make sure you have python >= 3.5 installed and run the script `video_parser.py` inside the Videos folder.

### Output
Running the python script will create the folders `Easy_actions`, `Medium_actions` and `Hard_actions` which each contain subfolders titled according to a specific action. Inside each of these folders, you will find videos corresponding to the action in the video.

You can re-run the above script if you accidentally delete or corrupt some of the files to get a fresh copy of the directories containing the videos. If you delete some of the videos from the original `Easy`, `Medium` or `Hard`, the script will not replace any of the original files and will simply create action folders based on the current available files.  Notice that action folders will not be created if there are no videos corresponding to a specific action in their respective difficulty groups.

## How to use RetinaFace Detection Coordinates

### 