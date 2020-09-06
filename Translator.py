from googletrans import Translator, constants
from gtts import gTTS 
import speech_recognition as sr
from pydub import AudioSegment
from playsound import playsound
n=int(input("how you want to translate!!???\nPress (1) Speech to speech\nPress (2) Text to speech\n"))
if n==1:
    c=1
    while(c!=0):
        v=int(input("From where you want to give input\n1.Audio file\n2.Microphone\n"))
        if v==1:
            r = sr.Recognizer()
            dst = "hi2.wav"                                                    
            sound = AudioSegment.from_mp3(r"C:\Users\ADMIN\Desktop\Life\Python project\New folder\Translated Audio.mp3")
            sound.export(dst, format="wav")
            audio = sr.AudioFile('hi2.wav')
            with audio as source:
                audio_text = r.record(source)
                txt=r.recognize_google(audio_text)
            print("Your Text: "+txt)
            c-=1 
        elif v==2:
            cc=2
            while(cc!=0):
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Talk")
                    audio_text = r.listen(source)
                    print("Time over, thanks")    
                    try:
                        txt=r.recognize_google(audio_text)
                        print("Your Text: "+txt)
                        cc=0
                    except:
                        print("Sorry, I did not get that")
                        cc=cc-1
            c-=1                   
        else:
            print("You have input a wrong input try angain")
elif n==2:
    txt=str(input("Enter you text:"))
else:
    print("Sorry ....You have enter a wrong input")
    exit
    
lan=str(input("Enter the language code to which you want the translate the text e.g.:- \n'hi': Hindi\n'es': Spanish\n'fr': French\n'gu': Gujarati\n'te': Telugu\n'kn': Kannada\n'en': English\nYou want to translate your text to:"))
translator = Translator()
translation = translator.translate(txt, dest=lan)
d=translator.detect(txt)
print("\nYour Enter text Language code is:", d.lang)
print("Confidence:", (d.confidence)*100,"%")
print("\nYour text after translation:",translation.text)
x=translation.text
voice=gTTS(text=x, lang=lan, slow=False) 
#print("\nUrl of your translated voice-->\n",voice.get_urls())
voice.save("Translated3Audio.mp3") 
playsound("Translated3Audio.mp3")
        