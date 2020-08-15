from useful import *

import re
import speech

class QuestSection(object):
    def __init__(self, quest, section, require, action):
        self.quest = quest
        self.section = section
        self.path = quest.path
        self.name = quest.name
        
        self.requireEvent = {}
        if "event" in require:
            for entry in require.pop("event").split(","):
                k,v = entry.strip().split(":")
                v = v.strip()
                if re.match("re\(.+\)", v): # TODO not a great solution
                    v = re.compile(v[3:-1])
                self.requireEvent[k.strip()] = v
        self.requireStore = []
        if "store" in require:
            self.requireStore.extend([x.strip() for x in require.pop("store").split(",")])
            
        self.requireDistance = {}
        if "distance" in require:
             for entry in require.pop("distance").split(","):
                k,v = entry.strip().split(":")
                v = int(v.strip())
                self.requireDistance[k.strip()] = v
        
        if "message" in action:
            self.actionMessage = action.pop("message")
        else:
            self.actionMessage = None
        
        self.actionStore = ["%s.%s"%(self.name, self.section)] # Default to saving this step is completed
        if "store" in action:
            self.actionStore = [ x.strip() for x in action.pop("store").split(",") ]
        
        
        self.require = require # This should be empty by now
        self.action = action # This should be empty by now

    def getStorage(self):
        return r"%s\quests.store"%self.path
        
    def checkStore(self):
        f = self.getStorage()
        try:
            items = set(x.strip() for x in open(f).readlines()) # TODO duplicates below
        except FileNotFoundError:
            items = set()
        result = True
        for item in self.requireStore:
            if item.startswith("!"):
                if item[1:] in items:
                    #debug(1,item, items)
                    result = False
            elif item not in items:
                #debug(2,item,items)
                result = False
        #result = all(r in items for r in self.requireStore)
        #print("checkStore %s %s %s"%(f, self.requireStore, result))
        return result
        
    def store(self):
        f = self.getStorage()
        try:
            items = set(x.strip() for x in open(f).readlines()) # TODO duplicates above
        except FileNotFoundError:
            items = set()
        
        for item in self.actionStore:
            if not item.startswith("!") and item not in items:
                items.add(item)
                
        open(f,"w+").write("\n".join(sorted(items))) # TODO make thread safe
    
    def main(self, entry):
        if matchEntry(entry, self.requireEvent):
            if self.checkStore():
                log("Action %s %s %s %s"%(self, entry, self.requireEvent, self.actionMessage)) # TODO debug. Should be empty action by now
                msg = self.actionMessage.format_map(entry)
                log(msg)
                try:
                    speech.speak(msg, path=self.path) # TODO path is only needed if I can't solve the problem with voice inside EDMC
                except Exception as e:
                    log("speak failed  %s"%e)

                if self.actionStore:
                    self.store()
                return True
        return False
        
        
        
        
