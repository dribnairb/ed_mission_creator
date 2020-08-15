import sys
import time

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
    #print(command)
    result = subprocess.Popen(command, startupinfo=startupinfo) # play in background
    #print(result)

# API version
# TODO need options to show a message for longer/shorter time. Even permanently for a mission objective maybe?
# TODO need to keep track of messages on screen so we can display other ones in a more suitable place
# TODO messages should be able to specify their colour, size etc.
def speak(msg, path=None, text=True, voice=True):
    #print("speak %s %s %s"%(text, voice, msg)) # debugging
    if text:
        for attempt in range(2): # Sometimes it fails for reasons I'm not entirely sure.
            try:
                global client
                if client is None:
                    from edmcoverlay import Overlay
                    client = Overlay()
                
                msgs = [ m.strip() for m in msg.split(".") if m.strip() ] # Split long lines. Assume each sentence fits on screen.
                ttl = 0
                for i,m in enumerate(msgs):
                    ttl += int(2+(0.4*len(m.split()))) # Longer time for longer messages
                    client.send_message(
                        msgid="ed_mission_creator%s"%i,
                        text=m,
                        color="#00ffff",
                        size="large",
                        x=25,
                        y=50+(i*22),
                        ttl=ttl
                        )
                    #time.sleep(0.1) # Waiting here means the voiceover won't start until we're finished. Plus we don't want to sleep on the last line. TODO maybe run in a thread?
                break # If it works, don't retry :)
            except Exception as e:
                print("Text failed %s"%e)
                client = None # I've seen "send_raw failed with [WinError 10053] An established connection was aborted by the software in your host machine" so maybe resetting the Overlay will fix it. Worth a try anyway :)
    
    if voice:
        try:
            if speaker:
                speaker.Speak(msg)
            else:
                speak2(msg,path)# Attempt it the other way
        except Exception as e:
            print("Text2Speech failed %s"%e)

if __name__=="__main__":
    msg = " ".join(sys.argv[1:])
    speak(msg, text=False, voice=True) # Running from the command line is when the voice PYTHONPATH isn't working
    import edmcoverlay, os
    
    edmcoverlay.HERE = os.path.split(edmcoverlay.HERE)[0]
    speak(msg, text=True, voice=False)
