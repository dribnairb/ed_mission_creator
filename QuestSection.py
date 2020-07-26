from useful import *
#import sys
#sys.path.append(r"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Lib\site-packages") # TODO why isn't this available in EDMarketConnector?

import re
import winsound # TODO this makes it windows only
#try:
#    import win32com
#    import win32com.client
#except ImportError as e:
#    log("cannot import win32com %s so no speech!"%e)

class QuestSection(object):
    def __init__(self, require, action, path):
        self.path = path
        
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
        
        self.actionStore = []
        if "store" in action:
            self.actionStore = [ x.strip() for x in action.pop("store").split(",") ]
        
        
        self.require = require
        self.action = action

    def getStorage(self):
        return r"%s\quests.store"%self.path
        
    def checkDistance(self, entry):
        return True # TODO StarPos isn't in all entry's so we need to check this iff it's a particular entry type. Maybe it needs to be a separate questsection
        # for system, distance in self.requireDistance
        
    def checkStore(self):
        print("checkStore %s %s"%(self.path, self.requireStore))
        f = self.getStorage()
        items = set(x.strip() for x in open(f).readlines())
        result = all(r in items for r in self.requireStore)
        return result
        
    def store(self):
        f = self.getStorage()
        items = set(x.strip() for x in open(f).readlines()) # TODO duplicates above
        
        for item in self.actionStore:
            if item not in items:
                items.add(item)
                
        open(f,"w").write("\n".join(sorted(items))) # TODO make thread safe
    
    def main(self, entry):
        if matchEntry(entry, self.requireEvent):
            if self.checkStore() and self.checkDistance(entry):
                log("Action %s %s %s %s"%(self, entry, self.require, self.action)) # TODO debug. Should be empty action by now
                msg = self.actionMessage.format_map(entry)
                log(msg)
                try:
                    #speaker = win32com.client.Dispatch("SAPI.SpVoice")
                    #speaker.Speak(msg)
                    import subprocess
                    #subprocess.call()
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    startupinfo.wShowWindow = subprocess.SW_HIDE
                    subprocess.Popen(["python",r"%s\speech.py"%self.path]+(msg.split()), startupinfo=startupinfo) # play in background
                except Exception as e:
                    log("Text2Speech failed %s"%e)

                #winsound.MessageBeep()
                #log(self.actionStore)
                if self.actionStore:
                    self.store()
        
        
        
        
