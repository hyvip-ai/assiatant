import pyttsx3
from datetime import date,datetime
import difflib
import pywhatkit as kit
import webbrowser
import wikipedia
import random
import subprocess







engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voices',voices[0].id)
def intro():
    engine.say("hello sir i am I-BER ")
    engine.runAndWait()
    engine.say("my full name is,IMAGINATION BECOMES REALITY")
    engine.runAndWait()

def time():




    hour = datetime.today().hour
    minute = datetime.today().minute

    engine.say(" the time is")
    if hour>=12:
        hour = hour - 12
        if hour==00:
            engine.say("12")
            engine.runAndWait()
        else:
            engine.say(hour)
        engine.say(minute)
        engine.say("p m")
        engine.runAndWait()
    else:
        if hour==00:
            engine.say("12")
            engine.runAndWait()
        else:
            engine.say(hour)
        engine.say(minute)
        engine.say("a m")
        engine.runAndWait()


def wish():
    hour = datetime.today().hour

    if hour>=12 :
        engine.say("good afternoon ")
        engine.runAndWait()
        engine.say("I-BER at your service sir, what can i do for you")
        engine.runAndWait()
    elif hour<12:
        engine.say("good morning ")
        engine.runAndWait()
        engine.say("I-BER at your service sir, what can i do for you")
        engine.runAndWait()

wish()
def date():
    today = datetime.today().date()

    engine.say("today's date is")

    engine.say(today)
    engine.runAndWait()









while True:

    text = input("type here:")
    words = ["whats-app","inch","what","calculator","whatsapp","translator","much","how many","many","become","to" ,"it","how much","is" ,"equals to" ,"to become" ,"convert","m","feet","in","into","to", "the","joke","lat","apply","code","python","lon","latitude","longitude","tell","mail","g mail","chrome","google","g-mail","gmail" ,"search","whats app", "intro","whats","app", "on","time","some", "date","me","something","jarvis","hey","can","you","open","for","youtube","want","mode","you","check","play","music"]
    l = "search in wikipedia youtube chrome open on wiki yt"

    line = text

    line = line.split()
    for word in line:

        if word not in words:
            x = difflib.get_close_matches(word, words)
            # print(x)


            for z in range(0,len(x)):
                print("did you mean", x[z], end="")
                print(" instead of ", word, end="")
                print("?")
                engine.say("did you mean")
                engine.say(x[z])
                engine.say("instead of")
                engine.say(word)
                engine.say("if yes , enter 'yes' to change the word else enter 'no' for not changing it")
                engine.runAndWait()
                ch = input("enter your choice:")
                #print(x[0])
                #print(x)
                if ch == "yes":
                    y = line.index(word)
                    line.remove(line[y])
                    line.insert(y, x[z])

                elif ch == "no":

                    if x[z] == "jarvis":

                        engine.say("sir,my name is jarvis,not ")
                        engine.say(word)

                        engine.runAndWait()
                        continue



    text = " ".join(line)
    my_command = text

    text = text.split()
    if "wikipedia" in my_command and "search" in my_command or "wiki" in my_command:
        #line = input("enter the line")
        #l = "search in wikipedia"
        l = l.split()
        #line = line.split()
        search_list = []
        for word in text:

            if word not in l:
                search_list.append(word)

        new_list = []
        for word in search_list:
            #print(word)
            new_list.append(word.capitalize())

        new_list = " ".join(new_list)
        #print(new_list)
        ans = wikipedia.summary(new_list,sentences=3)
        result = ans.split()
        i = 0
        for j in result:
            print(j ,end = " ")
            i = i + 1
            if i == 25:
                print(" ")
                i = 0
        engine.say(ans)
        engine.runAndWait()


        engine.say("sir, do you want me to open the search result?")
        engine.runAndWait()
        ch1 = input("\n enter your choice:")


        if "yes" in ch1:
            engine.say("as your wish sir!")
            webbrowser.open("https://wikipedia.org/wiki/" + new_list)
            engine.runAndWait()



        elif "no" in ch1:
            engine.say("as your wish sir!")
            engine.runAndWait()
            continue




    elif "youtube" in my_command  or "yt" in my_command and "search" in my_command and "python" not in my_command:
        l = l.split()
        # line = line.split()
        search_list = []
        for word in text:

            if word not in l:
                search_list.append(word)

        new_list = []
        for word in search_list:
            # print(word)
            new_list.append(word.capitalize())

        new_list = " ".join(new_list)
        # print(new_list)
        engine.say("sir, do you want me to play the first video of the search result?")
        engine.say("enter play video for playing the video, and show results for showing the serach result")
        engine.runAndWait()
        cho = input("enter your choice:")
        if "result" in cho or "results" in cho:
            engine.say("showing the search results ,sir")
            engine.runAndWait()
            webbrowser.open("https://www.youtube.com/results?search_query="+new_list)
        elif "play" in cho:
            engine.say("playing the video, sir")
            engine.runAndWait()
            kit.playonyt(new_list)
    elif "search" in my_command and "chrome" in my_command :
        l = l.split()
        # line = line.split()
        search_list = []
        for word in text:

            if word not in l:
                search_list.append(word)

        new_list = []
        for word in search_list:
            # print(word)
            new_list.append(word.capitalize())

        new_list = " ".join(new_list)
        # print(new_list)
        engine.say("opening chrome ,sir")
        engine.runAndWait()
        webbrowser.open("https://google.com/?#q="+new_list)


    elif "search" in my_command and "chrome" not in my_command and "youtube" not in my_command and "wiki" not in my_command and "wikipedia" not in my_command:

        l = l.split()
        # line = line.split()
        search_list = []
        for word in text:

            if word not in l:
                search_list.append(word)

        new_list = []
        for word in search_list:
            # print(word)
            new_list.append(word.capitalize())

        new_list = " ".join(new_list)
        # print(new_list)
        engine.say("sir,as you haven't mentioned anything like where you want to search ")
        engine.say(new_list)
        engine.say("so i am opening every possible search result")
        engine.runAndWait()
        webbrowser.open("https://google.com/?#q=" + new_list)
        webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+new_list)
        webbrowser.open_new_tab("https://wikipedia.org/wiki/" + new_list)




    if  "date" in my_command:

        date()


    if "time" in my_command and "centimeter" not in my_command and "centimeters" not in my_command:
        time()
    if "intro" in my_command or "yourself" in my_command:
        intro()

    if "open whats-app" in my_command or "whats app" in my_command or "whatsapp" in my_command :
        engine.say("opening whats app, sir")
        engine.runAndWait()
        webbrowser.open("https://web.whatsapp.com/")

    if "open mail" in my_command or "open g-mail" in my_command or "gmail" in my_command or "mail" in my_command and "send" not in my_command or "g mail" in my_command:
        engine.say("opening your g-mail sir")
        engine.runAndWait()
        webbrowser.open("https://www.google.com/gmail/")
    if "send mail" in my_command:
        engine.say("this feature is not available this time")
        engine.runAndWait()



    if "open youtube" in my_command:

        engine.say("opening youtube sir")
        engine.runAndWait()
        webbrowser.open("https://www.youtube.com/")


    if "sorry jarvis" in my_command:
        engine.say("its okay sir")
        engine.runAndWait()
   


    if "go to sleep" in my_command:
        engine.say("as your wish sir")
        engine.runAndWait()

    if "open google" in my_command and "map" not in my_command:
        engine.say("opening google, sir")
        engine.runAndWait()
        webbrowser.open("https://google.com/")



    if "open map" in my_command or "open google map" in my_command or "open maps" in my_command or "open google maps" in my_command or "my location" in my_command:
        engine.say("opening google maps , sir")
        engine.runAndWait()
        webbrowser.open("https://www.google.com/maps/")
    if "play music" in my_command or "hit the music" in my_command or "play some music" in my_command or "music" in my_command:
        music = ["hips don't lie","perfect to me","perfect","to be young","in the end","play date","anne-marie-2002","whenever-wherever","alone","believer","numb"]
        x = random.choice(music)
        engine.say("sir,do you want me to open the search result or to play the first video of the search result?")
        engine.runAndWait()
        cho = input("enter your choice:")
        if "play" in cho:
            engine.say("playing")
            engine.say(x)
            engine.say("on youtube")
            engine.runAndWait()
            kit.playonyt(x)
        elif "result" in cho or "results" in cho:
            engine.say("showing the search result for")
            engine.say(x)
            engine.say("sir")
            engine.runAndWait()
            webbrowser.open("https://www.youtube.com/results?search_query="+x)

    if "tell" in my_command and "joke" in my_command:
        jokes = ["how many  introverts does it take to screw a light bulb? why does it have to be a group activity","why can't the astronauts eat popsicles? In space no one can hear the ice cream truck","what's the first thing a monster eats after his teeth check? The dentist","what did the teacher do with her student's report on the history of cheese?..She grated it","what do you call a rose that wants to go to the moon?Goolab ja moon"]
        x = random.choice(jokes)
        #print(jokes)
        engine.say(x)
        engine.runAndWait()

    if "convert" in my_command  and "to become" not in my_command and "how much" not in my_command and "open" not in my_command:
        engine.say("let's see, sir")
        webbrowser.open("https://google.com/?#q="+my_command)
        engine.runAndWait()

    if  "translator" in my_command and "open calculator" not in my_command :
        if "open" in my_command:
            input_lan = text[1]
            output_lan = text[3]
            engine.say("opening")
            engine.say(input_lan)
            engine.say("to")
            engine.say(output_lan)
            engine.say("translator,sir")

            webbrowser.open("https://google.com/?#q="+ input_lan + " to " + output_lan +" translation")
            engine.runAndWait()
        elif "open" not in my_command:
            input_lan = text[0]
            output_lan = text[2]
            engine.say("opening")
            engine.say(input_lan)
            engine.say("to")
            engine.say(output_lan)
            engine.say("translator,sir")

            webbrowser.open("https://google.com/?#q=" + input_lan + " to " + output_lan + " translation")
            engine.runAndWait()
           # ai1.AlexaResponses




    if "open calculator" in my_command:


        engine.say("opening calculator,sir")

        subprocess.Popen('C:\Windows\System32\calc.exe')
        engine.runAndWait()



















