# How to Use


### Windows
Run the script called `video_parser` inside the `Videos` folder

### Mac
Make sure you have python >= 3.5 installed and run the script `video_parser.py` inside the Videos folder.

### Output
Running the python script will create the folders `Easy_actions`, `Medium_actions` and `Hard_actions` which each contain subfolders titled according to a specific action. Inside each of these folders, you will find videos corresponding to the action in the video.

You can re-run the above script if you accidentally delete or corrupt some of the files to get a fresh copy of the directories containing the videos. If you delete some of the videos from the original `Easy`, `Medium` or `Hard`, the script will not replace any of the original files and will simply create action folders based on the current available files.  Notice that action folders will not be created if there are no videos corresponding to a specific action in their respective difficulty groups.