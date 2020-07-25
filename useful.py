import math

def log(*args):
    line = " ".join([str(a) for a in args])
    open(r"C:\Users\dribn\AppData\Local\EDMarketConnector\plugins\Brian\brian.log","a").write("%s\n"%line)
    
def distance(pos1,pos2):
    total = 0 
    for i in range(3):
        total += (pos1[i]-pos2[i])**2
    return math.sqrt(total)

def matchEntry(entry, required):
    result = True
    for key, expected in required.items():
        actual = entry.get(key)
        if isinstance(expected,(str,int,bool)):
            result = (actual == expected) and result
        else: # Assume regex
            result = (actual is not None and expected.match(actual)) and result
    return result
        
        