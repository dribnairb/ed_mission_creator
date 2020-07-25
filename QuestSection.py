from useful import *
import re

class QuestSection(object):
    def __init__(self, require, action):
        self.requireEvent = {}
        if "event" in require:
            for entry in require.pop("event").split(","):
                k,v = entry.strip().split(":")
                self.requireEvent[k.strip()] = v.strip()
        self.requireStore = []
        if "store" in require:
            self.requireStore.extend(require.pop("store").split(","))
            
        if "message" in action:
            self.actionMessage = action.pop("message")
        if "store" in action:
            self.actionStore = action.pop("store")
        
        self.require = require
        self.action = action
        
    def checkStore(self):
        return True
        
    def main(self, entry):
        if matchEntry(entry, self.requireEvent):
            if self.checkStore():
                self.execute(entry)
    
    def execute(self, entry):
        log("Action %s %s %s %s"%(self, entry, self.require, self.action)) # TODO debug. Should be empty action by now
        log(self.actionMessage.format(entry))
        log(self.actionStore)
        
        
        
