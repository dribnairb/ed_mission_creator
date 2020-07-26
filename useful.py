import math

#PATH = r"%LOCALAPPDATA%\EDMarketConnector\plugins\ed_mission_creator" # TODO Only works on Windows
PATH = r"C:\Users\dribn\AppData\Local\EDMarketConnector\plugins\ed_mission_creator" # TODO replace with above

def log(*args):
    line = " ".join([str(a) for a in args])
    print(line)
    
def debug(*args):
    line = " ".join([str(a) for a in args])
    open(r"c:\temp\events.log","a").write("%s\n"%line)
    
def distance(pos1,pos2):
    total = 0 
    for i in range(3):
        total += (pos1[i]-pos2[i])**2
    return math.sqrt(total)

def matchEntry(entry, required):
    result = True
    for key, expected in required.items():
        # Special case:
        if key == "near":
            expected = expected.split(";")
            if "StarPos" in entry:
                expectedPos, expectedDistance = (float(expected[0]), float(expected[1]), float(expected[2])), float(expected[3])
                howFar = distance(entry["StarPos"], expectedPos)
                log("%sLY from %s"%(howFar, expectedPos))
                result = howFar <= expectedDistance and result
                entry["distance"] = howFar
        else:
            actual = str(entry.get(key))
            if isinstance(expected,(str,int,bool)):
                result = (actual == expected) and result
            else: # Assume regex TODO not a great solution
                result = (actual is not None and expected.match(actual)) and result
        #print(key, expected,actual, result)
    return result
        
        