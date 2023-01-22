import json
import os
import shutil

#Change this to your MWSE filepath, in your Morrowind Data Files directory. Make sure to use double slashes like the example below
MWfilepath = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Morrowind\\Data Files\\MWSE\\'
#Change this to your Oblivion Data directory path. Make sure to use double slashes like the example below
OBfilepath = 'C:\\Games\\Oblivion\\Data\\'
#Don't edit this or anything below
filename = 'BossData.json'
MWfull_path = MWfilepath + filename
OBfull_path = OBfilepath + filename

# Copy the Oblivion file as-is to modify it
shutil.copyfile(OBfull_path, MWfull_path)

