from useful import *
import traceback
import Quest
import os
import glob
import sys
import speech

# Minimal load for Quests
VERSION = 0.02
QUESTS = []

def plugin_start3(plugin_dir):
    # Look for load any quests
    for f in glob.glob(r"%s\*.cfg"%plugin_dir):
        QUESTS.append(Quest.load(f, plugin_dir))
    log("ed_mission_creator started %s"%sys.path)
    speech.speak("ED mission creator started with %s quests"%len(QUESTS), path=plugin_dir)
    return "v%s with %s quests from %s"%(VERSION, len(QUESTS),  plugin_dir)
    
def plugin_stop():
    pass
  
def journal_entry(cmdr, is_beta, system, station, entry, state):
    if entry.get("event") not in ("Music","ShipTargeted","ReceiveText"): # For speed, ignore common events we're not interested in. TODOSPEED calculate this list based on the loaded quests
        #debug(entry) # TODO remove
        for quest in QUESTS:
            try:
                quest.main(entry)
            except:
                log("QUEST: %s failed: %s"%(quest, traceback.format_exc()))

        
    
if __name__=="__main__":
    # testing
    plugin_start3(r"%localappdata%\EDMarketConnector\plugins\ed_mission_creator")
    #journal_entry("cmdr",False, "System","Station",{'timestamp': '2020-07-26T14:48:43Z', 'event': 'FSDTarget', 'Name': 'Auss', 'SystemAddress': 2243877095787, 'StarClass': 'F'},{})
    journal_entry("cmdr",False, "System","Station",{'timestamp': '2020-07-26T14:48:43Z', 'event': 'FSSSignalDiscovered', 'ThreatLevel': 0, 'SystemAddress': 2243877095787, 'StarClass': 'F'},{})
