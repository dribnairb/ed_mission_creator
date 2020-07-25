from useful import *
import traceback
import Quest
import os
import glob

# Minimal load for Quests
VERSION = 0.01
QUESTS = []

def plugin_start3(plugin_dir):
    # Look for load any quests
    for f in glob.glob(r"%s\*.cfg"%plugin_dir):
        QUESTS.append(Quest.load(f))
    return "v%s with %s quests from %s"%(VERSION, len(QUESTS),  plugin_dir)
    
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

        
    
