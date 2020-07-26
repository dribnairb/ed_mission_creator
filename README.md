# ed_mission_creator
Testing an idea for creating story/mission things for Elite Dangerous

Installation
------------
NOTE This is pre-alpha. It only works on Windows 10 and may not even work there :)

Copy the entire directory into the plugins folder for EDMarketConnector. eg:
c:\Users\me\AppData\Local\EDMarketConnector\plugins\ed_mission_creator

(Re)start ED Market Connector
In File -> Settings you should see ed_mission_creator under "Enabled plugins". If not, something has gone wrong. Logs may be available in %TMP%\EDMarketConnector.log

This requires Python3 to already be installed with win32com.client for speech.

Missions
--------
Each "mission" is a single .cfg file in the ed_mission_creator folder.
Each section within the file is a single step to be triggered when each of the "require_" properties is met
Once all require_ properties have been met by an event from ED Market Connector all the action_ properties are applied.
Disable a mission by renamed it (eg. add .disabled to the end of the filename)

require_event= a list of comma separated key:value pairs. Each key is a value in an event from Elite Dangerous. Currently the special key "near" is a semi-colon separated list of 4 numbers. The first 3 are X;Y;Z location in space and the fourth is a distance in LY. The step is considered True if the event contains a StarPos within that distance from the X;Y;Z location
require_store= a required step that must have already taken place. Must be unique across all missions

action_store=store this step as completed. Must be unique across all missions
action_message=Play a message to the player


Notes
-----
I know it's not coded very well, this is a proof of concept and I've changed my mind many times :)
Feel free to take any/all code and come up with something better
Alternatively, feel free to make new mission files and submit them. I am particularly interested in story arcs that lead to finding something in Elite Dangerous that a player might otherwise miss (eg. Something that points you towards the INRA bases without having to know in advance they already exist)

