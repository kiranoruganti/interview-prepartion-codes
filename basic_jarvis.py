import pyttsx3 as pyt
import speech_recognition as sr
import datetime
import os
import cv2
import random
import pywhatkit  # This method can be used to remotely control your PC using your phone (Windows only)
import pyautogui
#from welcome_backsir import *  # welcomeback sir animation code
from requests import get
import wikipedia
import webbrowser
from pydub import AudioSegment
from pydub.playback import play
import pyjokes
import keyboard

engine = pyt.init("sapi5")
voices = engine.getProperty("voices")  # voices is a variable
# print(voices)
'''
voice[0] and voice[3]=david voice
voice[1]= microsoft mark voice(better one)'
voice[2] and voice[4]=zira voice'''
engine.setProperty("voice", voices[
    1].id)  # 1st parameter lo voices ani pedthe male voice ye osthadi everytime change it to voice and voices[should be 1 for female 0 for male]
engine.setProperty("rate", 160)  # 2nd parameter sets speed of voice

chose=0#for music


# converts text to speech
def speak(audio):
    engine.say(audio)  # says the given audio
    engine.runAndWait()


# takecommand takes voiceinput from user and converts it to text and displays it on screen (required module=speechrecognition)
def takecommand():
    listener = sr.Recognizer()
    # microphone is source for voice
    with sr.Microphone() as source:
        print("Listening.....")
        listener.pause_threshold = 1
        voice = listener.listen(source, timeout=10, phrase_time_limit=6)  # listens user voice from source(microphone)
        #phrase_time_limit=5 means jarvis listens for 5 seconds to our speech
        # if you dont speak or microphone is off for sometime(10) jarvis will automatically terminate

    try:
        print("Recognizing...")
        query = listener.recognize_google(voice, language="en-in")  # lang=english-india
        # string madyala variable name iyaniki format strings vadtham

        query = query.lower()  # converts user input to small letters
        print(f"user said:{query}")  # prints what user said

    except Exception as e:
        print("Say that again please...")
        speak("Sorry i didn't understand say that again please...")
        return "none"
    return query


# to wish
def wishme():
    hour = int(datetime.datetime.now().hour)
    # print(hour)

    if hour >= 0 and hour < 12:
        print("good morning")
        speak("good morning ")
    elif hour >= 12 and hour < 18:
        print("good afternoon")
        speak("good afternoon")
    else:
        print("good evening")
        speak("good evening")
    print("i am jarvis,how can i help you")
    speak("i am jarvis,how can i help you")


if __name__ == "__main__":

    while True:

        # userinput will be stored in query var
        query = takecommand()

        if "introduce yourself" in query or "tell me about yourself" in query or "jarvis introduce yourself" in query:
            speak("hello,i am jarvis built by my boss kiran oruganti")
            # from jarvis_with_sound import *

        elif "how are you" in query:
            speak("I'm great thanks for asking")

        elif "open notepad" in query or "open Notepad" in query:
            os.system("start notepad")
        elif "close notepad" in query:
            os.system("TASKKILL /F /IM Notepad.exe")

        elif "open command prompt" in query:
            if True:
                speak("opening command prompt")
                os.system("start cmd")
            else:
                speak("sorry you dont have command prompt")

        # elif "open powerpoint" in query:
        #     if True:
        #         os.system("POWERPNT")
        #     else:
        #         speak("sorry, you dont have ms powerpoint in your device")

        # elif "open ms word" in query:
        #     wpath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        #     os.system(wpath)
        # elif ("open telegram" in query) or ("telegram" in query) :
        #     if True:
        #         speak("Opening telegram")
        #         os.system("telegram")
        #     else:
        #         speak('you dont have telegram in your device')

        # elif "open mail" in query:
        #     os.system("mail")
        # elif "open microsoft store" in query:
        #     os.system("microsoft store")

        elif "open file explorer" in query:
            speak("opening file explorer")
            os.system("explorer")

        elif "open camera" in query:
            speak("opening camera")
            speak("press esc to close camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k == 27:#press esc to close camera
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "what is the time" in query or "time" in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is ' + time)
            speak('Current time is ' + time)

# <------------------------------------SENDING WHATSAPP MESSAGE USING JARVIS------------------------------------------------->

        elif "send whatsapp message" in query or "send whatsapp message" in query or \
                 " i want to send a message in whatsapp" in query or "send a whatsapp message" in query \
                 or "whatsaap message" in query:

                contacts = {"mother": "+9196522 61371", "sister": "+919666678143", "teja reddy": "+918499086087",
                            "swaranjitha": "+91 79810 40672", "nandini": "+91 93812 74249", "swetha": "+9190523 38989",
                            "sushma": "+919381746260", "vyshnavi": "+91 80085 77233", "afreen": "+91 95427 71221 ",
                            "shirisha": "+91 93909 04160", "shivani": "+916305336475", "gracy": "+919390420357",
                            "saketh": "+91 96187 35313", "nagacharan": "+917675915987", "tony": "+919014241961",
                            "pavan": "+91 93982 58816", "nikhil": "+917793906095", "balaji": "+91 95152 37210 ",
                            "sri teja": "7889490068", "shalini": "+919100891759", "madhukar sir": "+9198469117393",
                            "cp sir": "+919848072444", "aravind sir": "+91 77300 70111", "ranjith sir": "+919347309750",
                            "ramesh sir": "+919866826110", "ramu sir": "+918309175449", "srikanth sir": "+919985740968 ",
                            "varaprasad sir": "+91 8555950622", "hema bindu mam": "+919908881941",
                            "shoba mam": "+919849384255",
                            "deepthi mam": "+919573817887", "sumalatha mam": "+919700215715",
                            "srilatha mam": "+919100374481",
                            "shirisha mam": "+918008743213"}

                names_list = list(contacts.keys())  # converts keys to list
                speak("sure!,whom do you wanna send")
                msgloop = True
                while msgloop:
                    contact_name = takecommand()  # calling takemethod again to take voice input for this sepecific variable(contact_name)

                    if contact_name in names_list:
                        number = contacts[contact_name]
                        print(number)
                        speak("what message u wanna send")
                        msg = takecommand()  # calling takemethod again to take voice input for this sepecific variable(msg)
                        print("your message:", msg)
                        speak("your message will be delivered in 10 to 30 seconds")
                        pywhatkit.sendwhatmsg_instantly(number, msg)  # pywhatkitsends msg instantly
                        speak("message delivered")
                        msgloop = False

                    else:
                        speak("please enter from available contacts")
                        msgloop = False




        #<-----------------playing audio using jarvis------------------------>
        elif "i love you" in query or "friday i love you" in query:
            romeo = AudioSegment.from_wav("nuvemaina romeo.wav")
            play(romeo)
            # from romeodilogue import *

        elif "he died loving but I am not his type" in query or "he died loving" in query:
            cp = AudioSegment.from_wav("chala shekal unnay ra neelo.wav")
            play(cp)
            # from chala_shekal_unnay import *

        elif "jarvis do you love me" in query or "do you love me" in query:
            fs = AudioSegment.from_wav("I Just Want Flirtationship.wav")
            play(fs)
            # from I_just_want_flirtationship import *

        elif "propose me" in query or "propose this lady" in query or "propose this girl" in query:
            pd = AudioSegment.from_wav("Malli Malli Idhi Rani Roju.wav")
            play(pd)
            # from propose_dialogue import *

        elif "propose him" in query or "propose this guy" in query:
            mca = AudioSegment.from_wav("mca proposal scene.wav")
            play(mca)
            # from mca_proposal_scene import *

        elif "idiot" in query or "stupid" in query or "waste fellow" in query or "psycho" in query:
            brahmi1 = AudioSegment.from_wav("yendi bro antha mata annav(720P_HD).wav")
            play(brahmi1)
            # from yendi_bro_anthamataannav import *


        elif "who is teja reddy" in query or "teja reddy" in query:
            kingu = AudioSegment.from_wav("kingu koduku.wav")
            play(kingu)
            # from kingu_koduku import *

        elif "jarvis she loves you" in query or "love you" in query or "she loves you" in query:
            # from devudu_unnadra import *

            karthi1 = AudioSegment.from_wav("Devudu unnadra.wav")
            play(karthi1)

        elif "but as a friend" in query:
            karthi2 = AudioSegment.from_wav("Devudu ledra.wav")
            play(karthi2)

        elif "why should anyone love you" in query or "jarvis why should anyone love you" in query or "jarvis why should i love you" in query:

            orange = AudioSegment.from_wav("nijayithi unnodini.wav")
            play(orange)

        elif "bye jarvis" in query or "bye" in query or "goodbye" in query or "jarvis bye" in query:
            husharu1 = AudioSegment.from_wav("Undiporadhey song.wav")
            play(husharu1)
            # from undiporadhe import *

        elif "jarvis sing a song for me" in query or "jarvis sing a song" in query or "sing a song" in query:
            husharu2 = AudioSegment.from_wav("vere janmantu naake nduku le.wav")
            play(husharu2)
            # from verejanmantu import *



        # to make this work we have to link whatsapp web in microsoft edge to mobile
        # elif "send WhatsApp message" in query:
        #     pywhatkit.sendwhatmsg("+919652261371",
        #                           "hello i am jarvis this message is sent by my boss from pycharms code", 11, 57)


        elif "music" in query or "hit some music" in query:
            speak("playing music")
            music_dir_path = "C:\\Users\\kiran\\Music"
            songs = os.listdir(music_dir_path)  # converting songs into list
            d = random.choice(songs)  # chooses random music
            os.startfile(os.path.join(music_dir_path, d))  # plays random music
            chose+=1

        elif "next" in query or "i don't like this " in query\
                or "next song" in query:
            music_dir_path = "C:\\Users\\kiran\\Music"
            songs = os.listdir(music_dir_path)  # converting songs into list
            length = len(songs)
            chose+=1
            if chose >= length:
                speak("no more music to next")
                speak("i'm playing music from starting")
                chose = 0
                os.startfile(os.path.join(music_dir_path, songs[chose]))
            else:
                os.startfile(os.path.join(music_dir_path, songs[chose]))
                chose += 1
        elif 'stop' in query or "stop the music" in query or "quit music" in query:
            speak('okay')
            speak("now i stop music")
            #we are writing different music players name hear becuz one one person will have their own wish music players
            #the following codes will work for music players
            os.system('taskkill /F /FI "WINDOWTITLE eq Movies & Tv" ')
            os.system('taskkill /F /FI "WINDOWTITLE eq Groove Music" ')
            os.system('taskkill /F /FI "WINDOWTITLE eq Media Player" ')
            os.system('taskkill /F /FI "WINDOWTITLE eq Windows Media Player" ')
            #os.system('taskkill /F /FI "WINDOWTITLE eq VLC media player" ')




        # <----------------IP ADDRESS(using request module)---------------------->
        elif "ip address " in query or "what is my ip address" in query or "my ip address" in query:

            ip = get("https://api.ipify.org").text  # website gives ip address we are converting it into text
            print(f"your ip address is: {ip} ")
            speak(f"your ip address is: {ip} ")



        elif "who" in query or "where " in query or "what is" in query or "how " in query:
            query = query.replace("who", "")
            query = query.replace("what is", "")
            query = query.replace("how", "")
            query = query.replace("where", "")
            info = wikipedia.summary(query, sentences=2)  # read only 3 sentences
            speak("according to wikipedia")
            print(info)
            speak(info)

        # <-----------------------playing in youtube using pywhatkit------------------------>
        elif "play" in query:
            query = query.replace('play', '')  # empty string replaces play
            # if i say play saranga dariya then system takes only saranga dariya.''(in this empty string saranga dariya will be stored)
            print("Playing" + query)
            speak("Playing" + query)
            pywhatkit.playonyt(query)


        elif "search" in query or "google" in query:
            query = query.replace("search ", "")
            query = query.replace("google ", "")
            print("okay,Searching for", query)
            speak("okay searching for" + query)
            pywhatkit.search(query)

            # webbrowser.open("www.youtube.com")


        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")



        # <------PYAUTOGUI FEATURES=used to automate python using shortcut keys------->
        elif "open hidden menu" in query:
            # win +X=opens hidden menu
            pyautogui.hotkey("winleft", "x")

        elif "open task manager" in query:
            # Crtl + Shift +Esc=opens task manager
            pyautogui.hotkey("ctrl", "shift", "esc")

        elif "open task view" in query:
            # win +tab=shows running tasks
            pyautogui.hotkey("winleft", "tab")

        elif "shift tab" in query or "switch tab" in query:
            # alt+tab=shifts the tab
            pyautogui.hotkey("alt", "tab")

        elif "take screenshot" in query:
            # win+prtscr
            pyautogui.hotkey("winleft", "prtscr")
            print("screenshot location C:\\Users\\kiran\\OneDrive\\Pictures\\Screenshots")
            speak("okay ,you the screenshot is in the given location")

        elif "take snip" in query:
            pyautogui.hotkey("winleft", "shift", "s")
            speak("please take your snip of your choice")

        elif "close current application" in query:
            pyautogui.hotkey("alt", "f4")

        elif "take me to desktop" in query:
            pyautogui.hotkey("winleft", "d")

        elif "open new virtual desktop" in query:
            pyautogui.hotkey("winleft", "ctrl", 'd')

        elif "open file explorer" in query:
            pyautogui.hotkey("winleft", "e")

        elif "open run dialog box" in query:
            pyautogui.hotkey("winleft", "r")

        elif "copy the selected text" in query or "copy" in query:
            pyautogui.hotkey("ctrl", "c")
            speak("copied")

        elif "paste the copied text" in query or "paste" in query:
            pyautogui.hotkey("ctrl", "v")
            speak("pasted")

        elif "type what i say" in query:  # u might get error if you get error comment this code
            pyautogui.hotkey("winleft", "h")


        # <-----------------------------------BATTERY PERCENTAGE(psutil module)------------------------->

        elif "battery percentage" in query or "what is my battery percentage" in query or "battery percentage in my system" in query:
            import psutil

            battery = psutil.sensors_battery()
            percentage = battery.percent
            if percentage >= 75 and percentage <= 100:
                speak(
                    f"our system has {percentage} percent battery left,which is sufficient for about 2 hours at a moderate usage ")
            elif percentage >= 30 and percentage < 75:
                speak(
                    f"our system has {percentage} percent battery left,which might give you 60 to 70 minutes at a moderate usage")
            elif percentage >= 0 and percentage < 30:
                speak(
                    f"our system has a very crtical battery left, that is {percentage} percent battery,Please pluggin the charger")

        elif "jarvis sleep" in query or "bye" in query or "sleep" in query  or "close jarvis" in query:
            speak("bye")
            break