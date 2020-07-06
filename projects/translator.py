'''
This python file is made to translate a file named "main.txt" to a different language which is french, If you want to change the language you need to wite the code of other
language against dest at line 18.

For this you need a jupyter notebook and run a pip command "pip install googletrans".

After running this file you will get a file "myfile.txt" with a new language in the same directory. 
'''
from googletrans import Translator

fh = str(input("Enter file name"))
if len(fh)<1:
    fh="main.txt"
f = open(fh, "r")
a=f.read()

translator = Translator()
translated_sentence = translator.translate(a,src='en',dest='fr')

b = str(translated_sentence)

fc = open("myfile.txt", "w")
fc.write(b)
fc.close()
