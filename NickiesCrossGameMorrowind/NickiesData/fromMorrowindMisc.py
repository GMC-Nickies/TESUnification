import json
import os
import shutil

#Change this to your MWSE filepath, in your Morrowind Data Files directory
MWfilepath = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Morrowind\\Data Files\\MWSE\\'
#Change this to your Oblivion Data directory path
OBfilepath = 'C:\\Games\\Oblivion\\Data\\'
#Don't edit this or anything below
filename = 'BossData.json'
MWfull_path = MWfilepath + filename
OBfull_path = OBfilepath + filename

# Copy the Oblivion file as-is to modify it
shutil.copyfile(MWfull_path, OBfull_path)

