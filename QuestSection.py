from useful import *
import re

class QuestSection(object):
    def __init__(self, require, action, path):
        self.path = path
        
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
        print("checkStore %s %s"%(self.path, self.requireStore))
        return True
        
    def store(self):
        for item in self.actionStore:
            print("STORE %s"%item) # TODO need namespace of quest (and quest section?). And need to append to existing list
    
    def main(self, entry):
        if matchEntry(entry, self.requireEvent):
            if self.checkStore():
                log("Action %s %s %s %s"%(self, entry, self.require, self.action)) # TODO debug. Should be empty action by now
                log(self.actionMessage.format(entry))
                log(self.actionStore)
                if self.actionStore:
                    self.store()
        
        
        
        
