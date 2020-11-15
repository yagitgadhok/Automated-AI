import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice' , voices[0].id)

def speak(audio):
    ''' main speak command function'''
    engine.say(audio)
    engine.runAndWait()

def wishme():
    ''' wishme when wake up'''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak('good morning')

    elif hour>=12 and hour<18:
        speak('good afternoon')

    else:
        speak('good evening')

    speak('i am AID how can i help u')


def takecommand():
    '''takes microphone input and returns string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')

    except Exception as e:
        print(e)

        print('say that again....')
        return 'None'

    return query
def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mail','pwd')
    server.sendmail('mail',to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
    #if 1:
        query =takecommand().lower()

        #logic for executing on basis of command
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 2)
            speak('according to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            query= query.replace('open','')
            speak(f'opening {query}')
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            query= query.replace('open','')
            speak(f'opening{query}')
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            query= query.replace('open','')
            speak(f'opening{query}')
            webbrowser.open('stackoverflow.com')

        elif 'open linkedin' in query:
            query= query.replace('open','')
            speak(f'opening{query}')
            webbrowser.open('linkedin.com')
    
        #elif 'play music' in query:
        #music_dir = 'dir name'
        #songs = as.listdir(music_dir)
        #print(songs)
        #os.startfile(os.path.join(music_dir,songs[rand(len(songs))]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'sir the time is {strtime}')

        elif 'how are you' in query:
            speak(f'i am fine sir, thank you for asking')

        elif 'open code' in query:
            code = "D:\\Microsoft VS Code\\Code.exe"
            speak(f'sure sir')
            os.startfile(code)

        elif 'open word' in query:
            word = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            query= query.replace('open','')
            speak(f'opening{query}')
            os.startfile(word)

        elif 'open chrome' in query:
            chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            query= query.replace('open','')
            speak(f'opening{query}')
            os.startfile(chrome)
        
        elif 'send email' in query:
            try:
                speak('what should i write')
                content = takecommand()
                to = 'gadhokyagit@gmail.com'
                sendemail(to,content)
                speak('email has been sent')

            except Exception as e:
                print(e)
                speak('sorry unable to sent the mail')

        elif 'cancel' in query:
            break


