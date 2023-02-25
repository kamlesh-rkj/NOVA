from win32gui import GetWindowText, GetForegroundWindow
from nova_engine import time,text_to_speech
def waiting_mode():
    currentwindow=str(GetWindowText(GetForegroundWindow()))
    while "nova.py" not in currentwindow:
        time.sleep(1)    
        currentwindow=str(GetWindowText(GetForegroundWindow()))
    text_to_speech("again ,welcome sir,what can i do for you?")