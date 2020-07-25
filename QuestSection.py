from useful import *
import re

class QuestSection(object):
    def __init__(self, require, action):
        self.requireEvent = {}
        if "event" in require:
            for entry in require.pop("event").split(","):
                for k,v in entry.strip().split(":"):
                    self.requireEvent[k.strip()] = v.strip()
        self.requireStore = []
        if "store" in require:
            self.requireStore.extend(require.pop("store").split(","))
        self.require = require
        
        self.action = action
        
    def checkStore(self):
        return True
        
    def main(self, entry, self.requireEvent):
        if matchEntry(entry, self.requireEvent):
            if self.checkStore():
                section.execute(entry)
    
    def execute(self, entry):
        log("Action %s %s %s"%(self, entry, self.action))
