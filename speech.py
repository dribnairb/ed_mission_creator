import sys

global client
client = None

try:
    #sys.path.append(r"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Lib\site-packages")
    #sys.path.append(r"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Lib\site-packages\win32")
    import win32com # TODO this doesn't work inside EDMC, seemingly because the site-packages are not in PYTHONPATH. But it works from the command line in windows 10
    import win32com.client
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
except Exception as e:
    speaker = None
    print("Voice unavailable %s"%e)
    

# Command line version because this doesn't work inside EDMarketConnector because not all the win32com stuff is in the PYTHONPATH
def speak2(msg, path):
    import subprocess
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    command = ["python",r"%s\speech.py"%path]+[msg]
    print(command)
    result = subprocess.Popen(command, startupinfo=startupinfo) # play in background
    print(result)

# API version
def speak(msg, text=True, voice=True):
    print("speak %s %s %s"%(text, voice, msg)) # debugging
    if text:
        global client
        if client is None:
            from edmcoverlay import Overlay
            client = Overlay()
        
        client.send_message(
          msgid="ed_mission_creator1",
          text=msg,
          color="#ffffff",
          size="large",
          x=100,
          y=100,
          ttl=20)
    
    if voice:
        if speaker:
            speaker.Speak(msg)
        else:
            raise Exception("Voice not available")

if __name__=="__main__":
    msg = " ".join(sys.argv[1:])
    speak(msg, text=False, voice=True) # Running from the command line is when the voice PYTHONPATH isn't working
