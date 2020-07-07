'''
This python program helps to covert a text file "myfile.txt" to a audio file "myaudio.wav" within the same directory. 

By default the language in which it gets converted is french but you can change it by replacing the code against language in line 12.
'''
from gtts import gTTS
import os

f = open('myfile.txt')
x = f.read()

language = 'fr'

audio = gTTS(text=x,lang=language,slow=False)

audio.save("myaudio.wav")
os.system("myaudio.wav")
