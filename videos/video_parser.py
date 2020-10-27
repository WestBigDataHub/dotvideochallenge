import os
from shutil import copyfile
from shutil import rmtree


files = os.listdir()

for file in files:
    if os.path.exists(file + "_actions/"):
        rmtree(file + "_actions/")

files = os.listdir()

for file in files:
    if file.split(".")[0] in ["Easy", "Medium", "Hard"]:
        action_folder = file + "_actions/"
        os.mkdir(action_folder)
        for name in os.listdir(file):
            action = name.split("_")[-1][:-4]
            print(action)

            if (os.path.exists(action_folder + action)):
                copyfile(file + "/" + name, action_folder + action + "/" + name)
            else:
                os.mkdir(action_folder + action)
                copyfile(file + "/" + name, action_folder + action + "/" + name)

