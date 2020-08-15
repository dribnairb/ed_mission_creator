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
# TODO need options to show a message for longer/shorter time. Even permanently for a mission objective maybe?
# TODO need to keep track of messages on screen so we can display other ones in a more suitable place
# TODO messages should be able to specify their colour, size etc.
def speak(msg, path=None, text=True, voice=True):
    print("speak %s %s %s"%(text, voice, msg)) # debugging
    if text:
        global client
        if client is None:
            from edmcoverlay import Overlay
            client = Overlay()
        
        msgs = [ m.strip() for m in msg.split(".") if m.strip() ] # Split long lines. Assume each sentence fits on screen.
        for i,m in enumerate(msgs):
            client.send_message(
                msgid="ed_mission_creator%s"%i,
                text=m,
                color="#ffffff",
                size="large",
                x=100,
                y=80+(i*22),
                ttl=20)
    
    if voice:
        try:
            if speaker:
                speaker.Speak(msg)
            else:
                speak2(msg,path)# Attempt it the other way
        except Exception as e:
            log("Text2Speech failed %s"%e)

if __name__=="__main__":
    msg = " ".join(sys.argv[1:])
    speak(msg, text=False, voice=True) # Running from the command line is when the voice PYTHONPATH isn't working
    import edmcoverlay, os
    
    edmcoverlay.HERE = os.path.split(edmcoverlay.HERE)[0]
    speak(msg, text=True, voice=False)
