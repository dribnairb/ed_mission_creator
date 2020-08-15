import sys

# Command line version because this doesn't work inside EDMarketConnector because not all the win32com stuff is in the PYTHONPATH
def speak2(msg, path):
    import subprocess
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    result = subprocess.Popen(["python",r"%s\speech.py"%path]+[msg], startupinfo=startupinfo) # play in background
    #print(result)

# API version which requires win32com and the rest of the speech stuff in the PYTHONPATH but EDMarketConnector doesn't have it. TODO figure this out
def speak(msg):
    #sys.path.append(r"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Lib\site-packages")
    #sys.path.append(r"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Lib\site-packages\win32")
    import win32com
    import win32com.client
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(msg)

if __name__=="__main__":
    msg = " ".join(sys.argv[1:])
    speak(msg)
