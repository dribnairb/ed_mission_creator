#For some reason this doesn't work inside ED Market Connector

import win32com
import win32com.client

import sys
sys.path.append(r"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Lib\site-packages") # TODO why isn't this available in EDMarketConnector?

msg = " ".join(sys.argv[1:])
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(msg)
