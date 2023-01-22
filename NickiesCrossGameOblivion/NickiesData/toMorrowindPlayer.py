import json
import os
import shutil

#Change this to your MWSE filepath, in your Morrowind Data Files directory
MWfilepath = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Morrowind\\Data Files\\MWSE\\'
#Change this to your Oblivion Data directory path
OBfilepath = 'C:\\Games\\Oblivion\\Data\\'
#Don't edit this or anything below
MWfull_path = MWfilepath + 'PlayerDataOB.json'
OBfull_path = OBfilepath + 'PlayerDataOB.json'

baseString1 = "Item"
baseString2 = "Effect"
counter1 = 0
counter2 = 0

## TO-DO: Uniques / Artifacts in dict2, then functionalize this and FromMorrowind

# Converts skills from their OB actor values to MW actor values
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

# Converts spell effect ids from OB to MW. Note that some effects are not converted.
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
	'DGAT': 22,
	'DGHE': 23,
	'DGSP': 24,
	'DGFA': 25,
	'WKFI': 28,
	'WKFR': 29,
	'WKSH': 30,
	'WKMA': 31,
	'WKDI': 33,
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
	'CUDI': 70,
	'CUPO': 72,
	'CUPA': 73,
	'REAT': 74,
	'REHE': 75,
	'REFA': 77,
	'FOAT': 79,
	'FOHE': 80,
	'FOSP': 81,
	'FOFA': 82,
	'FOMM': 84,
	'ABAT': 85,
	'ABHE': 86,
	'ABSP': 87,
	'ABFA': 88,
	'RSFI': 90,
	'RSFR': 91,
	'RSSH': 92,
	'RSMA': 93,
	'RSDI': 95,
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

}

# Enchantment types conversion
type_Dict = {
	0:5,
	1:2,
	2:1,
	3:3,
	4:4,
	5:5
}
# Converts spell types (Power, Spell, etc.)
type_Dict2 = {
	0:0,
	1:3,
	2:5,
	3:0,
	4:1,
}

# Dict containing most notable armor
dict2 = {'Armor\\Thief\\M\\Boots': 'boots of blinding speed[unique]',  'Armor\\Mithril\\M\\Cuirass': 'silver_cuirass',  'Armor\\Ebony\\M\\Cuirass': 'ebony_cuirass',  'Armor\\Legion\\M\\Cuirass': 'imperial cuirass_armor',  'Armor\\SaviorsHide\\Cuirass': 'cuirass_savior_unique',  'Armor\\ImperialWatch\\M\\Gauntlets': 'Helsethguard_gauntlet_left',  'Armor\\HelmetOreynBeardaw\\Helmet': 'cephalopod_helm',  'Armor\\SpellBreaker\\Shield': 'spell_breaker_unique',  'Armor\\Elven\\shield': 'bonemold_tshield_telvanniguard',  'Armor\\AmelionCeremonial\\M\\Greaves': 'BM_Ice_greaves',  'Armor\\AmelionCeremonial\\M\\Gauntlets': 'BM_Ice_gauntletL',  'Armor\\AmelionCeremonial\\M\\Cuirass': 'BM_Ice_cuirass',  'Armor\\AmelionCeremonial\\M\\Helmet': 'BM_Ice_Helmet',  'Armor\\AmelionCeremonial\\Shield': 'BM_Ice minion_Shield1',  'Armor\\Chainmail\\Shield': 'BM_NordicMail_Shield',  'Armor\\M\\Chainmail\\Boots': 'BM_NordicMail_Boots',  'Armor\\Chainmail\\M\\Cuirass': 'imperial_studded_cuirass',  'Armor\\Chainmail\\M\\Greaves': 'imperial_chain_greaves',  'Armor\\M\\Chainmail\\Gauntlets': 'BM_NordicMail_gauntletL',  'Armor\\Chainmail\\M\\Helmet': 'imperial_chain_coif_helm',  'Armor\\Blackwood\\Boots': 'adamantium boots',  'Armor\\Blackwood\\Gauntlets': 'adamantium_bracer_left',  'Armor\\Blackwood\\Cuirass': 'adamantium_cuirass',  'Armor\\Blackwood\\Greaves': 'adamantium_greaves',  'Armor\\Blackwood\\Helmet': 'adamantium_helm',  'Armor\\Elven\\Boots': 'indoril boots',  'Armor\\Elven\\Cuirass': 'indoril cuirass',  'Armor\\Elven\\Gauntlets': 'indoril left gauntlet',  'Armor\\Elven\\Greaves': 'Indoril_Almalexia_Greaves',  'Armor\\Elven\\Helmet': 'indoril helmet',  'Armor\\Dwarven\\M\\Gauntlet': 'dwemer_bracer_left',  'Armor\\Fur\\M\\Boots': 'BM_wolf_boots_snow',  'Armor\\Fur\\M\\Cuirass': 'BM_wolf_cuirass_snow',  'Armor\\Fur\\M\\Gauntlets': 'bonedancer gauntlet',  'Armor\\Fur\\M\\Greaves': 'BM_wolf_greaves_snow',  'Armor\\Fur\\M\\Helmet': 'steel_colovian_helm_white',  'Armor\\Blades\\M\\Cuirass': 'bonemold_founders_helm',  'Armor\\Iron\\M\\Cuirass': 'nordic_iron_cuirass',  'Armor\\Iron\\M\\Boots': 'iron boots',  'Armor\\Blades\\M\\Gauntlets': 'bonemold_bracer_left',  'Armor\\Iron\\M\\Greaves': 'iron_greaves',  'Armor\\Iron\\Shield': 'goblin_shield',  'Armor\\MS31BlackWater': 'chest of fire',  'Armor\\Thief\\M\\Greaves': 'netch_leather_greaves',  'Armor\\Daedric\\M\\Boots': 'bound_boots',  'Armor\\Daedric\\M\\Cuirass': 'bound_cuirass',  'Armor\\Daedric\\M\\Helmet': 'bound_helm',  'Armor\\Daedric\\M\\Gauntlets': 'bound_gauntlet_left',  'Armor\\Daedric\\M\\Greaves': 'daedric_greaves',  'Armor\\Thief\\M\\Cuirass': 'netch_leather_cuirass',  'Armor\\Thief\\M\\Gauntlets': 'left leather bracer',  'Armor\\Thief\\M\\Helmet': 'chitin_watchman_helm',  'Armor\\Mithril\\M\\Helmet': 'redoran_master_helm',  'Armor\\Madness\\M\\Cuirass': 'dreugh_cuirass',  'Armor\\Madness\\M\\Helmet': 'dreugh_helm',  'Armor\\Dwarven\\M\\Boots': 'dwemer_boots',  'Armor\\Dwarven\\M\\Curiass': 'dwemer_cuirass',  'Armor\\Dwarven\\M\\Greaves': 'dwemer_greaves',  'Armor\\Dwarven\\M\\Helmet': 'dwemer_helm',  'Armor\\Dwarven\\Shield': 'dwemer_shield',  'Armor\\Ebony\\M\\Boots': 'ebony_boots',  'Armor\\Ebony\\M\\Gauntlets': 'ebony_bracer_left',  'Armor\\Ebony\\M\\Greaves': 'ebony_greaves',  'Armor\\Ebony\\M\\Helmet': 'ebony_closed_helm',  'Armor\\ImperialWatch\\M\\Boots': 'Helsethguard_boots',  'Armor\\ImperialWatch\\M\\Cuirass': 'Helsethguard_cuirass',  'Armor\\ImperialWatch\\M\\Greaves': 'Helsethguard_greaves',  'Armor\\ImperialWatch\\M\\Helmet': 'Helsethguard_Helmet',  'Armor\\Legion\\M\\Boots': 'imperial boots',  'Armor\\Legion\\M\\Gauntlets': 'imperial left gauntlet',  'Armor\\Legion\\M\\Greaves': 'imperial_greaves',  'Armor\\Legion\\M\\Helmet': 'imperial helmet armor',  'Armor\\Legion\\Shield': 'feather_shield',  'Armor\\Iron\\M\\Gauntlets': 'slave_bracer_left',  'Armor\\Iron\\M\\Helmet': 'nordic_iron_helm',  'Armor\\ClavicusVile\\Helmet': 'daedric_helm_clavicusvile',  'Armor\\Orcish\\M\\Boots': 'orcish_boots',  'Armor\\Orcish\\M\\Gauntlets': 'orcish_bracer_left',  'Armor\\Orcish\\M\\Cuirass': 'orcish_cuirass',  'Armor\\Orcish\\M\\Greaves': 'orcish_greaves',  'Armor\\Orcish\\M\\Helmet': 'orcish_helm',  'Armor\\Ebony\\Shield': 'trollbone_cuirass',  'Armor\\Leather\\Shield': 'netch_leather_shield',  'Armor\\Daedric\\Shield': 'daedric_towershield',  'Armor\\Madness\\Shield': 'dreugh_shield',  'Armor\\Steel\\Shield': 'blessed_tower_shield',  'Armor\\Blade\\Cuirass': 'silver_dukesguard_cuirass',  'Armor\\Steel\\Boots': 'steel_boots',  'Armor\\Steel\\Cuirass': 'steel_cuirass',  'Armor\\Steel\\Gauntlets': 'steel_gauntlet_left',  'Armor\\Steel\\Greaves': 'steel_greaves',  'Armor\\Steel\\Helmet': 'steel_helm',  'Armor\\LegionDragon\\M\\Boots': 'templar boots',  'Armor\\LegionDragon\\M\\Gauntlets': 'templar bracer left',  'Armor\\LegionDragon\\M\\Cuirass': 'templar_cuirass',  'Armor\\LegionDragon\\M\\Greaves': 'templar_greaves',  'Armor\\LegionDragon\\M\\Helmet': 'templar_helmet_armor',  'Armor\\Mithril\\Shield': 'dragonscale_towershield',  'Armor\\Orcish\\Shield': 'orcish_towershield',  'Armor\\HelmetBloodworm\\Helmet': 'bloodworm_helm_unique',  'Armor\\Fur\\Shield': 'BM wolf shield',  'Clothes\\UpperClass\\04\\M\\pants': 'expensive_skirt_02',  'Clothes\\Ring\\Ring': 'bm_ring_marksman',  'Clothes\\Amulet\\AmuletGold': 'expensive_amulet_02',  'Clothes\\RobeNecromancer\\RobeNecromancer': 'extravagant_robe_01_c',  'Clothes\\MiddleClass\\01\\M\\Shoes': 'common_shoes_07',  'Clothes\\LowerClass\\08\\M\\Shirt08M': 'common_shirt_02_h',  'Clothes\\MiddleClass\\01\\M\\Pants': 'common_pants_01',  'Clothes\\LowerClass\\Jail\\M\\JailShirtHandcuff': 'bm_black_glove_l_s',  'Clothes\\UpperClass\\04\\M\\shirt': 'extravagant_shirt_01_r',  'Clothes\\MiddleClass\\04\\M\\Shoes': 'common_shoes_01',  'Clothes\\LowerClass\\03\\M\\Pants': 'common_pants_01_a',  'Clothes\\LowerClass\\07\\M\\Pants07M': 'expensive_pants_01_a',  'Clothes\\MiddleClass\\02\\M\\Pants': 'common_pants_03',  'Clothes\\LowerClass\\02\\M\\Pants': 'common_pants_04_b',  'Clothes\\MiddleClass\\04\\M\\Pants': 'Caius_pants',  'Clothes\\LowerClass\\05\\M\\Pants': 'common_pants_01_e',  'Clothes\\LowerClass\\04\\M\\Pants': 'common_pants_01_u',  'Clothes\\MiddleClass\\MCPantsHobbitBritch\\M\\Pants': 'common_skirt_02',  'Clothes\\MiddleClass\\MCPantsAdventurer\\M\\Pants': 'common_skirt_05',  'Clothes\\UpperClass\\01\\M\\Pants': 'extravagant_skirt_02',  'Clothes\\UpperClass\\UCCountCountess\\M\\Pant': 'extravagant_pants_01',  'Clothes\\RobeLC01\\RobeLC01': 'expensive_robe_01',  'Clothes\\RobeLC02\\RobeLC02': 'extravagant_robe_01_h',  'Clothes\\RobeUC02\\RobeUC02': 'extravagant_robe_02',  'Clothes\\MythicDawnrobe\\MythicDawnrobe': 'common_robe_02_r',  'Clothes\\RobeUC01\\RobeUC01': 'extravagant_robe_01_r',  'Clothes\\RobeMage\\RobeMage': 'extravagant_robe_01_t',  'Clothes\\RobeLC03\\RobeLC03': 'common_robe_05_a',  'Clothes\\RobeMageArch\\RobeMageArch': 'expensive_robe_02_a',  'Clothes\\Wizard\\Shirt': 'common_robe_EOT',  'Clothes\\UpperClass\\Emperor\\Shirt': "Helseth's Robe",  'Clothes\\UpperClass\\02\\M\\Shirt.NIF': 'expensive_shirt_hair',  'Clothes\\LowerClass\\10\\M\\Shirt10M': 'common_shirt_04_a',  'Clothes\\LowerClass\\03\\M\\Shirt': 'common_shirt_01_e',  'Clothes\\LowerClass\\07\\M\\Shirt07M': 'common_shirt_01_u',  'Clothes\\LowerClass\\13\\M\\Shirt13M': 'common_shirt_01_z',  'Clothes\\LowerClass\\05\\M\\Shirt': 'common_shirt_05',  'Clothes\\MiddleClass\\02\\M\\Shirt': 'expensive_shirt_01_a',  'Clothes\\MiddleClass\\MCShirtForester\\M\\MCShirtForester': 'expensive_shirt_01_u',  'Clothes\\MiddleClass\\05\\M\\Shirt': 'common_shirt_02_r',  'Clothes\\UpperClass\\UCCountCountess\\M\\Shirt': 'common_shirt_03',  'Clothes\\MiddleClass\\MCShirtSneaky\\M\\MCShirtSneaky': 'common_shirt_04_b',  'Clothes\\UpperClass\\05\\M\\shirt': 'exquisite_shirt_01',  'Clothes\\UpperClass\\03\\M\\Shirt': 'extravagant_shirt_01',  'Clothes\\LowerClass\\06\\M\\Shirt06M': 'common_shirt_04',  'Clothes\\UpperClass\\UCShirtHighway\\Shirt': 'caius_shirt',  'Clothes\\MiddleClass\\03\\M\\Shirt': 'common_shirt_02_hh',  'Clothes\\MiddleClass\\04\\M\\Shirt': 'common_shirt_02_rr',  'Clothes\\LowerClass\\15\\M\\Shirt15M': 'common_shirt_02_t',  'Clothes\\UpperClass\\01\\M\\Shirt': 'common_shirt_02_tt',  'Clothes\\UpperClass\\03\\M\\Shoes': 'extravagant_shoes_01',  'Clothes\\LowerClass\\02\\M\\Shoes': 'common_shoes_04',  'Clothes\\MiddleClass\\05\\M\\Shoes': 'common_shoes_05',  'Clothes\\MiddleClass\\02\\M\\Shoes': 'expensive_shoes_01',  'Clothes\\LowerClass\\03\\M\\Shoes': 'expensive_shoes_02',  'Clothes\\UpperClass\\02\\M\\Shoes': 'exquisite_shoes_01',  'Clothes\\UpperClass\\01\\M\\Shoes': 'shoes of st. rilms',  'Weapons\\SilverClaymore': 'spear_mercy_unique',  'Weapons\\SteelBow': 'steel longbow',  'Weapons\\SteelLongsword': 'steel katana',  'Weapons\\SteelClaymore': 'steel dai-katana',  'Weapons\\SteelBattleAxe': 'nordic battle axe',  'Weapons\\SteelWarAxe': 'steel club',  'Weapons\\SteelShortsword': 'steel wakizashi',  'Weapons\\SilverDagger': 'silver spear',  'Weapons\\SilverLongsword': 'dwarven_hammer_volendrung',  'Weapons\\SilverMace': 'BM nordic silver mace',  'Weapons\\SilverWarAxe': 'silver war axe',  'Weapons\\SilverBattleAxe': 'BM nordic silver battleaxe',  'Weapons\\IronMace': 'iron mace',  'Weapons\\SilverShortsword': 'silver shortsword',  'Weapons\\IronWarAxe': 'iron war axe',  'Weapons\\IronArrow': 'iron arrow',  'Weapons\\DaedricArrow': 'daedric arrow',  'Weapons\\EbonyArrow': 'ebony arrow',  'Weapons\\GlassArrow': 'templar arrow',  'Weapons\\SilverArrow': 'silver arrow',  'Weapons\\SteelArrow': 'steel arrow',  'Weapons\\EbonyWarAxe': 'adamantium_axe',  'Weapons\\DaedricDagger': 'daedric tanto',  'Weapons\\EbonyWarhammer': 'ebony staff',  'Weapons\\Chillrend': 'keening',  'Weapons\\SteelDagger': 'steel tanto',  'Weapons\\DAMaceofMolagbal': 'mace of molag bal_unique',  'Weapons\\DaedricBattleAxe': 'daedric battle axe',  'Weapons\\DwarvenMace': 'dwarven mace',  'Weapons\\IronBattleAxe': 'iron halberd',  'Weapons\\EbonyClaymore': 'adamantium_spear',  'Weapons\\EbonyLongsword': 'ebony longsword',  'Weapons\\IronLongsword': 'iron longsword',  'Weapons\\IronDagger': 'iron tanto',  'Weapons\\IronShortsword': 'goblin_sword',  'Weapons\\IronClaymore': 'iron spear',  'Weapons\\Club': 'goblin_club',  'Weapons\\DaedricMace': 'daedric_scourge_unique',  'Weapons\\DwarvenBow': 'dwarven crossbow',  'Weapons\\DaedricLongsword': 'daedric katana',  'Weapons\\DaedricShortsword': 'daedric wakizashi',  'Weapons\\GlassDagger': 'templar dagger',  'Weapons\\SteelWarhammer': 'steel warhammer',  'Weapons\\DwarvenBattleAxe': 'dwarven halberd',  'Weapons\\DwarvenClaymore': 'dwarven claymore',  'Weapons\\DwarvenShortSword': 'dwarven shortsword',  'Weapons\\DwarvenDagger': 'dwarven spear',  'Weapons\\DwarvenWarAxe': 'dwarven war axe',  'Weapons\\DwarvenWarhammer': 'stendar_hammer_unique',  'Weapons\\IronBow': 'short bow',  'Weapons\\EbonyBow': 'longbow_shadows_unique',  'Weapons\\DaedricBow': 'daedric long bow',  'Weapons\\SteelMace': 'steel mace',  'Weapons\\EbonyMace': 'adamantium_mace',  'Weapons\\Cutlass': 'nerevarblade_01_flame',  'Weapons\\EbonyShortsword': 'adamantium_shortsword',  'Weapons\\SilverWarhammer': 'warhammer_crusher_unique',  'Weapons\\DaedricWarhammer': '6th bell hammer',  'Weapons\\DaedricWarAxe': 'daedric war axe',  'Weapons\\IronWarhammer': 'wooden staff',  'Weapons\\ElvenDagger': 'dagger_fang_unique',  'Weapons\\SE45Fork': 'iron fork',  'Weapons\\DAGoldbrand': 'katana_goldbrand_unique',  'Weapons\\UmbraSword': 'longsword_umbra_unique',  'Weapons\\BlackwaterBlade' : 'steel longsword',  'Weapons\\MS29ArgarmirsSword' : 'steel shortsword',  'Weapons\\DaeEbonyBlade' : 'daedric katana',  'Weapons\\RugdumphsSword' : 'dwarven claymore',  'Weapons\\MS13Thornblade' : 'silver longsword',  'Weapons\\DAVolendrung' : 'dwarven_hammer_volendrung',  'Weapons\\MS04Witsplinter' : 'steel tanto',  'Weapons\\adventurerssword' : 'bladepiece_01',  'Weapons\\SE07SylsWarhammer' : 'stendar_hammer_unique',  'Weapons\\ShadowBlade' : 'longsword_umbra_unique',  'Weapons\\ND\\ndsword' : 'BM nordic silver longsword',  'Weapons\\ND\\ndmace' : 'BM nordic silver mace',  'Clutter\\Potions\\IconPotion01': 'potion', 'Clutter\\IconScroll1':'scroll'}

# Backups (items not in dict2) are handled by looking for a keyword of the armor type (such as "Fur", "Steel", "Daedric", etc.) and then
# using an appropriate backup dict. The "None" dict is for items lacking any helpful keyword.
armorBackupDictNone = {
	0:"daedric_god_helm",
	1:"templar_helm",
	2:'daedric_cuirass',
	3:'daedric_greaves',
	4:'daedric_gauntlet_right',
	5:'daedric_boots',
	6:'expensive_ring_02',
	7:'expensive_ring_02',
	8:'expensive_amulet_02',
	9:'daedric longsword',
	10:'daedric dai-katana',
	11: 'daedric longsword',
	12: 'daedric arrow',
	13: 'daedric_towershield',
	14: 'iron_shield',
	15: 'expensive_ring_02',
	16: 'daedric longsword',
	17: 'daedric arrow',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictFur = {
	0:"fur_helm",
	1:"fur_helm",
	2:'fur_cuirass',
	3:'fur_greaves',
	4:'fur_gauntlet_right',
	5:'fur_boots',
	13: 'nordic_leather_shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictIron = {
	0:"iron_helm",
	1:"iron_helm",
	2:'iron_cuirass',
	3:'iron_greaves',
	4:'iron_gauntlet_right',
	5:'iron boots',
	13: 'iron_shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictLeather = {
	0:"netch_leather_helm",
	1:"netch_leather_helm",
	2:'netch_leather_cuirass',
	3:'netch_leather_greaves',
	4:'netch_leather_gauntlet_right',
	5:'netch_leather_boots',
	13: 'netch_leather_shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictSteel = {
	0:"steel_helm",
	1:"steel_helm",
	2:'steel_cuirass',
	3:'steel_greaves',
	4:'steel_gauntlet_right',
	5:'steel_boots',
	13: 'steel_shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictChainmail = {
	0:"imperial_chain_coif_helm",
	1:"imperial_chain_coif_helm",
	2:'imperial_chain_cuirass',
	3:'imperial_chain_greaves',
	4:'indoril_gauntlet_right',
	5:'indoril_boots',
	13: 'dragonscale_shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictDwarven = {
	0:"dwemer_helm",
	1:"dwemer_helm",
	2:'dwemer_cuirass',
	3:'dwemer_greaves',
	4:'dwemer_bracer_right',
	5:'dwemer_boots',
	13: 'dwemer_shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictMithril = {
	0:"silver_helm",
	1:"silver_helm",
	2:'silver_cuirass',
	3:'imperial_greaves',
	4:'imperial right gauntlet',
	5:'imperial boots',
	13: 'steel_towershield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}


armorBackupDictOrcish = {
	0:"orcish_helm",
	1:"orcish_helm",
	2:'orcish_cuirass',
	3:'orcish_greaves',
	4:'orcish_bracer_right',
	5:'orcish_boots',
	13: 'orcish_towershield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictElven = {
	0:"indoril helmet",
	1:"indoril helmet",
	2:'indoril cuirass',
	3:'bonemold_greaves',
	4:'indoril right gauntlet',
	5:'indoril boots',
	13: 'indoril shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictEbony = {
	0:"ebony_closed_helm",
	1:"ebony_closed_helm",
	2:'ebony_cuirass',
	3:'ebony_greaves',
	4:'ebony_bracer_right',
	5:'ebony_boots',
	13: 'ebony_shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictGlass = {
	0:"glass_helm",
	1:"glass_helm",
	2:'glass_cuirass',
	3:'glass_greaves',
	4:'glass_bracer_right',
	5:'glass_boots',
	13: 'glass_shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictDaedric = {
	0:"daedric_god_helm",
	1:"daedric_god_helm",
	2:'daedric_cuirass',
	3:'daedric_greaves',
	4:'daedric_gauntlet_right',
	5:'daedric_boots',
	6:'expensive_ring_02',
	7:'expensive_ring_02',
	8:'expensive_amulet_02',
	9:'daedric longsword',
	10:'daedric dai-katana',
	11: 'daedric longsword',
	12: 'daedric arrow',
	13: 'daedric_towershield',
	14: 'iron_shield',
	15: 'expensive_ring_02',
	16: 'daedric longsword',
	17: 'daedric arrow',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictAmber = {
	0:"dreugh_helm",
	1:"dreugh_helm",
	2:'dreugh_cuirass',
	3:'bonemold_greaves',
	4:'bonemold_bracer_right',
	5:'bonemold_boots',
	13: 'dreugh_shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictMadness = {
	0:"trollbone_helm",
	1:"trollbone_helm",
	2:'trollbone_cuirass',
	3:'ebony_greaves',
	4:'ebony_bracer_right',
	5:'ebony_boots',
	13: 'trollbone_shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictDragon = {
	0:"templar_helmet_armor",
	1:"templar_helmet_armor",
	2:'templar_cuirass',
	3:'templar_greaves',
	4:'templar bracer right',
	5:'templar boots',
	13: 'indoril shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

armorBackupDictCrusader = {
	0:"iron_helmet",
	1:"iron_helmet",
	2:'silver_dukesguard_cuirass',
	3:'imperial_greaves',
	4:'imperial left gauntlet',
	5:'imperial boots',
	13: 'steel_shield',
	15: 'expensive_ring_02',
	18: 'netch_leather_cuirass',
	19: 'netch_leather_cuirass',
	20: 'netch_leather_cuirass',
	21: 'netch_leather_cuirass',
	22: 'netch_leather_cuirass'
}

# The full dict of dicts for armor backups
armorBackupDict2 = {
	"fur": armorBackupDictFur,
	"iron": armorBackupDictIron,
	"leather":armorBackupDictLeather,
	"steel":armorBackupDictSteel,
	"chainmail":armorBackupDictChainmail,
	"dwarven":armorBackupDictDwarven,
	"mithril":armorBackupDictMithril,
	"orcish":armorBackupDictOrcish,
	"elven":armorBackupDictElven,
	"ebony":armorBackupDictEbony,
	"glass":armorBackupDictGlass,
	"daedric":armorBackupDictDaedric,
	"amber":armorBackupDictAmber,
	"madness":armorBackupDictMadness,
	"dragon":armorBackupDictDragon,
	"ndheavy":armorBackupDictCrusader,
	"ndknight":armorBackupDictCrusader,
	"none":armorBackupDictNone
}


# Weapon backups work the same way as armor
weaponBackupDictIron = {
	'dagger':'iron dagger',
	'shortsword':'iron shortsword',
	'longsword':'iron longsword',
	'claymore':'iron claymore',
	'mace':'iron mace',
	'waraxe':'iron war axe',
	'battleaxe':'iron battle axe',
	'hammer':'iron hammer',
	'bow':'long bow'
}

weaponBackupDictSteel = {
	'dagger':'steel dagger',
	'shortsword':'steel shortsword',
	'longsword':'steel longsword',
	'claymore':'steel claymore',
	'mace':'steel mace',
	'waraxe':'steel war axe',
	'battleaxe':'steel battle axe',
	'hammer':'steel hammer',
	'bow':'steel longbow'
}


weaponBackupDictSilver = {
	'dagger':'BM nordic silver dagger',
	'shortsword':'BM nordic silver shortsword',
	'longsword':'BM nordic silver longsword',
	'claymore':'silver claymore',
	'mace':'BM nordic silver mace',
	'waraxe':'BM nordic silver axe',
	'battleaxe':'BM nordic silver battleaxe',
	'hammer':'steel hammer',
	'bow':'steel longbow'
}

weaponBackupDictDwarven = {
	'dagger':'dwarven shortsword',
	'shortsword':'dwarven shortsword',
	'longsword':'dwarven shortsword',
	'claymore':'dwarven claymore',
	'mace':'dwarven mace',
	'waraxe':'dwarven war axe',
	'battleaxe':'dwarven battle axe',
	'hammer':'dwarven hammer',
	'bow':'bonemold long bow'
}


weaponBackupDictElven = {
	'dagger':'dwarven shortsword',
	'shortsword':'dwarven shortsword',
	'longsword':'dwarven shortsword',
	'claymore':'dwarven claymore',
	'mace':'dwarven mace',
	'waraxe':'dwarven war axe',
	'battleaxe':'dwarven battle axe',
	'hammer':'dwarven hammer',
	'bow':'bonemold long bow'
}


weaponBackupDictEbony = {
	'dagger':'ebony shortsword',
	'shortsword':'ebony shortsword',
	'longsword':'ebony longsword',
	'claymore':'silver claymore',
	'mace':'ebony mace',
	'waraxe':'ebony war axe',
	'battleaxe':'orcish battle axe',
	'hammer':'orc hammer',
	'bow':'bonemold long bow'
}

weaponBackupDictGlass = {
	'dagger':'glass dagger',
	'shortsword':'glass dagger',
	'longsword':'glass longsword',
	'claymore':'glass claymore',
	'mace':'ebony mace',
	'waraxe':'glass war axe',
	'battleaxe':'glass staff',
	'hammer':'glass staff',
	'bow':'long bow'
}

weaponBackupDictDaedric = {
	'dagger':'daedric dagger',
	'shortsword':'daedric shortsword',
	'longsword':'daedric longsword',
	'claymore':'daedric claymore',
	'mace':'daedric mace',
	'waraxe':'daedric war axe',
	'battleaxe':'daedric battle axe',
	'hammer':'daedric hammer',
	'bow':'daedric longbow'
}

weaponBackupDictAmber = {
	'dagger':'dwarven shortsword',
	'shortsword':'dwarven shortsword',
	'longsword':'dwarven shortsword',
	'sword':'dwarven shortsword',
	'claymore':'dwarven claymore',
	'mace':'dwarven mace',
	'waraxe':'dwarven war axe',
	'battleaxe':'dwarven battle axe',
	'hammer':'dwarven hammer',
	'bow':'bonemold long bow'
}


weaponBackupDictMadness = {
	'dagger':'ebony shortsword',
	'shortsword':'ebony shortsword',
	'longsword':'ebony longsword',
	'claymore':'silver claymore',
	'mace':'ebony mace',
	'waraxe':'ebony war axe',
	'battleaxe':'orcish battle axe',
	'hammer':'orc hammer',
	'bow':'bonemold long bow'
}

weaponBackupDictNone = {
	'dagger':'BM nordic silver dagger',
	'shortsword':'BM nordic silver shortsword',
	'longsword':'BM nordic silver longsword',
	'claymore':'silver claymore',
	'mace':'BM nordic silver mace',
	'waraxe':'BM nordic silver axe',
	'battleaxe':'BM nordic silver battleaxe',
	'hammer':'steel hammer',
	'bow':'steel longbow'
}

# Dict of dicts for weapon backup
weaponBackupDict2 = {
	"iron": weaponBackupDictIron,
	"steel":weaponBackupDictSteel,
	"silver":weaponBackupDictSilver,
	"dwarven":weaponBackupDictDwarven,
	"elven":weaponBackupDictElven,
	"ebony":weaponBackupDictEbony,
	"templar":weaponBackupDictGlass,
	"daedric":weaponBackupDictDaedric,
	"amber":weaponBackupDictAmber,
	"madness":weaponBackupDictMadness,
	"none":weaponBackupDictNone
}

# Clothing is more straightforward and imo less consequential, so just one dict for backups here
clothingBackupDict = {
	0:'netch_leather_helm',
	1:'netch_leather_helm',
	2:'expensive_shirt_01_a',
	3:'expensive_pants_01_a',
	4:'expensive_glove_right_01',
	5:'expensive_shoes_01',
	6:'expensive_ring_02',
	7:'expensive_ring_02',
	8:'expensive_amulet_02',
	9:'daedric longsword',
	10:'daedric dai-katana',
	11: 'daedric longsword',
	12: 'daedric arrow',
	13: 'daedric_towershield',
	14: 'iron_shield',
	15: 'expensive_ring_02',
	16: 'daedric longsword',
	17: 'daedric arrow',
	18: 'expensive_robe_02_a',
	19: 'expensive_robe_02_a',
	20: 'expensive_robe_02_a',
	21: 'expensive_robe_02_a',
	22: 'expensive_robe_02_a'
}

birthsignDict = {
	"0001FD91":"Apprentice",
	"0001FD92":"Lady",
	"0001FD96":"Lord",
	"0001FD97":"Lover",
	"0001FD93":"Mage",
	"0001FD98":"Ritual",
	"0001FD99":"Serpent",
	"0001FD9A":"Shadow",
	"0001FD9B":"Steed",
	"0001FD94":"Thief",
	"0001FD9C":"Tower",
	"0001FD9D":"Warrior",
	"0001FD95":"Atronach"
}

raceDict = {
	"00023FE9":"Argonian",
	"000224FC":"Breton",
	"000191C1":"Dark Elf",
	"00019204":"High Elf",
	"00000907":"Imperial",
	"000223C7":"Khajiit",
	"000224FD":"Nord",
	"000191C0":"Orc",
	"00000D43":"Redguard",
	"000223C8":"Wood Elf"
}

# Copy the original OB file to Morrowind and begin editing it
shutil.copyfile(OBfull_path, MWfull_path)

new_dict = {

}

with open(OBfull_path) as json_file:

	##### ITEMS

	# For noting if we have to worry about splitting gauntlets
	gotGauntlet = 0

	data1 = json.load(json_file)
	data = data1["Items"]
	lastItem = data["LastItemNumber"]
		##print("Last item #: " + str(lastItem))

	# For noting if we have to worry about splitting items
	hasGauntlets = 0
	hasGloves = 0
	hasBelt = 0

	GauntletRBaseKey = "" 
	GloveRBaseKey = ""
	BeltBaseKey = "" 
	PantsBaseKey = ""

	# Initial check to see if we have to worry about gauntlets, and to get armor / clothing slots
	while(counter1<= lastItem):

		itemIconKeyString = baseString1 + str(counter1) + "icon"
		iconString = data[itemIconKeyString]
		iconString = iconString[:-4].lower()
		itemIDKeyString = baseString1 + str(counter1) + "id"

		TypeVarKeyString = baseString1 + str(counter1) + "typeVar"
		typeVar = data[TypeVarKeyString]
			##print(typeVar)

		# Slots are converted to their MW version after being retrieved from the JSON
		# Remember if we have gauntlets or gloves (these need to split into L and R items in Morrowind)
		if typeVar == 0:
			armorSlotKeyString = baseString1 + str(counter1) + "armorSlot"
			clothingSlotKeyString = baseString1 + str(counter1) + "clothingSlot"
			armorSlot = data[armorSlotKeyString]
			clothingSlot = -1
			if armorSlot == 4:
				GauntletRBaseKey = baseString1 + str(counter1)
				hasGauntlets = 1
				gotGauntlet = 1
		if typeVar == 1:
			armorSlotKeyString = baseString1 + str(counter1) + "armorSlot"
			clothingSlotKeyString = baseString1 + str(counter1) + "clothingSlot"
			clothingSlot = data[clothingSlotKeyString]
			armorSlot = -1
			if clothingSlot == 4:
				GloveRBaseKey = baseString1 + str(counter1)
				hasGloves = 1
		counter1 = counter1 + 1

	counter1 = 0
	while(counter1 <= lastItem):
		# Get icon and id; icon is the easiest and most reliable way to determine base item model
		itemIconKeyString = baseString1 + str(counter1) + "icon"
			##print(data[effectIDString])
		iconString = data[itemIconKeyString]
			##print(iconString)
		iconString = iconString[:-4].lower()
			##print(iconString)
		itemIDKeyString = baseString1 + str(counter1) + "id"

		# Get enchantment type if it exists
		TypeVarKeyString = baseString1 + str(counter1) + "typeVar"
		typeVar = data[TypeVarKeyString]

		foundSub = 0

		# The following is how the backup dicts work -- dict2 being where the icon should ideally be found first
		if iconString not in dict2:
			iconString = iconString.lower()
			##print(iconString)
			if typeVar == 0:
				armorSlotKeyString = baseString1 + str(counter1) + "armorSlot"
				armorSlot = data[armorSlotKeyString]
				# See if the item contains a keyword like "Daedric" or "Glass", etc. If it does use the relevant backup dict, if not use the None backup dict
				for k,v in armorBackupDict2.items():
					if k in iconString:
						newID = v[armorSlot]
						foundSub = 1
				if foundSub == 0:
					newID = armorBackupDictNone[armorSlot]

			# Clothing just gets the one backup dict
			if typeVar == 1:
				clothingSlotKeyString = baseString1 + str(counter1) + "clothingSlot"
				clothingSlot = data[clothingSlotKeyString]
				newID = clothingBackupDict[clothingSlot]

				armorRatingKeyString = baseString1 + str(counter1) + "armorRating"
				data[armorRatingKeyString] = 0
				

			# Weapons work the same as armor for finding the right backup
			if typeVar == 2:
				weaponTypeKeyString = baseString1 + str(counter1) + "weapType"
				weapType = data[weaponTypeKeyString]
				for k,v in weaponBackupDict2.items():
					if k in iconString:
						for kk, vv in weaponBackupDict2[k].items():
							if kk in iconString:
								newID = vv
								foundSub = 1
				if foundSub == 0:
					for kk, vv in weaponBackupDict2[k].items():
						if kk in iconString:
							newID = vv
			if typeVar == 3:
				newID = 'p_burden_q'
			if typeVar == 4:
				newID = 'sc_healing'
		else:
			newID = dict2[iconString].lower()
		data[itemIDKeyString] = newID
		##print(data[itemIDKeyString])

		# ARMOR
		if typeVar == 0:
			# Morrowind uses something called an armor scalar to determine how much each armor piece's rating affects your total rating.
			# Oblivion lacks this, so I create it based on the armor slot and adjust the armor rating accordingly.
			# The priority is making the armor piece equally as protective (total damage reduction) in each game.
			armorRatingKeyString = baseString1 + str(counter1) + "armorRating"
			armorRating = data[armorRatingKeyString]
			scalarDict = {
					0:.1,
					1:.1,
					2:.3,
					3:.1,
					4:.05,
					5:.1,
					6:1,
					7:1,
					8:1,
					9:1,
					10:1,
					11:1,
					12:1,
					13:.1,
					14:1,
					15:1,
					16: 1,
					17: 1,
					18: .4,
					19: .5,
					20: .6,
					21: .5,
					22: .4
			}
			armorSlotKeyString = baseString1 + str(counter1) + "armorSlot"
			armorSlot = data[armorSlotKeyString]

			armorScalar = scalarDict[armorSlot]
			armorRating = armorRating / 100
			armorRating = (armorRating / armorScalar)
			data[armorRatingKeyString] = armorRating

			# Convert armor class. Items cannot be medium armor when coming from Oblivion.
			armorClassKeyString = baseString1 + str(counter1) + "armorClass"
			armorClass = data[armorClassKeyString]
			if armorClass == 1:
				armorClass = 2
				data[armorClassKeyString] = armorClass 

		# WEAPONS
		if typeVar == 2:
			# Determine if the weapon can harm ghosts
			weapNonNormalString = baseString1 + str(counter1) + "weapNonNormal"
			weapNonNormal = data[weapNonNormalString]
			if weapNonNormal == True:
				data[weapNonNormalString] = 1 
			if weapNonNormal == False:
				data[weapNonNormalString] = 0

		# POTIONS
		if typeVar == 3:
			enchTypeKeyString = baseString1 + str(counter1) + "EnchType"
			enchNumKeyString = baseString1 + str(counter1) + "LastEffectNumber"
			counter2 = 0
			if data[enchTypeKeyString] > -1:
				lastEffect = data[enchNumKeyString]
				# Convert enchantment type
					##print("Last effect #: " + str(lastEffect))
				# Walk through the effects ...
				while(counter2 <= lastEffect):
					effectIDString = baseString1 + str(counter1) + baseString2 + str(counter2) + "effect"
						##print(data[effectIDString])
					# Convert the effect to its Morrowind ID; cases like Reflect Damage are handled in the MWSE lua file
					data[effectIDString] = convertDict[data[effectIDString]]
					# If necessary, convert skills to their MW actor values
					if data[effectIDString] == 21 or data[effectIDString] == 83:
							##print(effectIDString)
						effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
							##print(effectAttString)
						data[effectAttString] = skillsOBtoMWDict[data[effectAttString]]
					counter2 = counter2 + 1
						##print(data[effectIDString])
						##print(data)

		# Get enchantment type and effect number JSON keys
		enchTypeKeyString = baseString1 + str(counter1) + "EnchType"
		enchNumKeyString = baseString1 + str(counter1) + "LastEffectNumber"
		counter2 = 0
		if data[enchTypeKeyString] > 0:
			lastEffect = data[enchNumKeyString]
			# Convert enchantment type
			data[enchTypeKeyString] = type_Dict[data[enchTypeKeyString]]
				##print("Last effect #: " + str(lastEffect))
			# Walk through the effects ...
			while(counter2 <= lastEffect):
				effectIDString = baseString1 + str(counter1) + baseString2 + str(counter2) + "effect"
					##print(data[effectIDString])
				# Convert the effect to its Morrowind ID; cases like Reflect Damage are handled in the MWSE lua file
				data[effectIDString] = convertDict[data[effectIDString]]
				# If necessary, convert skills to their MW actor values
				if data[effectIDString] == 21 or data[effectIDString] == 83:
						##print(effectIDString)
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = skillsOBtoMWDict[data[effectAttString]]
				counter2 = counter2 + 1
					##print(data[effectIDString])
					##print(data)
		counter1 = counter1 + 1
	counter1 = 0
	# SPLITTING GAUNTLETS
	if hasGauntlets == 1:
		# Armor Rating
		GauntletRARKey = GauntletRBaseKey + "armorRating"
		GauntletRAR = data[GauntletRARKey]
		data[GauntletRARKey] = GauntletRAR / 2

		# Name, Value, Weight
		GauntletRNameKey = GauntletRBaseKey + "name"
		data[GauntletRNameKey] = "(R) " + data[GauntletRNameKey]

		GauntletRValueKey = GauntletRBaseKey + "value"
		GauntletRValue = data[GauntletRValueKey]
		data[GauntletRValueKey] = GauntletRValue / 2

		GauntletRWeightKey = GauntletRBaseKey + "weight"
		GauntletRWeight = data[GauntletRWeightKey]
		data[GauntletRWeightKey] = GauntletRWeight / 2

		# Enchantments
		GauntletREnchTypeKey = GauntletRBaseKey + "EnchType"
		GauntletRLastEffectKey = GauntletRBaseKey + "LastEffectNumber"

		if data[GauntletREnchTypeKey] > 0:
			#if data[GauntletRLastEffectKey] == -1:
			#	data[GauntletRLastEffectKey] = 3
			counter1 = 0
			# Cut the enchantment in half, such that you need to wear both gauntlets to get the original full effect
			while counter1 <= data[GauntletRLastEffectKey]:
				baseString1 = GauntletRBaseKey + "Effect" + str(counter1)
				baseString2 = baseString1 + "magnitude"
				iterDict = data.copy()
				for k,v in iterDict.items():
					##print(k)
					##print(baseString2)
					if k == baseString2:
						##print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF!")
						data[baseString2] = data[baseString2] / 2
				counter1 = counter1 + 1
	# SPLITTING GLOVES
	# Same as gauntlets, just without armor rating and scalar
	if hasGloves == 1:
		# Name, Value, Weight
		GloveRNameKey = GloveRBaseKey + "name"
		data[GloveRNameKey] = data[GloveRNameKey] + " (R)"

		GloveRValueKey = GloveRBaseKey + "value"
		GloveRValue = data[GloveRValueKey]
		data[GloveRValueKey] = GloveRValue / 2

		GloveRWeightKey = GloveRBaseKey + "weight"
		GloveRWeight = data[GloveRWeightKey]
		data[GloveRWeightKey] = GloveRWeight / 2

		# Enchantments
		GloveREnchTypeKey = GloveRBaseKey + "EnchType"
		GloveRLastEffectKey = GloveRBaseKey + "LastEffectNumber"

		if data[GloveREnchTypeKey] > 0:
			#if data[GloveRLastEffectKey] == -1:
			#	data[GloveRLastEffectKey] = 3
			counter1 = 0
			while counter1 <= data[GloveRLastEffectKey]:
				baseString1 = GloveRBaseKey + "Ench" + str(counter1)
				baseString2 = baseString1 + "magnitude"
				iterDict = data.copy()
				for k,v in iterDict.items():
					if k == baseString2:
						data[baseString2] = data[baseString2] / 2
				counter1 = counter1 + 1

	##### SPELLS

	data = data1["Spells"]

	counter1 = 0
	size = data["TotalSpells"]

	while counter1 < size:
		baseString = "Spell" + str(counter1)
		# Get number of effects (can not exceed 8) and get the converted spell type
		lastEffect = data[baseString + "LastEffectNumber"]
		data[baseString + "Type"] = type_Dict2[data[baseString + "Type"]]
			##print("Last effect #: " + str(lastEffect))
			##print(lastEffect)
		counter = 0
		# For each effect...
		while(counter <= lastEffect):
			baseString2 = baseString + "Effect"
			# Get the effect ID, convert it to its MW version, then assign the key to the converted version
			effectIDString = baseString2 + str(counter) + "effect"
				##print(data[effectIDString])
			##sprint(data[effectIDString])
			data[effectIDString] = convertDict[data[effectIDString]]
			##print(data[effectIDString])

			# Convert skills to Morrowind values
			if data[effectIDString] == 21 or data[effectIDString] == 83:
				effectAttString = baseString2 + str(counter) + "attribute"
				data[effectAttString] = skillsOBtoMWDict[data[effectAttString]]
			counter = counter + 1
		counter1 = counter1 + 1

	#### STATS

	data = data1["Player"]
	#fullIDString = data["Race"]
	#fullIDString = fullIDString[:8]
	#data["Race"] = raceDict[fullIDString]

	fullIDString = data["Birthsign"]
	fullIDString = fullIDString[:8]
	data["Birthsign"] = birthsignDict[fullIDString]

	# SKILL CONVERSION

	data["Longblade"] = data["Blade"]
	data["Shortblade"] = data["Blade"]
	data["Bluntweapon"] = data["Blunt"]
	data["Axe"] = data["Blunt"]
	data["Spear"] = data["Blade"]

	data["Enchant"] = data["Intelligence"]

	data["Mediumarmor"] = max(data["Heavyarmor"], data["Lightarmor"])
	data["Unarmored"] = data["Lightarmor"]


# Remove the old Morrowind file and replace it with the one we just created and modified
os.remove(MWfull_path)
with open(MWfull_path, 'w') as f:
	json.dump(data1, f, indent=4)
f.close()

"""
with open(OBfull_path) as json_file:
	data = json.load(json_file)
	print(data)
"""