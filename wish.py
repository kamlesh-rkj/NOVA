
def wish_user():
    from nova_engine import text_to_speech
    from nova_engine import datetime
    date=datetime.datetime.today().time()
    if date.hour>=12:
        text_to_speech("Good Afternoon sir")
    elif date.hour>=17:
        text_to_speech("Good Evening sir")    
    elif date.hour>=0 and date.hour<12:
        text_to_speech("Good Morning sir")
    text_to_speech("All  NOVA  System  is  online  ".upper()+"Wellcome To NOVA , How Can I Help You ?".upper())
