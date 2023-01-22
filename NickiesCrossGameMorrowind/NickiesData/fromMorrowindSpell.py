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

# Dict for converting spell effects
convertDict = {
	0:"WABR",
	1:"SWSW",
	2:"WAWA",
	3:"SHLD",
	4:"FISH",
	5:"LISH",
	6:"FRSH",
	7:"BRDN",
	8:"FTHR",
	9:"JUMP",
	10:"LEVI",
	11:"LEVI",
	12:"NONE",
	13:"OPEN",
	14:"FIDG",
	15:"SHDG",
	16:"FRDG",
	17:"DRAT",
	18:"DRHE",
	19:"DRSP",
	20:"DRFA",
	21:"DRSK",
	22:"DGAT",
	23:"DGHE",
	24:"DGSP",
	25:"DGFA",
	26:"NONE",
	27:"DGHE",
	28:"WKFI",
	29:"WKFR",
	30:"WKSH",
	31:"WKMA",
	32:"WKDI",
	33:"WKDI",
	34:"WKDI",
	35:"WKPO",
	36:"WKNW",
	37:"DIWE",
	38:"DIAR",
	39:"INVI",
	40:"CHML",
	41:"LGHT",
	42:"RSNW",
	43:"NEYE",
	44:"CHRM",
	45:"PARA",
	46:"SLNC",
	47:"BLIN",
	48:"SLNC",
	49:"CALM",
	50:"CALM",
	51:"FRNZ",
	52:"FRNZ",
	53:"DEMO",
	54:"DEMO",
	55:"RALY",
	56:"RALY",
	57:"DSPL",
	58:"STRP",
	59:"TELE",
	60:"MARK",
	61:"RECA",
	62:"DIVI",
	63:"NONE",
	64:"DTCT",
	65:"NONE",
	66:"NONE",
	67:"SABS",
	68:"RFLC",
	69:"CUDI",
	70:"CUDI",
	71:"CUDI",
	72:"CUPO",
	73:"CUPA",
	74:"REAT",
	75:"REHE",
	76:"RESP",
	77:"REFA",
	78:"NONE",
	79:"FOAT",
	80:"FOHE",
	81:"FOSP",
	82:"FOFA",
	83:"FOSK",
	84:"FOMM",
	85:"ABAT",
	86:"ABHE",
	87:"ABSP",
	88:"ABFA",
	89:"NONE",
	90:"RSFI",
	91:"RSFR",
	92:"RSSH",
	93:"RSMA",
	94:"RSDI",
	95:"RSDI",
	96:"RSDI",
	97:"RSPO",
	98:"RSNW",
	99:"RSPA",
	100:"NONE",
	101:"TURN",
	102:"ZSCA",
	103:"ZCLA",
	104:"ZDAE",
	105:"ZDRE",
	106:"ZWRA",
	107:"ZSKE",
	108:"ZZOM",
	109:"ZHDZ",
	110:"ZLIC",
	111:"Z009",
	112:"Z008",
	113:"Z010",
	114:"ZFIA",
	115:"ZFRA",
	116:"ZSTA",
	117:"FATT",
	118:"COCR",
	119:"COHU",
	120:"BWDA",
	121:"BWSW",
	122:"BWMA",
	123:"BWAX",
	124:"NONE",
	125:"BWBO",
	126:"NONE",
	127:"BACU",
	128:"BAHE",
	129:"BABO",
	130:"BASH",
	131:"BAGA",
	132:"NONE",
	133:"NONE",
	134:"NONE",
	135:"SUDG",
	136:"STMA",
	137:"NONE",
	138:"NONE",
	139:"Z005",
	140:"NONE",
	141:"NONE",
	142:"NONE",
	1000:"REDG"
}

# Dict for converting spell type (Power, Lesser Power, etc.)
type_Dict = {
	0:0,
	1:4,
	2:1,
	3:1,
	4:4,
	5:2
}

# Converting Actor Values for skills
skillsMWtoOBAVDict = {
	0:15,
	1:12,
	2:18,
	3:18,
	4:16,
	5:14,
	6:16,
	7:14,
	8:13,
	9:25,
	10:22,
	11:20,
	12:23,
	13:21,
	14:24,
	15:25,
	16:19,
	17:27,
	18:30,
	19:31,
	20:26,
	21:27,
	22:14,
	23:28,
	24:29,
	25:32,
	26:17
}

# First make a copy of the Morrowind version of the JSON
shutil.copyfile(MWfull_path, OBfull_path)

new_dict = {
	"Spell":{},
	"Reset":{}
}

with open(OBfull_path) as json_file:
	# Load the file
	data = json.load(json_file)
	data = data["Spell"]
	#print(data)
	# Get the last effect number (no more than 8)
	lastEffect = data["Spell0LastEffectNumber"]
	# Convert Spell Type and force Powers cost 0 magicka
	data["Spell0Type"] = type_Dict[data["Spell0Type"]]
	if data["Spell0Type"] == 2:
		data["Spell0Cost"] = 0
		##print("Last effect #: " + str(lastEffect))
	# Go through each effect and make the necessary changes
	while(counter <= lastEffect):
		effectIDString = baseString + str(counter) + "effect"
			##print(data[effectIDString])
		# Change the effect id to the Oblivion version
		data[effectIDString] = convertDict[data[effectIDString]]
		# Turn invalid effects into a dummy effect to avoid errors
		if data[effectIDString] == 'NONE':
			##print("Dummy effect!")
			data[effectIDString] = 'FOAT'
			effectAttString = baseString + str(counter) + "attribute"
			data[effectAttString] = 7
			effectMagString = baseString + str(counter) + "magnitude"
			data[effectMagString] = 0
			effectDurString = baseString + str(counter) + "duration"
			data[effectDurString] = 0
		# If the effect concerns skills, change the skill AV to the Oblivion value
		elif data[effectIDString] == 'FOSK' or data[effectIDString] == 'DRSK':
				##print(effectIDString)
			effectAttString = baseString + str(counter) + "attribute"
				##print(effectAttString)
			data[effectAttString] = skillsMWtoOBAVDict[data[effectAttString]]
		elif data[effectIDString] == 'SWSW':
			data[effectIDString] = 'FOSK'
			effectAttString = baseString + str(counter) + "attribute"
				##print(effectAttString)
			data[effectAttString] = 13
		elif data[effectIDString] == 'LEVI':
			data[effectIDString] = 'FOSK'
			effectAttString = baseString + str(counter) + "attribute"
				##print(effectAttString)
			data[effectAttString] = 26
		elif data[effectIDString] == 'JUMP':
			data[effectIDString] = 'FOSK'
			effectAttString = baseString + str(counter) + "attribute"
				##print(effectAttString)
			data[effectAttString] = 26
			effectMagString = baseString + str(counter) + "magnitude"
				##print(effectAttString)
			data[effectMagString] = data[effectMagString] * 3
		elif data[effectIDString] == 'BLIN':
			data[effectIDString] = 'DRAT'
			effectAttString = baseString + str(counter) + "attribute"
				##print(effectAttString)
			data[effectAttString] = 3
		elif data[effectIDString] == 'FATT':
			data[effectIDString] = 'FOAT'
			effectAttString = baseString + str(counter) + "attribute"
				##print(effectAttString)
			data[effectAttString] = 3

		counter = counter + 1
			##print(data[effectIDString])
			##print(data)

# Assign the changed values to our dict
new_dict["Spell"] = data
new_dict["Reset"] = {"ResetJSON":0}

# Delete the old Oblivion version of the JSON
os.remove(OBfull_path)
# Create a new JSON with our finished dict
with open(OBfull_path, 'w') as f:
    json.dump(new_dict, f, indent=4)
f.close()