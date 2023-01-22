Nickies' CrossGame Add-On
by Nickies 1/22/2023

____________________________________________
| 					   |
|   MORROWIND INSTALLATION INSTRUCTIONS:   |
|                                          |
|__________________________________________|

1. Create folder (if you haven't already) on your C:\ Drive (accessed by clicking This PC -> Windows C:) called "NickiesData" -- ensure spelling is correct.
2. Put the files in the "NickiesData" folder in "NickiesCrossGameMorrowind" into your newly created C:\NickiesData\ folder

Now we're going to make sure the scripts that transfer files between the two games have the right filepaths.

2a. Open "toMorrowindSpell.py" in Notepad or a text editor of your choice.
2b. See at the top of the file, where it says MWfilepath and OBfilepath? You need to change these to the filepaths your versions of the games use.
By default, this is set to a Steam installation of Morrowind and an Oblivion installation at C:\Games\

TO COPY THE RIGHT FILEPATH:

Go to your Morrowind folder. Open "Data Files". Open "MWSE". Click in the white space up in the address bar, next to where it should
say something like Morrowind>Data Files>MWSE. This should highlight your file path. Copy what is highlighted.

Then, back in toMorrowindSpell.py, paste the filepath between the two '' symbols. 
VERY IMPORTANT: Add an additional \ every time one occurs in the filepath.

[When I say 'what it should look like' below, I don't mean the literal filepath, just that you remembered to double-slash and include the ' symbols on both ends]

What it should look like: 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Morrowind\\Data Files\\MWSE'
BAD: 'C:\Program Files (x86)\Steam\steamapps\common\Morrowind\Data Files\MWSE' [No double-slash]
BAD: C:\\Program Files (x86)\\Steam\\steamapps\\common\\Morrowind\\Data Files\\MWSE [Missing ' symbols at the ends]

Then do the same for your Oblivion Data folder filepath. This is done the same as the Morrowind MWSE folder: go to your
Oblivion folder, then click on "Data". Click ion the white space in the address bar to the right of Oblivion>Data, and copy it.

Then, back in toMorrowindSpell.py, paste the filepath between the two '' symbols.

What it should look like: 'C:\\Games\\Oblivion\\Data\\'

Now, I recommend copying these four lines so you don't have to repeat this process anymore:
#Change this to your MWSE filepath, in your Morrowind Data Files directory
MWfilepath = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Morrowind\\Data Files\\MWSE\\'
#Change this to your Oblivion Data directory path
OBfilepath = 'C:\\Games\\Oblivion\\Data\\'

With those four lines copied [showing your filepaths, not the original examples unless they happen to match], replace the filpaths
in the following files to your own:

toMorrowindSpell.py (should be done already)
toMorrowindItem.py
toMorrowindPlayer.py
toMorrowindMisc.py

I recommend holding on to the four lines you copied for the Oblivion installation if you haven't done it yet.

3. Put the files in the "Data Files" folder in "NickiesCrossGameMorrowind" into your Morrowind directory's Data Files folder
4. Remember to activate "NickiesCrossGameNew.esp" in your Morrowind Launcher or Mod Manager before beginning

____________________________________________
| 					   |
|    OBLIVION INSTALLATION INSTRUCTIONS:   |
|                                          |
|__________________________________________|

1. Create folder (if you haven't already) in your C:\ Drive (accessed by clicking This PC -> Windows C:) called "NickiesData" -- ensure spelling is correct.
2. Put the files in the "NickiesData" folder in "NickiesCrossGameOblivion" into your newly created C:\NickiesData\ folder

Now we're going to make sure the scripts that transfer files between the two games have the right filepaths.

2a. Open "toMorrowindSpell.py" in Notepad or a text editor of your choice.
2b. See at the top of the file, where it says MWfilepath and OBfilepath? You need to change these to the filepaths your versions of the games use.
By default, this is set to a Steam installation of Morrowind and an Oblivion installation at C:\Games\

TO COPY THE RIGHT FILEPATH:

Go to your Morrowind folder. Open "Data Files". Open "MWSE". Click in the white space up in the address bar, next to where it should
say something like Morrowind>Data Files>MWSE. This should highlight your file path. Copy what is highlighted.

Then, back in toMorrowindSpell.py, paste the filepath between the two '' symbols. 
VERY IMPORTANT: Add an additional \ every time one occurs in the filepath.

[When I say 'what it should look like' below, I don't mean the literal filepath, just that you remembered to double-slash and include the ' symbols on both ends]

What it should look like: 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Morrowind\\Data Files\\MWSE'
BAD: 'C:\Program Files (x86)\Steam\steamapps\common\Morrowind\Data Files\MWSE' [No double-slash]
BAD: C:\\Program Files (x86)\\Steam\\steamapps\\common\\Morrowind\\Data Files\\MWSE [Missing ' symbols at the ends]

Then do the same for your Oblivion Data folder filepath. This is done the same as the Morrowind MWSE folder: go to your
Oblivion folder, then click on "Data". Click ion the white space in the address bar to the right of Oblivion>Data, and copy it.

Then, back in toMorrowindSpell.py, paste the filepath between the two '' symbols.

What it should look like: 'C:\\Games\\Oblivion\\Data\\'

Now, I recommend copying these four lines so you don't have to repeat this process anymore:
#Change this to your MWSE filepath, in your Morrowind Data Files directory
MWfilepath = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Morrowind\\Data Files\\MWSE\\'
#Change this to your Oblivion Data directory path
OBfilepath = 'C:\\Games\\Oblivion\\Data\\'

With those four lines copied [showing your filepaths, not the original examples unless they happen to match], replace the filpaths
in the following files to your own:

fromMorrowindSpell.py (should be done already)
fromMorrowindItem.py
fromMorrowindPlayer.py
fromMorrowindMisc.py

I recommend holding on to the four lines you copied for the Morrowind installation if you haven't done it yet.

3. Put the files in the "Data" folder in "NickiesCrossGameOblivion" into your Oblivion directory's Data Files folder

OBLIVION-ONLY INSTRUCTION:
4. Put the files in the "Saves" folder in your Saves folder located in Documents -> My Games -> Oblivion -> Saves

5. Remember to activate "NickiesCrossGameBoss" in your Oblivion Launcher or Mod Manager before beginning


____________________________________________
|					   |
|     GOOD CHECK TO SEE IF YOU'RE GOOD:    |
|                                          |
|__________________________________________|

At the end of Installation, your C:\NickiesData folder should have 8 files:

toMorrowindSpell.py
toMorrowindItem.py
toMorrowindPlayer.py
toMorrowindMisc.py
fromMorrowindSpell.py
fromMorrowindItem.py
fromMorrowindPlayer.py
fromMorrowindMisc.py

And all of them should have your filepaths at the top of them instead of the originals, unless they happen to match.

____________________________________________
| 					   |
|	  TO SKIP THE BOSS FIGHT:	   |
|                                          |
|__________________________________________|

In Morrowind, open the console and type "set NickiesCrossSaveCheck to 2". The relevant things should appear in Addamasartus as if you beat the boss in both Morrowind and Oblivion.
In Oblivion, open the console and type "set NickiesBossDefeatedGlobal to 1". The relevant things should appear in Vilverin as if you beat the boss in both Morrowind and Oblivion.

____________________________________________
| 					   |
|    CROSS GAME TRANSFER BEST PRACTICES:   |
|                                          |
|__________________________________________|

I tried to ensure as many effects and mechanics from Morrowind as possible were preserved when transferred to Oblivion. This includes On-Use enchantments, Constant Effect enchantment weapons,
and On-Self When Strikes weapon enchantment effects. GETTING THESE EFFECTS IN OBLIVION IS ONLY POSSIBLE BY TRANSFERRING ITEMS FROM MORROWIND.

Differences in mechanics:
	- On-Use enchantments are now simply usable once-per-day rather than operating off charge. For balancing purposes, you must wait a day after picking up the item to use it.
		-- If your On-Use item isn't working, try dropping it and picking it up to see if the relevant Greater Power was added. Note as above you must wait 24 hours before using it.
	- Almost all spell effects in Morrowind that don't exist in Oblivion are converted to some analog, e.g. Jump effects are converted to Fortify Acrobatics.
	- Note all effects are kept, however, mostly for stability. For example, the Lock effect from Morrowind is not transferred.
	- Non-transferred effects are sometimes transferred as a dummy effect, a magnitude 0 "Fortify Luck" effect, so that total effect count is preserved for internal purposes.

Note that the only added mechanic to Morrowind in transfers is the Reflect Damage effect, which is added with identical functionality to Oblivion. Like the added Morrowind mechanics in Oblivion,
this is only obtainable by transferring Oblivion items with the effect to Morrowind.

As a general rule, transfers should follow a strict Oblivion->Morrowind->Oblivion->Morrowind basis (rather than trying Oblivion->Morrowind->Morrowind or what have you). I do recommend your first
transfer be Oblivion -> Morrowind and I'm not sure the game will let you do the reverse as your first transfer.

Real-time transferring (having both games open at once) IS supported for spells and items, but not necessarily player data.

Obviously, you can exploit this add-on for things like item duplication. Use at your own discretion.
