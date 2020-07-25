import math

#PATH = r"%LOCALAPPDATA%\EDMarketConnector\plugins\ed_mission_creator" # TODO Only works on Windows
PATH = r"C:\Users\dribn\AppData\Local\EDMarketConnector\plugins\ed_mission_creator" # TODO replace with above

def log(*args):
    line = " ".join([str(a) for a in args])
    #open(r"%s\ed_mission_creator.log"%PATH,"a").write("%s\n"%line)
    #open(r"C:\Users\dribn\AppData\Local\EDMarketConnector\plugins\ed_mission_creator\ed_mission_creator.log"%PATH,"a").write("%s\n"%line)
    print(line)
    
    
def distance(pos1,pos2):
    total = 0 
    for i in range(3):
        total += (pos1[i]-pos2[i])**2
    return math.sqrt(total)

def matchEntry(entry, required):
    result = True
    for key, expected in required.items():
        actual = str(entry.get(key))
        if isinstance(expected,(str,int,bool)):
            result = (actual == expected) and result
        else: # Assume regex
            result = (actual is not None and expected.match(actual)) and result
    return result
        
        