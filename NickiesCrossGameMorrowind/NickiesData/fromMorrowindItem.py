import json
import os
import shutil

#Change this to your MWSE filepath, in your Morrowind Data Files directory
MWfilepath = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Morrowind\\Data Files\\MWSE\\'
#Change this to your Oblivion Data directory path
OBfilepath = 'C:\\Games\\Oblivion\\Data\\'
#Don't edit this or anything below
MWfull_path = MWfilepath + 'ItemData.json'
OBfull_path = OBfilepath + 'ItemData.json'

baseString1 = "Item"
baseString2 = "Effect"
counter1 = 0
counter2 = 0

# TODO -- create functions to clean up a lot of the bloat from repeated code

# Dict to convert skill actor values from MW to Oblivion
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

# Spell Effect conversion dict (MW to OB)
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

# Enchantment type conversion (MW to OB)
type_Dict = {
	0:5,
	1:2,
	2:4,
	3:3,
	5:5
}

# A base dict to handle notable armor and weapons.
dict2 = {'a_boots_apostle': '0002319b', 'a_cuirass_dragon': '0002c0fe', 'a_cuirass_ebon': '0002ad85', 'a_cuirass_lords': '00028adf', 'a_cuirass_savior': '00027107', 'a_gauntlet_fists': '0018ae4d', 'a_helm_bearclaw': '000a5659', 'a_nerevar_b_shield': '000897c1', 'a_shield_breaker': '000897c2', 'a_shieled_eleidon': '000229a0', 'ice_boot': '0012dd18', 'ice_greaves': '0012dd18', 'ice_grove': '0012dd1a', 'ice_m_chest': '000091fa', 'ice_m_helmet': '0012dd19', 'ice_pauldron': '000091fa', 'ice_shield': '0012dd1c', 'nord_shield': '00032d49', 'nordicmail_boot': '0001c6d4', 'nordicmail_chest': '0001c6d3', 'nordicmail_greaves': '0001c6d5', 'nordicmail_grove': '0001c6d6', 'nordicmail_helmet': '0001c6d7', 'nordicmail_pauldron': '0001c6d3', 'tx_adamantium_boots': '00038514', 'tx_adamantium_bracer': '00038511', 'tx_adamantium_cuirass': '00038510', 'tx_adamantium_greaves': '00038512', 'tx_adamantium_helm': '00038513', 'tx_adamantium_pauldron': '00038510', 'tx_almindoril_boots': '00014f13', 'tx_almindoril_cuirass': '00014f0d', 'tx_almindoril_gauntlet': '00014f10', 'tx_almindoril_greaves': '0002299d', 'tx_almindoril_helmet': '00014f12', 'tx_almindoril_pauldron': '00014f0d', 'tx_art_wraithguard': '00036346', 'tx_bear2_boot': '00024767', 'tx_bear2_cuirass': '00024766', 'tx_bear2_gauntlet': '00024765', 'tx_bear2_greaves': '00024764', 'tx_bear2_helmet': '00024768', 'tx_bear2_pauldron': '00024766', 'tx_bear_boot': '00024767', 'tx_bear_cuirass': '00024766', 'tx_bear_gauntlet': '00024765', 'tx_bear_greaves': '00024764', 'tx_bear_helmet': '00024768', 'tx_bear_pauldron': '00024766', 'tx_bear_shield': '00024766', 'tx_bonemold_armun_an_helm': '00000c09', 'tx_bonemold_armun_an_pau': '0001c6d1', 'tx_bonemold_boots': '0001c6cf', 'tx_bonemold_bracer': '0002391c', 'tx_bonemold_chuzei_helm': '00000c09', 'tx_bonemold_cuirass': '0001c6d1', 'tx_bonemold_gah_julan_c': '0001c6d1', 'tx_bonemold_gah_julan_h': '00000c09', 'tx_bonemold_gah_julan_pau': '0001c6d1', 'tx_bonemold_greaves': '0001c6d0', 'tx_bonemold_helmet': '00000c09', 'tx_bonemold_pauldron': '0001c6d1', 'tx_bonemold_shield': '000352c1', 'tx_boot_heavy_leather': '0002319b', 'tx_cephalopod_helm': '000a5659', 'tx_chitin_boot': '0002319b', 'tx_chitin_curaiss': '0000c1d6', 'tx_chitin_gauntlet': '00048999', 'tx_chitin_greaves': '00023198', 'tx_chitin_helmet': '0004899b', 'tx_chitin_pauldron': '0000c1d6', 'tx_colovianhelm_w': '0004899b', 'tx_daedric_boots': '00036359', 'tx_daedric_cuirass': '0003635b', 'tx_daedric_fountain_helm': '00026272', 'tx_daedric_gauntlet': '0000c582', 'tx_daedric_god_h': '00026272', 'tx_daedric_greaves': '0003635a', 'tx_daedric_pauldron': '0003635b', 'tx_daedric_terrifying_h': '00026272', 'tx_darkbrotherhood_boot': '0015985b', 'tx_darkbrotherhood_cuir': '0015985c', 'tx_darkbrotherhood_gaunt': '0015985d', 'tx_darkbrotherhood_greav': '00023198', 'tx_darkbrotherhood_helm': '0015985f', 'tx_darkbrotherhood_pauld': '0015985c', 'tx_dragonscale_cuirass': '0002c0fe', 'tx_dragonscale_helm': '0002c104', 'tx_dreugh_cuirass': '0001f444', 'tx_dreugh_helm': '0001f453', 'tx_dustadept_helm': '0015985f', 'tx_dwemer_boots': '00036347', 'tx_dwemer_bracer': '00036346', 'tx_dwemer_cuirass': '00036349', 'tx_dwemer_greaves': '00036348', 'tx_dwemer_helmet': '00036345', 'tx_dwemer_pauldron': '00036349', 'tx_dwemer_shield': '0003634a', 'tx_ebony_boot': '00036353', 'tx_ebony_bracer': '00036352', 'tx_ebony_cuirass': '0002ad85', 'tx_ebony_greaves': '00036354', 'tx_ebony_helmet': '00036351', 'tx_ebony_pauldron': '0002ad85', 'tx_fur_colovian_helm': '00024768', 'tx_fur_cuirass': '00024766', 'tx_glass_boots': '00036341', 'tx_glass_bracer': '00036340', 'tx_glass_cuirass': '00036343', 'tx_glass_greaves': '00036342', 'tx_glass_helmet': '0003633f', 'tx_glass_pauldron': '00036343', 'tx_gondolier_helm': '0015985f', 'tx_helm_silver': '0002c104', 'tx_helsethguard_boots': '0018ae48', 'tx_helsethguard_cuirass': '0018ae4c', 'tx_helsethguard_gauntlet': '0018ae4d', 'tx_helsethguard_greave': '0018ae4e', 'tx_helsethguard_helmet': '0018ae4f', 'tx_helsethguard_pauldron': '0018ae4c', 'tx_icem_shield1': '0012dd1c', 'tx_imperial_boot': '00028ade', 'tx_imperial_curaiss': '00028adf', 'tx_imperial_gauntlet': '00028ae0', 'tx_imperial_greaves': '00028ae1', 'tx_imperial_helmet': '00028ae2', 'tx_imperial_pauldron': '00028adf', 'tx_imperial_shield': '000352d3', 'tx_imperialchain_cuirass': '0001c6d3', 'tx_imperialchain_greaves': '0001c6d5', 'tx_imperialchain_helmet': '0001c6d7', 'tx_imperialchain_pauldron': '0001c6d3', 'tx_indoril_boot': '00014f13', 'tx_indoril_curaiss': '00014f0d', 'tx_indoril_gauntlet': '00014f10', 'tx_indoril_helmet': '00014f12', 'tx_indoril_pauldron': '00014f0d', 'tx_indoril_shield': '000229a0', 'tx_iron_boots': '0001c6cf', 'tx_iron_bracer': '0001c6d2', 'tx_iron_cuirass': '0001c6d1', 'tx_iron_gauntlet': '0001c6d2', 'tx_iron_greaves': '0001c6d0', 'tx_iron_helm_01': '0001c6ce', 'tx_iron_pauldron': '0001c6d1', 'tx_masque_clavicus': '000228ee', 'tx_molecrab_helm': '0015985f', 'tx_moragtong_helm': '0015985f', 'tx_netch_boiled_helm': '0015985f', 'tx_netch_boots': '0015985b', 'tx_netch_cuirass': '0015985c', 'tx_netch_cuirass2': '0015985c', 'tx_netch_gauntlet': '0015985d', 'tx_netch_greaves': '00023198', 'tx_netch_helmet': '0015985f', 'tx_netch_pauldron': '0015985c', 'tx_newtscale_cuirass': '0001c6d3', 'tx_nordicfur_boots': '00024767', 'tx_nordicfur_bracer': '00024765', 'tx_nordicfur_cuirass': '00024766', 'tx_nordicfur_gauntlet': '00024765', 'tx_nordicfur_greaves': '00024764', 'tx_nordicfur_helmet': '00024768', 'tx_nordicfur_pauldron': '00024766', 'tx_nordiciron_cuirass': '000cbd4f', 'tx_nordiciron_helm': '000661c4', 'tx_orcish_boots': '0003634d', 'tx_orcish_bracer': '0003634c', 'tx_orcish_cuirass': '0003634f', 'tx_orcish_greaves': '0003634e', 'tx_orcish_helmet': '0003634b', 'tx_orcish_pauldron': '0003634f', 'tx_redoranmaster_h': '0002c104', 'tx_ringmail_cuirass': '0001c6d3', 'tx_shield_almindoril': '000229a0', 'tx_shield_auriel': '00036356', 'tx_shield_chitin': '00025058', 'tx_shield_daedric': '0003635c', 'tx_shield_dreugh': '0001f458', 'tx_shield_ebony': '00036356', 'tx_shield_glass': '00036344', 'tx_shield_iron': '000352c1', 'tx_shield_nordic_leather': '00047ac8', 'tx_shield_steel': '00023923', 'tx_silver_cuirass': '0002c0fe', 'tx_silver_dukes_cuir': '00023318', 'tx_steel_boot': '000229a5', 'tx_steel_curaiss': '000229a2', 'tx_steel_gauntlet': '0001c6d8', 'tx_steel_greaves': '000229a3', 'tx_steel_helmet': '000229a4', 'tx_steel_pauldron': '000229a2', 'tx_studdedleather_cuirass': '0001c6d3', 'tx_templar_boot': '000add4e', 'tx_templar_bracer': '000add51', 'tx_templar_curaiss': '000add50', 'tx_templar_greaves': '000add52', 'tx_templar_helmet': '000adda2', 'tx_templar_pauldron': '000add50', 'tx_tenpaceboot': '0002319b', 'tx_towershield_bonemold': '000352c1', 'tx_towershield_chitin': '00025058', 'tx_towershield_daedric': '0003635c', 'tx_towershield_dragon': '000352bf', 'tx_towershield_ebony': '00036356', 'tx_towershield_glass': '00036344', 'tx_towershield_hlaalu': '000229a0', 'tx_towershield_iron': '000352c1', 'tx_towershield_netch': '00025058', 'tx_towershield_orcish': '00036350', 'tx_towershield_redoranm': '000229a0', 'tx_towershield_steel': '00023923', 'tx_towershield_telv': '000229a0', 'tx_towershield_trollbone': '00036356', 'tx_trollbone_cuirass': '00036356', 'tx_trollbone_helm': '00014673', 'tx_watchmanshelm': '0015985f', 'tx_wolf2_boot': '00024767', 'tx_wolf2_cuirass': '00024766', 'tx_wolf2_gauntlet': '00024765', 'tx_wolf2_greaves': '00024764', 'tx_wolf2_helmet': '00024768', 'tx_wolf2_pauldron': '00024766', 'tx_wolf_boot': '00024767', 'tx_wolf_cuirass': '00024766', 'tx_wolf_gauntlet': '00024765', 'tx_wolf_greaves': '00024764', 'tx_wolf_helmet': '00024768', 'tx_wolf_pauldron': '00024766', 'tx_wolf_shield': '00025056', 'tx_c_bracercloth': '00024765', 'tx_c_bracerleather01': '0015985d', 'tx_slavebracer': '0001c6d2', 'tx_w_goblin_shield': '000352c1', 'tx_imperial_skirt': '00003a93', 'tx_templar_skirt': '00003a93', 'c_ring_khajiit': '00027110', 'tx_amulet_exquisite1': '00098457', 'tx_belt_common01': '000229ae', 'tx_c_liche_robe': '001885c9', 'tx_c_shoecom01': '000229af', 'tx_common1_cuirass': '0002b90c', 'tx_common1_greaves': '000229ae', 'tx_common1_shoes': '000229af', 'tx_common1_skirt': '000229ae', 'tx_common2_cuirass': '0002b90c', 'tx_common2_greaves': '000229ae', 'tx_common2_shoes': '000229af', 'tx_common2_skirt': '000229ae', 'tx_glove_balmolagmer': '000be335', 'tx_glove_common1': '000be335', 'tx_glove_expensive1': '000be335', 'tx_glove_extravagant_1': '000be335', 'tx_glove_moragtong': '000be335', 'tx_mournhold_cuirass': '00003a94', 'tx_mournhold_greaves': '00003a93', 'tx_mournhold_shoes': '00000bea', 'tx_mournhold_skirt': '00003a93', 'tx_pants_com01': '00000857', 'tx_pants_com03_b': '00028587', 'tx_pants_com04': '0001c830', 'tx_pants_com04_b': '000229ab', 'tx_pants_comm_3': '0001c830', 'tx_pants_comm_3c': '0001047c', 'tx_pants_common_1a': '00000857', 'tx_pants_common_1e': '00027318', 'tx_pants_common_1u': '0001c82c', 'tx_pants_common_1z': '00028587', 'tx_pants_common_5': '000229ae', 'tx_pants_expensive_1': '00064f7c', 'tx_pants_expensive_1a': '00028587', 'tx_pants_expensive_1e': '00064f7c', 'tx_pants_expensive_1u': '00064f7c', 'tx_pants_expensive_1z': '00003a93', 'tx_pants_expensive_2': '00064f7a', 'tx_pants_expensive_3': '00003a93', 'tx_pants_exquisite_1': '000229b1', 'tx_pants_extrav_1': '00064fe4', 'tx_pants_extrav_2': '00064f7c', 'tx_pantscom00': '000229ae', 'tx_ring_expensive02': '00027110', 'tx_robe_com01': '00071019', 'tx_robe_com02': '0007101b', 'tx_robe_com02h': '00071019', 'tx_robe_com02hh': '00071021', 'tx_robe_com02r': '00024de2', 'tx_robe_com02rr': '0007101f', 'tx_robe_com02t': '00064f7f', 'tx_robe_com02tt': '0007101b', 'tx_robe_com03': '00071021', 'tx_robe_com03a': '00071021', 'tx_robe_com03b': '0007101f', 'tx_robe_com04': '0007101b', 'tx_robe_com05': '00071019', 'tx_robe_com05a': '0007101d', 'tx_robe_com05b': '00071019', 'tx_robe_com05c': '0007101b', 'tx_robe_expensive_1': '00071019', 'tx_robe_expensive_2': '00071021', 'tx_robe_expensive_2a': '00064fdf', 'tx_robe_expensive_3': '0007101b', 'tx_robe_exquisite_1': '000a498f', 'tx_robe_extrav_1': '00064f7f', 'tx_robe_extrav_1a': '0007101f', 'tx_robe_extrav_1b': '00071021', 'tx_robe_extrav_1c': '001885c9', 'tx_robe_extrav_1h': '0007101b', 'tx_robe_extrav_1r': '0007101f', 'tx_robe_extrav_1t': '00064f7f', 'tx_robe_extrav_2': '00071021', 'tx_robe_helseth': '00023d33', 'tx_robe_white': '000a498f', 'tx_shirt_aralor': '0001c887', 'tx_shirt_common_1a': '0002ecad', 'tx_shirt_common_1e': '00000883', 'tx_shirt_common_1u': '0002858b', 'tx_shirt_common_1z': '0002c0f6', 'tx_shirt_common_5': '00027319', 'tx_shirt_common_gond': '0002b90c', 'tx_shirt_expensive_1': '0001c831', 'tx_shirt_expensive_1a': '0001c831', 'tx_shirt_expensive_1e': '0002ecad', 'tx_shirt_expensive_1u': '00064f79', 'tx_shirt_expensive_1z': '000352ba', 'tx_shirt_expensive_2': '00064fe5', 'tx_shirt_expensive_3': '00064f7d', 'tx_shirt_exquisite_1': '000a498e', 'tx_shirt_extrav01': '0002319d', 'tx_shirt_extrav02': '00064fe5', 'tx_shirt_extrav_1h': '000352ba', 'tx_shirt_extrav_1r': '00003a94', 'tx_shirt_extrav_1t': '000352ba', 'tx_shirtcom01': '0002ecad', 'tx_shirtcom02': '0002b90c', 'tx_shirtcom04': '00028732', 'tx_shirtcom04_a': '0002ecad', 'tx_shirtcom04_b': '00064f7d', 'tx_shirtcom04_c': '00064fe6', 'tx_shirtcomm_03': '00064fe5', 'tx_shirtcomm_03_b': '000352ba', 'tx_shirtcomm_2h': '0002b90c', 'tx_shirtcomm_2hh': '0001c884', 'tx_shirtcomm_2r': '000352ba', 'tx_shirtcomm_2rr': '00000b86', 'tx_shirtcomm_2t': '0002c0fa', 'tx_shirtcomm_2tt': '000229b0', 'tx_shirtcomm_3_c': '00064fe6', 'tx_shoecom01': '00000bea', 'tx_shoes_common_3': '0002319e', 'tx_shoes_common_4': '000229ac', 'tx_shoes_common_5': '000352bb', 'tx_shoes_expensive_1': '0001c883', 'tx_shoes_expensive_2': '0001c82b', 'tx_shoes_expensive_3': '0002319e', 'tx_shoes_exquisite_1': '0001c888', 'tx_shoes_extrav_1': '0002319e', 'tx_shoes_extrav_2': '000229b2', 'tx_shoes_rilms': '000229b2', 'tx_skirt_com01': '00064f7c', 'tx_skirt_com04_c': '00064f7c', 'tx_skirt_common_2': '00064f7c', 'tx_skirt_common_3': '00064f7a', 'tx_skirt_common_5': '00064f7a', 'tx_skirt_expensive_1': '000229b1', 'tx_skirt_expensive_2': '00003a93', 'tx_skirt_expensive_3': '000229b1', 'tx_skirt_exquisite_1': '000229b1', 'tx_skirt_extravagant_1': '000229b1', 'tx_skirt_extravagant_2': '000229b1', 'hircine_spear': '00025226', 'huntsman_crossbow': '000229b7', 'huntsman_longsword': '0003a85a', 'huntsman_spear': '0003a858', 'huntsman_waraxe': '000229b6', 'huntsman_waraxem': '000229bd', 'icem_spear': '000229b8', 'icem_sword': '000229bc', 'ice_dagger': '00025224', 'ice_longsword': '0002521f', 'ice_mace': '00025223', 'ice_waraxe': '00025222', 'nord_battleaxe': '00025221', 'nord_claymore': '00025226', 'nord_dagger': '00025224', 'nord_leg': '00000d82', 'nord_longsword': '0002521f', 'nord_mace': '00025223', 'nord_shortsword': '00025220', 'nord_waraxe': '00025222', 'pickaxe': '00000d81', 'tx_arrow_bonemold': '00017829', 'tx_arrow_chitin': '00017829', 'tx_arrow_corkbulb': '00017829', 'tx_arrow_daedric': '0001efd3', 'tx_arrow_ebony': '0001efd5', 'tx_arrow_glass': '00022be1', 'tx_arrow_iron': '00017829', 'tx_arrow_silver': '0001efd4', 'tx_arrow_steel': '000229c1', 'tx_art_cleaverstfelms': '00035e6c', 'tx_art_crescent': '00035e78', 'tx_art_crosierstllothis': '00035e69', 'tx_art_keening': '00068c01', 'tx_art_mehrunesrazor': '0003a859', 'tx_art_molagbal_mace': '00027117', 'tx_art_queenofbats': '00035e77', 'tx_art_sunder': '00035dd2', 'tx_art_volendrung': '00027108', 'tx_battleaxe_daedric': '00035e77', 'tx_battleaxe_iron': '00000d7f', 'tx_battle_axe': '000229bd', 'tx_bipolar_blade': '00035e68', 'tx_broadsword_ebony': '00035e6e', 'tx_broadsword_imperial': '000229ba', 'tx_broadsword_iron': '00000c0c', 'tx_broadsword_leafbladed': '000229ba', 'tx_broadsword_nordic': '0003a85a', 'tx_chitin_club': '00000d81', 'tx_chitin_dagger': '00019171', 'tx_chitin_shortsword': '00000c0d', 'tx_chitin_spear': '00019171', 'tx_chitin_waraxe': '00000d81', 'tx_claymore': '000229b8', 'tx_claymore_iron': '0001c6cd', 'tx_claymore_nordic': '0003a858', 'tx_claymore_silver': '00025226', 'tx_club01': '0003b375', 'tx_club_daedric': '00035e75', 'tx_club_iron': '00000d81', 'tx_crossbow_steell': '000229b7', 'tx_crossbow_dwemer': '00035dce', 'tx_crystal_claymore': '00035e61', 'tx_crystal_longsword': '00035e5f', 'tx_daedric_claymore': '00035e78', 'tx_daedric_longsword': '00035e76', 'tx_daedric_shortsword': '00035e73', 'tx_dagger_daedric': '00035e72', 'tx_dagger_dragon': '000229b9', 'tx_dagger_glass': '00035e5b', 'tx_dagger_iron': '00019171', 'tx_dai-katana_daedric': '00035e78', 'tx_daikatana': '0009dac5', 'tx_dreugh_club': '0003b375', 'tx_dreugh_staff': '000229be', 'tx_dwemer_battleaxe': '00035dcd', 'tx_dwemer_claymore': '00035dcf', 'tx_dwemer_halberd': '00035dcd', 'tx_dwemer_mace': '00035dd2', 'tx_dwemer_shortsword': '00035dd3', 'tx_dwemer_spear': '00035dd0', 'tx_dwemer_waraxe': '00035dd4', 'tx_dwemer_warhammer': '00035dd5', 'tx_ebony_scimitar': '00035e6e', 'tx_halberd_glass': '00035e61', 'tx_halberd_iron': '00000d7f', 'tx_halberd_steel': '000229b6', 'tx_iron_claymore': '0001c6cd', 'tx_iron_longsword': '00000c0c', 'tx_iron_shortsword': '00000c0d', 'tx_katana': '00024dca', 'tx_katana_daedric': '00035e76', 'tx_longbow': '00025231', 'tx_longbow_ariel': '00035e7b', 'tx_longbow_bonemold': '00025231', 'tx_longbow_daedric': '0002627d', 'tx_longbow_steel': '000229b7', 'tx_longspear_ebony': '00035e70', 'tx_longsword_ebony': '00035e6e', 'tx_longsword_iron': '00000c0c', 'tx_mace01': '000229bb', 'tx_maceofslurring': '00035e6d', 'tx_mace_daedric': '00035e75', 'tx_mace_ebony': '00035e6d', 'tx_mace_iron': '00000d82', 'tx_miner_pick': '00000d81', 'tx_nordic_battleaxe': '00025221', 'tx_orcish_waraxe': '00035e6c', 'tx_orcish_warhammer': '00035e71', 'tx_saber': '0003aa82', 'tx_saber_iron': '0003aa82', 'tx_shortbow_chitin': '00025231', 'tx_shortbow_steel': '00025231', 'tx_shortsword01': '000229bc', 'tx_shortsword_ebony': '00035e6b', 'tx_shortsword_imperial': '0003a859', 'tx_shortsword_iron': '00000c0d', 'tx_shortsword_silver': '00025220', 'tx_silver_dagger': '00025224', 'tx_silver_longsword': '0002521f', 'tx_silver_spear': '00025224', 'tx_silver_staff': '00025225', 'tx_silver_waraxe': '00025222', 'tx_spear01': '000229b9', 'tx_spear_daedric': '00035e78', 'tx_spear_iron': '0001c6cd', 'tx_spikedclub': '000229bd', 'tx_staff01': '000229be', 'tx_staff_daedric': '00035e79', 'tx_staff_ebony': '00035e71', 'tx_staff_glass': '00035e62', 'tx_steel_battleaxe': '000229b6', 'tx_tanto': '000229b9', 'tx_tanto_daedric': '00035e72', 'tx_tanto_iron': '00019171', 'tx_wakazashi': '000229bc', 'tx_wakazashi_daedric': '00035e73', 'tx_wakazashi_iron': '00000c0d', 'tx_waraxe_daedric': '00035e74', 'tx_waraxe_ebony': '00035e6c', 'tx_waraxe_glass': '00035e5d', 'tx_waraxe_iron': '00000d81', 'tx_waraxe_nordic': '0003a856', 'tx_warhammer': '000229be', 'tx_warhammer_daedric': '00035e79', 'tx_warhammer_iron': '00019172', 'tx_wooden_staff': '00019172', 'tx_w_adtium_axe': '00035e6c', 'tx_w_adtium_claymore': '00035e70', 'tx_w_adtium_mace': '00035e6d', 'tx_w_adtium_shortsword': '00035e6b', 'tx_w_adtium_spear': '00035e70', 'tx_w_almalexia_scimitar': '0003aa82', 'tx_w_goblin_club': '0003b375', 'tx_w_goblin_sword': '00000c0d', 'tx_w_nerevarblade': '0003aa82', 'tx_w_nerevarblademiddle': '0003aa82', 'tx_w_stendarshammer': '00035dd5', 'w_6th_hammer': '00035e79', 'w_claymore_chrys': '00025226', 'w_claymore_iceblade': '00035e68', 'w_dagger_fang': '00035e6a', 'w_de_fork': '0007877f', 'w_katana_goldbrand': '00027105', 'w_longbow_shadows': '00035e7b', 'w_longsword_umbra': '00026b22', 'w_mace_scourge': '00035e75', 'w_nerevar_blade_fire': '0003aa82', 'w_spear_mercy': '00025226', 'w_staff_hasedoki': '00025225', 'w_staff_magnus': '00025225', 'w_warhammer_crusher': '00025225', 'tx_potion_bargain_01': '000920e', 'tx_scroll_open_01': '0008729e'}

# These backup dicts handle any items not found in dict2, using a rough approximation
armorBackupDict = {
	0:'tx_daedric_terrifying_h',
	1:'tx_daedric_cuirass',
	2:'tx_daedric_cuirass',
	3:'tx_daedric_cuirass',
	4:'tx_daedric_greaves',
	5:'tx_daedric_boots',
	6:'tx_daedric_gauntlet',
	7:'tx_daedric_gauntlet',
	8:'tx_shield_daedric',
	9:'tx_ebony_bracer',
	10:'tx_ebony_bracer'
}

clothingBackupDict = {
	0:'tx_pants_expensive_1',
	1:'tx_shoes_expensive_1',
	2:'tx_shirt_expensive_1',
	3:'tx_belt_common01',
	4:'tx_robe_expensive_1',
	5:'tx_glove_common1',
	6:'tx_glove_common1',
	7:'tx_skirt_expensive_1',
	8:'tx_ring_expensive02',
	9:'tx_amulet_exquisite1'
}

weaponBackupDict = {
	0:'tx_dagger_daedric',
	1:'tx_daedric_longsword',
	2:'tx_daedric_claymore',
	3:'tx_mace_daedric',
	4:'tx_warhammer_daedric',
	5:'tx_warhammer_daedric',
	6:'tx_daedric_claymore',
	7:'tx_waraxe_daedric',
	8:'tx_battleaxe_daedric',
	9:'tx_longbow_daedric',
	10:'tx_crossbow_dwemer',
	11:'tx_arrow_daedric',
	12:'tx_arrow_daedric'
}

# Make a copy of the current Morrowind version of the JSON
shutil.copyfile(MWfull_path, OBfull_path)

new_dict = {
	"Items":{},
	"Reset":{}
}

# Now edit the copy
with open(OBfull_path) as json_file:

	# These fields will tell us if we have to worry about problematic item pieces, which are configured differently in Oblivion vs. Morrowind
	gotPauldron = 0
	gotPauldronL = 0
	gotPauldronR = 0
	gotCuirass = 0

	gotGauntlet = 0
	gotGauntletR = 0
	gotBelt = 0

	gotBelt = 0
	gotPants = 0

	data = json.load(json_file)
		##print(data)
	lastItem = data["LastItemNumber"]
	print("Last item #: " + str(lastItem))

	# I also included data on if we have problematic items in the JSON itself
	hasGauntlets = data["HasGauntlets"]
	hasPauldrons = data["HasPauldrons"]
	hasBelt = data["HasBelt"]

	# Fields to make sure we have every piece needed in converting from MW to OB (for example, if we have only a left gauntlet and not a right). In theory the MW item chest should have
	# prevented this from being a problem in the first place.
	GauntletR = 0 
	Belt = 0 
	PauldronR = 0 
	PauldronL = 0 
	comCuirass = 0 
	comPants = 0

	# Fields to remember the JSON key needed to access these item values
	GauntletRBaseKey = "" 
	BeltBaseKey = "" 
	PauldronRBaseKey = "" 
	PauldronLBaseKey = "" 
	comCuirassBaseKey = "" 
	PantsBaseKey = ""

	# For each item, check if there is a problematic item (no direct conversion, e.g. gauntlets)
	while(counter1<= lastItem):

		# "KeyString" refers to the JSON key. I have to construct the string this way due to how I've stored the item data in the JSON: "Item0..." wherein Item0 is the KeyString

		# Get the icon and the ID. Due to item variants existing, icons are the easiest and most reliable way to determine a base item model.
		itemIconKeyString = baseString1 + str(counter1) + "icon"
		iconString = data[itemIconKeyString]
		iconString = iconString[2:-4].lower()

		# Not sure if we even need the item id but it's here just in case
		itemIDKeyString = baseString1 + str(counter1) + "id"

		# Get the Item type (armor, weapon, etc.)
		TypeVarKeyString = baseString1 + str(counter1) + "typeVar"
		typeVar = data[TypeVarKeyString]
			##print(typeVar)

		# PRELIMINARY ARMOR CHECK
		if typeVar == 0:
			# Get the armor slot JSON key
			armorSlotKeyString = baseString1 + str(counter1) + "armorSlot"
			
			# Convert the armor slots from their Morrowind data values to Oblivion data values
			if data[armorSlotKeyString] == 9:
				data[armorSlotKeyString] = 6
			if data[armorSlotKeyString] == 10:
				data[armorSlotKeyString] = 7

			# Assign the armor slot back into the JSON
			armorSlot = data[armorSlotKeyString]
				##print(armorSlot)
			# Now get the Oblivion base model of the item from the relevant dict
			iconString = armorBackupDict[armorSlot]

			# Note if the item is problematic (no direct conversion)
			if armorSlot == 1:
				comCuirassBaseKey = baseString1 + str(counter1)
			if armorSlot == 2:
				PauldronLBaseKey = baseString1 + str(counter1)
					##print(PauldronLBaseKey)
			if armorSlot == 3:
				PauldronRBaseKey = baseString1 + str(counter1)
			if armorSlot == 6 or armorSlot == 9:
				GauntletLBaseKey = baseString1 + str(counter1)
			if armorSlot == 7 or armorSlot == 10:
				GauntletRBaseKey = baseString1 + str(counter1)

			if data[armorSlotKeyString] == 2:
				data[armorSlotKeyString] = 9
			if data[armorSlotKeyString] == 3:
				data[armorSlotKeyString] = 9
			if data[armorSlotKeyString] == 6:
				data[armorSlotKeyString] = 9

		# PRELIMINARY CLOTHING CHECK
		if typeVar == 1:
			clothingSlotKeyString = baseString1 + str(counter1) + "clothingSlot"
				##print("Found Clothing!")

			# Get the slot and assign the new base model
			clothingSlot = data[clothingSlotKeyString]
			iconString = clothingBackupDict[clothingSlot]

			# Note problematic items
			if clothingSlot == 3:
					##print("Found Belt!")
				BeltBaseKey = baseString1 + str(counter1)
				data[clothingSlotKeyString] = 9
			if clothingSlot == 0 or clothingSlot == 7:
					##print("Found pants!")
				PantsBaseKey = baseString1 + str(counter1)
		counter1 = counter1 + 1

	counter1 = 0

	# Now convert each item
	while(counter1 <= lastItem):
		# Same initial steps as before
		itemIconKeyString = baseString1 + str(counter1) + "icon"
			##print(data[effectIDString])
		iconString = data[itemIconKeyString]
		print(iconString)
		iconString = iconString[2:-4].lower()
		print(iconString)
		itemIDKeyString = baseString1 + str(counter1) + "id"

		TypeVarKeyString = baseString1 + str(counter1) + "typeVar"
		typeVar = data[TypeVarKeyString]

		# If the item (determined by its icon) isn't in the more specific dict, use the backups. Then, get the relevant slot.
		if iconString not in dict2:
			if typeVar == 0:
				armorSlotKeyString = baseString1 + str(counter1) + "armorSlot"
				armorSlot = data[armorSlotKeyString]
				iconString = armorBackupDict[armorSlot]
			if typeVar == 1:
				clothingSlotKeyString = baseString1 + str(counter1) + "clothingSlot"
				clothingSlot = data[clothingSlotKeyString]
				iconString = clothingBackupDict[clothingSlot]
			if typeVar == 2:
				weaponTypeKeyString = baseString1 + str(counter1) + "weapType"
				weapType = data[weaponTypeKeyString]
				iconString = weaponBackupDict[weapType]
			if typeVar == 3:
				iconString = "tx_potion_bargain_01"
			if typeVar == 4:
				iconString = "tx_scroll_open_01"

		# Get the Oblivionized item ID, written to work with Punchinello
		newID = dict2[iconString].upper() + ":Oblivion.esm"
		data[itemIDKeyString] = newID
			##print(data[itemIDKeyString])

		# ARMOR
		if typeVar == 0:
			armorRatingKeyString = baseString1 + str(counter1) + "armorRating"
			armorScalarKeyString = baseString1 + str(counter1) + "armorScalar"
			armorRating = data[armorRatingKeyString]
			armorScalar = data[armorScalarKeyString]

			# Oblivionize the armor rating (prioritizing the same amount of damage reduction outcome)
			armorRating = (armorRating * 100 * armorScalar)
			data[armorRatingKeyString] = armorRating

			# Get the correct armor class (Light v. Heavy; Medium is is converted to Light)
			armorClassKeyString = baseString1 + str(counter1) + "armorClass"
			armorClass = data[armorClassKeyString]
			if armorClass == 2:
				armorClass = 1
				data[armorClassKeyString] = armorClass 

		# WEAPON
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

			lastEffect = data[enchNumKeyString]
			# Walk through the effects ...
			while(counter2 <= lastEffect):
				effectIDString = baseString1 + str(counter1) + baseString2 + str(counter2) + "effect"
				##print(data[effectIDString])
			
				# Convert the effect to Oblivion's effect id
				data[effectIDString] = convertDict[data[effectIDString]]
					##print(data[effectIDString])
					##print(data)

				# Turn invalid effects into a dummy effect to avoid errors
				
				if data[effectIDString] == 'NONE':
					data[effectIDString] = 'FOAT'
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
					data[effectAttString] = 7
					effectMagString = baseString1 + str(counter1) + baseString2 + str(counter2) + "magnitude"
					data[effectMagString] = 0
					effectDurString = baseString1 + str(counter1) + baseString2 + str(counter2) + "duration"
					data[effectDurString] = 0

				# Convert skills if necessary
				elif data[effectIDString] == 'FOSK' or data[effectIDString] == 'DRSK':
						##print(effectIDString)
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = skillsMWtoOBAVDict[data[effectAttString]]
				elif data[effectIDString] == 'SWSW':
					data[effectIDString] = 'FOSK'
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = 13
				elif data[effectIDString] == 'LEVI':
					data[effectIDString] = 'FOSK'
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = 26
				elif data[effectIDString] == 'JUMP':
					data[effectIDString] = 'FOSK'
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = 26
					effectMagString = baseString1 + str(counter1) + baseString2 + str(counter2) + "magnitude"
						##print(effectAttString)
					data[effectMagString] = data[effectMagString] * 3
				elif data[effectIDString] == 'BLIN':
					data[effectIDString] = 'DRAT'
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = 3
				elif data[effectIDString] == 'FATT':
					data[effectIDString] = 'FOAT'
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = 3


				counter2 = counter2 + 1

		# ENCHANTMENTS

		# Find the type and number of effects
		enchTypeKeyString = baseString1 + str(counter1) + "EnchType"
		enchNumKeyString = baseString1 + str(counter1) + "LastEffectNumber"
		counter2 = 0
		# If the item is enchanted...
		if data[enchTypeKeyString] > 0:
			lastEffect = data[enchNumKeyString]
			data[enchTypeKeyString] = type_Dict[data[enchTypeKeyString]]
				##print("Last effect #: " + str(lastEffect))
			while(counter2 <= lastEffect):
				effectIDString = baseString1 + str(counter1) + baseString2 + str(counter2) + "effect"
					##print(data[effectIDString])
				
				# Convert the effect to Oblivion's effect id
				data[effectIDString] = convertDict[data[effectIDString]]
					##print(data[effectIDString])
					##print(data)

				# Turn invalid effects into a dummy effect to avoid errors
				if data[effectIDString] == 'NONE':
					data[effectIDString] = 'FOAT'
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
					data[effectAttString] = 7
					effectMagString = baseString1 + str(counter1) + baseString2 + str(counter2) + "magnitude"
					data[effectMagString] = 0
					effectDurString = baseString1 + str(counter1) + baseString2 + str(counter2) + "duration"
					data[effectDurString] = 0
				# Convert skills if necessary
				elif data[effectIDString] == 'FOSK' or data[effectIDString] == 'DRSK':
						##print(effectIDString)
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = skillsMWtoOBAVDict[data[effectAttString]]
				elif data[effectIDString] == 'SWSW':
					data[effectIDString] = 'FOSK'
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = 13
				elif data[effectIDString] == 'LEVI':
					data[effectIDString] = 'FOSK'
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = 26
				elif data[effectIDString] == 'JUMP':
					data[effectIDString] = 'FOSK'
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = 26
					effectMagString = baseString1 + str(counter1) + baseString2 + str(counter2) + "magnitude"
						##print(effectAttString)
					data[effectMagString] = data[effectMagString] * 3
				elif data[effectIDString] == 'BLIN':
					data[effectIDString] = 'DRAT'
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = 3
				elif data[effectIDString] == 'FATT':
					data[effectIDString] = 'FOAT'
					effectAttString = baseString1 + str(counter1) + baseString2 + str(counter2) + "attribute"
						##print(effectAttString)
					data[effectAttString] = 3

				counter2 = counter2 + 1
		counter1 = counter1 + 1
	counter1 = 0

	# HANDLING PAULDRONS
	if hasPauldrons == 1:
		# Pauldron traits and enchantments are added to a Cuirass if possible

		# Armor Rating
		PauldronLARKey = PauldronLBaseKey + "armorRating"           
		PauldronLAR = data[PauldronLARKey]
		PauldronRARKey = PauldronRBaseKey + "armorRating"
		PauldronRAR = data[PauldronRARKey]
		comCuirassARKey = comCuirassBaseKey + "armorRating"
		comCuirassAR = data[comCuirassARKey]
		data[comCuirassARKey] = comCuirassAR + PauldronRAR + PauldronLAR

		# Name, Value, Weight
		comCuirassNameKey = comCuirassBaseKey + "name"
		data[comCuirassNameKey] = data[comCuirassNameKey] + " w/ pauldrons"

		PauldronLValueKey = PauldronLBaseKey + "value"          
		PauldronLValue = data[PauldronLValueKey]
		PauldronRValueKey = PauldronRBaseKey + "value"
		PauldronRValue = data[PauldronRValueKey]
		comCuirassValueKey = comCuirassBaseKey + "value"
		comCuirassValue = data[comCuirassValueKey]
		data[comCuirassValueKey] = comCuirassValue + PauldronRValue + PauldronLValue

		PauldronLWeightKey = PauldronLBaseKey + "weight"            
		PauldronLWeight = data[PauldronLWeightKey]
		PauldronRWeightKey = PauldronRBaseKey + "weight"
		PauldronRWeight = data[PauldronRWeightKey]
		comCuirassWeightKey = comCuirassBaseKey + "weight"
		comCuirassWeight = data[comCuirassWeightKey]
		data[comCuirassWeightKey] = comCuirassWeight + PauldronRWeight + PauldronLWeight

		# Enchantments
		PauldronLEnchTypeKey = PauldronLBaseKey + "EnchType"
		PauldronREnchTypeKey = PauldronRBaseKey + "EnchType"
		PauldronLLastEffectKey = PauldronLBaseKey + "LastEffectNumber"
		PauldronRLastEffectKey = PauldronRBaseKey + "LastEffectNumber"
		comCuirassLastEffectKey = comCuirassBaseKey + "LastEffectNumber"

		# Enchantments
		if data[PauldronLEnchTypeKey] != -1:
			if data[comCuirassLastEffectKey] == -1:
				data[comCuirassLastEffectKey] = 3
			counter1 = 0
			while counter1 <= data[PauldronLLastEffectKey]:
				baseString1 = PauldronLBaseKey + "Ench" + str(counter1)
				baseString2 = comCuirassBaseKey + "Ench" + str(data[comCuirassLastEffectKey] + 1)

				# Combine the enchantments; copy is needed to modify the enchantment during iteration
				iterDict = data.copy()
				for k,v in iterDict.items():
					if k.startswith(baseString1):
						newString1 = k.replace(baseString1, '')
						newString2 = baseString2 + newString1
							##print(newString2)
							##print(v)
						data[newString2] = v
				data[comCuirassLastEffectKey] = data[comCuirassLastEffectKey] + 1
				counter1 = counter1 + 1
		if data[PauldronREnchTypeKey] != -1:
			# Same as above but for right pauldrons
			if data[comCuirassLastEffectKey] == -1:
				data[comCuirassLastEffectKey] = 3
			counter1 = 0
			while counter1 <= data[PauldronRLastEffectKey]:
				baseString1 = PauldronRBaseKey + "Ench" + str(counter1)
				baseString2 = comCuirassBaseKey + "Ench" + str(data[comCuirassLastEffectKey] + 1)
				iterDict = data.copy()
				for k,v in iterDict.items():
					if k.startswith(baseString1):
						newString1 = k.replace(baseString1, '')
						newString2 = baseString2 + newString1
				data[comCuirassLastEffectKey] = data[comCuirassLastEffectKey] + 1
				counter1 = counter1 + 1
		"""
		# Delete Pauldrons
		for k,v in iterDict.items():
			if k.startswith(PauldronRBaseKey):
				del data[k]
			if k.startswith(PauldronLBaseKey):
				del data[k]
		data["LastItemNumber"] = data["LastItemNumber"] - 2
		"""
	if hasGauntlets == 1:
		print("Had gauntlets!")
		# Armor Rating
		GauntletLARKey = GauntletLBaseKey + "armorRating"           
		GauntletLAR = data[GauntletLARKey]
		GauntletRARKey = GauntletRBaseKey + "armorRating"
		GauntletRAR = data[GauntletRARKey]
		data[GauntletRARKey] = GauntletRAR + GauntletLAR

		# Name, Value, Weight
		GauntletRNameKey = GauntletRBaseKey + "name"
		GauntletLNameKey = GauntletLBaseKey + "name"
		data[GauntletRNameKey] = data[GauntletRNameKey] + "/" + data[GauntletLNameKey]

		GauntletLValueKey = GauntletLBaseKey + "value"          
		GauntletLValue = data[GauntletLValueKey]
		GauntletRValueKey = GauntletRBaseKey + "value"
		GauntletRValue = data[GauntletRValueKey]
		data[GauntletRValueKey] = GauntletRValue + GauntletLValue

		GauntletLWeightKey = GauntletLBaseKey + "weight"            
		GauntletLWeight = data[GauntletLWeightKey]
		GauntletRWeightKey = GauntletRBaseKey + "weight"
		GauntletRWeight = data[GauntletRWeightKey]
		data[GauntletRWeightKey] = GauntletRWeight + GauntletLWeight

		# Enchantments
		GauntletLEnchTypeKey = GauntletLBaseKey + "EnchType"
		GauntletREnchTypeKey = GauntletRBaseKey + "EnchType"
		GauntletLLastEffectKey = GauntletLBaseKey + "LastEffectNumber"
		GauntletRLastEffectKey = GauntletRBaseKey + "LastEffectNumber"

		if data[GauntletLEnchTypeKey] != -1:
			# Same process as pauldrons
			if data[GauntletRLastEffectKey] == -1:
				data[GauntletRLastEffectKey] = 3
			counter1 = 0
			effectBank = []
			doneBank = []
			while counter1 <= data[GauntletLLastEffectKey]:
				baseString1 = GauntletLBaseKey + "Effect" + str(counter1)
				baseString1R = GauntletRBaseKey + "Effect" + str(counter1)

				baseString1id = baseString1 + "effect"
				baseString1Rid = baseString1R + "effect"

				baseString2 = GauntletRBaseKey + "Effect" + str(data[GauntletRLastEffectKey] + 1)
				iterDict = data.copy()
				iterDict2 = data.copy()

				# Add new effects
				for k,v in iterDict.items():
					if k.startswith(baseString1):
						newString1 = k.replace(baseString1, '')
						newString2 = baseString2 + newString1
						print(newString2)
						print(v)
						data[newString2] = v

				# Combine duplicate effect magnitudes
				
				for k,v in iterDict2.items():
					if k.startswith(baseString1R):
						if data[baseString1Rid] in effectBank and data[baseString1Rid] not in doneBank:
							GauntletRMagnitudeKey = baseString1R + "magnitude"
							print(data[GauntletRMagnitudeKey])
							data[GauntletRMagnitudeKey] = data[GauntletRMagnitudeKey] * 2
							print(data[GauntletRMagnitudeKey])
							doneBank.append(data[baseString1Rid])
						else:
							effectBank.append(data[baseString1Rid])
				print(effectBank)
				print(doneBank)

				data[GauntletRLastEffectKey] = data[GauntletRLastEffectKey] + 1
				counter1 = counter1 + 1

	if hasBelt == 1:
		# Name, Value, Weight
		PantsNameKey = PantsBaseKey + "name"
		BeltNameKey = BeltBaseKey + "name"
		data[PantsNameKey] = data[PantsNameKey] + " w/ Belt"

		BeltValueKey = BeltBaseKey + "value"            
		BeltValue = data[BeltValueKey]
		PantsValueKey = PantsBaseKey + "value"
		PantsValue = data[PantsValueKey]
		data[PantsValueKey] = PantsValue + BeltValue

		BeltWeightKey = BeltBaseKey + "weight"          
		BeltWeight = data[BeltWeightKey]
		PantsWeightKey = PantsBaseKey + "weight"
		PantsWeight = data[PantsWeightKey]
		data[PantsWeightKey] = PantsWeight + BeltWeight

		# Enchantments
		BeltEnchTypeKey = BeltBaseKey + "EnchType"
		PantsEnchTypeKey = PantsBaseKey + "EnchType"
		BeltLastEffectKey = BeltBaseKey + "LastEffectNumber"
		PantsLastEffectKey = PantsBaseKey + "LastEffectNumber"

		if data[BeltEnchTypeKey] != -1:
			# Same idea as gauntlets and pauldrons
			if data[PantsLastEffectKey] == -1:
				data[PantsLastEffectKey] = 3
			counter1 = 0
			while counter1 <= data[BeltLastEffectKey]:
				baseString1 = BeltBaseKey + "Ench" + str(counter1)
				baseString2 = PantsBaseKey + "Ench" + str(data[PantsLastEffectKey] + 1)
				iterDict = data.copy()
				for k,v in iterDict.items():
					if k.startswith(baseString1):
						newString1 = k.replace(baseString1, '')
						newString2 = baseString2 + newString1
						print(newString2)
						print(v)
						data[newString2] = v
				data[PantsLastEffectKey] = data[PantsLastEffectKey] + 1
				counter1 = counter1 + 1



	##print(data)

# Once all the items are converted, delete the old Oblivion JSON and replace it with the new data
new_dict["Items"] = data
new_dict["Reset"] = {"ResetJSON":0}

os.remove(OBfull_path)
with open(OBfull_path, 'w') as f:
	json.dump(new_dict, f, indent=4)
f.close()

"""
with open(OBfull_path) as json_file:
	data = json.load(json_file)
	print(data)
"""