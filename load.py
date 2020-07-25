from useful import *
import traceback
import Quest
import os

# Minimal load for Quests
VERSION = 0.01
QUESTS = []

def plugin_start3(plugin_dir):
    # Look for load any quests
    for f in glob.glob("*.cfg"):
        QUESTS.append(Quest.load(f))
    return "ed_mission_creator v%s with %s quests from %s"%(VERSION, len(QUESTS),  os.getcwd())
    
def plugin_stop():
    pass
  
def journal_entry(cmdr, is_beta, system, station, entry, state):
    if entry.get("event") not in ("ReceiveText","Music"):
        log(entry) # Mainly for debugging
        for quest in QUESTS:
            try:
                quest.main(entry)
            except:
                log("QUEST: %s failed: %s"%(quest, traceback.format_exc()))

        
    
