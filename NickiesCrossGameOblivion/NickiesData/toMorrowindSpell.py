import json
import os
import shutil

#Change this to your MWSE filepath, in your Morrowind Data Files directory
MWfilepath = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Morrowind\\Data Files\\MWSE\\'
#Change this to your Oblivion Data directory path
OBfilepath = 'C:\\Games\\Oblivion\\Data\\'
#Don't edit this or anything below
filename = 'SpellData.json'
MWfull_path = MWfilepath + filename
OBfull_path = OBfilepath + filename

baseString = "Spell0Effect"
counter = 0

# Converts Oblivion spell effect ids to Morrowind effect ids
convertDict = {
	'WABR': 0,
	'NONE': -1,
	'WAWA': 2,
	'SHLD': 3,
	'FISH': 4,
	'LISH': 5,
	'FRSH': 6,
	'BRDN': 7,
	'FTHR': 8,
	'OPEN': 13,
	'FIDG': 14,
	'SHDG': 15,
	'FRDG': 16,
	'DRAT': 17,
	'DRHE': 18,
	'DRSP': 19,
	'DRFA': 20,
	'DRSK': 21,
	'DGAT': 22,
	'DGHE': 23,
	'DGSP': 24,
	'DGFA': 25,
	'WKFI': 28,
	'WKFR': 29,
	'WKSH': 30,
	'WKMA': 31,
	'WKDI': 34,
	'WKPO': 35,
	'WKNW': 36,
	'DIWE': 37,
	'DIAR': 38,
	'INVI': 39,
	'CHML': 40,
	'LGHT': 41,
	'NEYE': 43,
	'CHRM': 44,
	'PARA': 45,
	'SLNC': 46,
	'CALM': 50,
	'FRNZ': 52,
	'DEMO': 54,
	'RALY': 56,
	'DSPL': 57,
	'STRP': 58,
	'TELE': 59,
	'MARK': 60,
	'RECA': 61,
	'DIVI': 62,
	'DTCT': 64,
	'SABS': 67,
	'RFLC': 68,
	'RESP': 76,
	'CUDI': 71,
	'CUPO': 72,
	'CUPA': 73,
	'REAT': 74,
	'REHE': 75,
	'REFA': 77,
	'FOAT': 79,
	'FOHE': 80,
	'FOSP': 81,
	'FOFA': 82,
	'FOSK': 83,
	'FOMM': 84,
	'ABAT': 85,
	'ABHE': 86,
	'ABSP': 87,
	'ABFA': 88,
	'RSFI': 90,
	'RSFR': 91,
	'RSSH': 92,
	'RSMA': 93,
	'RSDI': 96,
	'RSPO': 97,
	'RSNW': 98,
	'RSPA': 99,
	'TURN': 101,
	'COCR': 118,
	'COHU': 119,
	'BWDA': 120,
	'BWSW': 121,
	'BWMA': 122,
	'BWAX': 123,
	'BWBO': 125,
	'BACU': 127,
	'BAHE': 128,
	'BABO': 129,
	'BASH': 130,
	'BAGA': 131,
	'SUDG': 135,
	'STMA': 136,
	'ABSK': 89,
	'DRSK': 21,
	'FOSK': 83,
	'BAGR': -1,
	'SEFF': -1,
	'REAN':-1,
	'REDG': 1000,
	'ZCLA': 103,
	'ZDAE': 104,
	'ZDRE': 105,
	'ZDRL': 105,
	'ZFIA': 114,
	'ZFRA': 115,
	'ZGHO': 106,
	'ZHDZ': 109,
	'ZLIC': 110,
	'ZSCA': 102,
	'ZSKA': 107,
	'ZSKC': 107,
	'ZSKE': 107,
	'ZSKH': 107,
	'ZSPD':-1,
	'ZSTA': 116,
	'ZWRA': 106,
	'ZWRL': 106,
	'ZXIV': -1,
	'ZZOM': 108,
	'Z001': 106,
	'Z002': 106,
	'Z003': -1,
	'Z004': 108,
	'Z005': 139,
	'Z006': 112,
	'Z007': 112,
	'Z008': 112,
	'Z009': 111,
	'Z010': 113,
	'Z011': -1,
	'Z012': 107,
	'Z013': 107,
	'Z014': 107,
	'Z015': 112,
	'Z016': 108,
	'Z017': 108,
	'Z018': 109,
	'Z019': 109,
	'Z020': -1,
	-1:-1,

}

# Converts spell types (Power, Spell, etc.)
type_Dict = {
	0:0,
	1:3,
	2:5,
	3:0,
	4:1,
}

# Converts skills. Some skills have to be assigned to nearest equivalent for now and handled later (e.g. Blade to Long Blade)
skillsOBtoMWDict = {
	  12: 1,
	  13: 8,
	  14: 5, 
	  #,22',
	  15: 0,
	  16: 6,
	  #4',
	  17: 26,
	  18: 2,
	  #3',
	  19: 16,
	  20: 11,
	  21: 13,
	  22: 10,
	  23: 12,
	  24: 14,
	  25: 15,
	  26: 20,
	  27: 21,
	  28: 23,
	  29: 24,
	  30: 18,
	  31: 19,
	  32: 25
}

# Copy the Oblivion file as-is to modify it
shutil.copyfile(OBfull_path, MWfull_path)

with open(MWfull_path) as json_file:
	data1 = json.load(json_file)
	data = data1["Spell"]
	# Get number of effects (can not exceed 8) and get the converted spell type
	lastEffect = data["Spell0LastEffectNumber"]
	data["Spell0Type"] = type_Dict[data["Spell0Type"]]
		##print("Last effect #: " + str(lastEffect))

	# For each effect...
	while(counter <= lastEffect):
		# Get the effect ID, convert it to its MW version, then assign the key to the converted version
		effectIDString = baseString + str(counter) + "effect"
			##print(data[effectIDString])
		data[effectIDString] = convertDict[data[effectIDString]]
			##print(data[effectIDString])

		# Convert skills to Morrowind values
		if data[effectIDString] == 21 or data[effectIDString] == 83:
			effectAttString = baseString + str(counter) + "attribute"
			data[effectAttString] = skillsOBtoMWDict[data[effectAttString]]
		counter = counter + 1
##print(data)

# Delete the old Morrowind JSON and replace it with the one we just made and modified
os.remove(MWfull_path)
with open(MWfull_path, 'w') as f:
    json.dump(data1, f, indent=4)
f.close()

