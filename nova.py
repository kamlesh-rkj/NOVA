import nova_engine as ne
from waiting import waiting_mode
start_nova = ne.speech_to_text().lower()
# print(start_nova)
if "nova".lower() in start_nova:
    from wish import wish_user
    wish_user()
    # ne.text_to_speech("  All  NOVA  System  is  online  ".upper()+"Wellcome To NOVA , How Can I Help You ?".upper())
    while True:
        speech_data = ne.speech_to_text().lower()
        # ..................normal command's...................

        if "time now".lower() in speech_data:
            temp = ne.datetime.datetime.now().strftime( "%I Hour, %M Minite , %S Secound , %p")
            # print(time)
            ne.text_to_speech("current time is "+temp)

        elif "how are you".lower() in speech_data:
            ne.text_to_speech(
                " I AM FINE THANK YOU KAMLESH , YOU ARE SO CARING PERSON ")

        elif "go and sleep".lower() in speech_data or "exit".lower() in speech_data:
            ne.text_to_speech("all system goes to offline master".upper())
            ne.text_to_speech("i hope you  come to me in near future ".upper())
            break

        elif "tell about you".lower() in speech_data:
            ne.text_to_speech('''
                    my name is nova,
                    i was created by kamlesh ratanpara,
                    i am one day old,
                    i have many mode's like normal mode , command mode , friend mode , hacking mode,..etc,
                    my defualt mode is friend mode,
                    if i dont work properly , please contect my creater,
                    i provoide his contect number and gmail id in your terminal, please see there 
                '''.upper())
            print("my creater gmail id is ".upper()+" rkjrk514@gmail.com")
            print("my creater phone number is".upper()+" 8866151630")

        elif "which date today".lower() in speech_data:
            date = ne.datetime.datetime().date()
            ne.text_to_speech(date.today())

        elif " tell me joke".lower() in speech_data:
            joke = ne.pyjokes.get_joke(language="guj")
            print(joke)
        # .............. SYSTEM COMMAND'S OR OS COMMAND'S ................
        elif "open notepad".lower() in speech_data:
            notepade_path = "C://Windows//System32//notepad.exe"
            ne.os.startfile(notepade_path)
            ne.time.sleep(5)
            waiting_mode()

        elif "open sublime text editor".lower() in speech_data:
            sublime_path = "C://Program Files//Sublime Text//sublime_text.exe"
            ne.os.startfile(sublime_path)
            ne.time.sleep(5)
            waiting_mode()
        elif "open android studio".lower() in speech_data:
            android_path = "C://Program Files//Android//Android Studio//bin//studio64.exe"
            ne.os.startfile(android_path)
            ne.time.sleep(5)
            waiting_mode()
        elif "play music".lower() in speech_data:
            song_path = "D://2//song"
            songs = ne.os.listdir(song_path)
            random_song_choies = ne.random.choice(songs)
            ne.os.startfile(ne.os.path.join(song_path, random_song_choies))
            ne.time.sleep(5)
            waiting_mode()
        # ..................NETWORK COMMAND'S...........................
        elif "open youtube".lower() in speech_data:
            ne.text_to_speech("which channel you want to see ".upper())
            speech_data_temp = ne.speech_to_text().lower()
            temp = speech_data_temp.split(" ")
            speech_data_temp2 = ""
            for i in temp:
                speech_data_temp2 += "".join(i)
            print(speech_data_temp)
            ne.text_to_speech("youtube started sucssesfully".upper())
            try:
                ne.webbrowser.open_new_tab(
                    "https://www.youtube.com/@"+speech_data_temp2)
                ne.time.sleep(5)
                waiting_mode()
            except Exception as e:
                pass

        elif " open website".lower() in speech_data:
            ne.text_to_speech("your webbrowser is started ".upper())
            ne.text_to_speech("tell me which website you want to open".upper())
            temp = ne.speech_to_text().lower()
            # temp=speech_dat
            ne.webbrowser.open_new_tab("https://www.google.com/search?q="+temp)
            ne.time.sleep(5)
            waiting_mode()

        elif "ip address".lower() in speech_data:
            ip = ne.requests.get('https://api.ipify.org').text
            print(f"your ip address is {ip}".upper())
            ne.text_to_speech(f"your ip address is ,{ip}")

        elif "send email to kamlesh".lower() in speech_data:
            try:
                print("what should i send in email")
                ne.text_to_speech("what should i send in email")
                content = ne.speech_to_text().lower()
                to = 'rkjrk515@gmail.com'.lower()
                ne.sendGmail(to, content)
                print("Email hash been send to kamlesh")
                ne.text_to_speech("Email hash been send to kamlesh")
            except Exception as e:
                print(e)
                ne.text_to_speech("sorry,i can not send Email ")
        elif "send whatsapp".lower() in speech_data or "send massage " in speech_data:
            to = ne.getReciverNumber()
            ne.text_to_speech("what should i send ")
            content = ne.speech_to_text().lower()
            ne.pywhatkit.sendwhatmsg_instantly(phone_no=to, message=content)
            ne.text_to_speech(f"message has been send to {to}")
        elif "play youtube song".lower() in speech_data:
            ne.text_to_speech("which song i play on youtube")
            ytsong_name = ne.speech_to_text().lower()
            ne.pywhatkit.playonyt(ytsong_name)
            ne.time.sleep(5)
            waiting_mode()
        elif "wikipedia".lower() in speech_data:
            ne.text_to_speech("what should i search on wikipedia")
            while True:
                wiki_search = ne.speech_to_text().lower()
                try:
                    result = ne.wikipedia.summary(wiki_search, 3)
                    print(result)
                    ne.text_to_speech(result)
                    break
                except ne.wikipedia.DisambiguationError as e:
                    ne.text_to_speech(f'''
                    i found many many information about {wiki_search},
                    please tell me exactly what you want to search on wikipedia
                    ''')
                except ne.wikipedia.PageError as e:
                    ne.text_to_speech(
                        f"i found same error in searching for{wiki_search},please tell me in deep")
        elif "wait".lower() in speech_data:
            from win32gui import GetWindowText, GetForegroundWindow
            currentwindow = str(GetWindowText(GetForegroundWindow()))
            while "nova.py" not in currentwindow:
                ne.time.sleep(2)
                currentwindow = str(GetWindowText(GetForegroundWindow()))
            ne.text_to_speech("again ,welcome sir,what can i do for you?")
        ne.time.sleep(0.5)
else:
    ne.text_to_speech("ohh shit,Nova System failear ".upper())
    ne.text_to_speech(start_nova)
