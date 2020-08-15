# ed_mission_creator https://github.com/dribnairb/ed_mission_creator
Testing an idea for creating story/mission things for Elite Dangerous

Prerequisites
-------------
ED Market Connector: https://github.com/EDCD/EDMarketConnector/releases/tag/Release%2F4.0.4 (When I wrote this I was using v4.0.4. Other versions may or may not work)
EDMCOverlay: https://github.com/inorton/EDMCOverlay/releases (When I wrote this I was using v1.0.5. Other versions may or may not work).
Windows 10: win32com.client is required for voiceover. May or may not be required for the rest of the plugin to work (I've not tested it).
Python 3 https://www.python.org/ (This may not be necessary if you don't want a voiceover. But ED Market Connector uses Python anyway. At time of writing I can't get the voice to work within EDMC so it tries to call python directly from the command line)



Installation
------------
NOTE This is pre-alpha. Don't be surprised if there are bugs or problems.

Download the zip from https://github.com/dribnairb/ed_mission_creator (Code -> Download ZIP)
Unzip the entire directory into the plugins folder for EDMarketConnector. eg:
c:\Users\me\AppData\Local\EDMarketConnector\plugins\ed_mission_creator


(Re)start ED Market Connector
In File -> Settings you should see ed_mission_creator under "Enabled plugins". If not, something has gone wrong. Logs may be available in %TMP%\EDMarketConnector.log




Example Mission
---------------
quest1.cfg contains an example mission. It should start next time you dock at a station (Fleet Carrier probably doesn't work)
The mission now uses EDMCOverlay to show text and attempts to play voiceover using Windows 10 voice library

Create your own Missions
------------------------
Each "mission" is a single .cfg file in the ed_mission_creator folder.
Each section within the file is a single step to be triggered when each of the "require_" properties is met
Once all require_ properties have been met by an event from ED Market Connector all the action_ properties are applied.
Disable a mission by renamed it (eg. add .disabled to the end of the filename)

require_event= a list of comma separated key:value pairs. Each key is a value in an event from Elite Dangerous. Currently the special key "near" is a semi-colon separated list of 4 numbers. The first 3 are X;Y;Z location in space and the fourth is a distance in LY. The step is considered True if the event contains a StarPos within that distance from the X;Y;Z location
require_store= comma separated list of required steps that must have already taken place. Each name must be unique across all missions. Prefix of ! means must NOT have been completed yet.

action_store=store this step as completed. Name must be unique across all missions
action_message=Play a message to the player


Notes
-----
I know it's not coded very well, this is a proof of concept and I've changed my mind many times :)
Feel free to take any/all code and come up with something better
Alternatively, feel free to make new mission files and submit them. I am particularly interested in story arcs that lead to finding something in Elite Dangerous that a player might otherwise miss (eg. Something that points you towards the Eagle Eye network without having to know in advance they already exist, and then nudging you in the right direction after that)
