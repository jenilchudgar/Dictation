import pyttsx3
import random
from tkinter import *

# Constants
APPEND = 'a'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0])
engine. setProperty("rate", 150)

wrong_words = {}

words = [
    'gradually',
    'Norman',
    'Gortsby',
    'Crispin',
    'beaten',
    'tragic',
    'boarding',
    'mutters',
    'exaggerated',
    'temper',
    'disinterested',
    'glances',
    'Patagonian',
    'Berkshire',
    'Square',
    'theatre',
    'strolled',
    'desperate',
    'shilling',
    'foriegn',
    'decent',
    'embassy',
    'impossible',
    'afternoon',
    'adopting',
    'confident',
    'restrained',
    'forethought',
    'con man',
    'hurriedly',
    'sovereign',
    'dissapear',
    'judging',
    'circumstances',
    'slipped',
]

'''words = [
    'confident',
    'exaggerated',
    'Berkshire',
    'sovereign',
    'Gortsby',
    'Norman',
    'dissapear',
]
'''

'''
words = [
    'Gortsby',
    'exaggerated',
    'sovereign',
]
'''
random.shuffle(words)

def wrong_word(word,user_wrote):
    wrong_words[word] = user_wrote

def speak(audio: str):
    engine.say(audio)
    engine.runAndWait()

def check():
    if entry.get() == word_wanted:
        print("Correct!")
    else:
        print("Wrong!")
        wrong_word(word_wanted,entry.get())
    
    next_word()

def next_word():
    global word_wanted
    
    if len(words) > 0:
        index = random.randint(0,len(words)-1)
        word_wanted = words[index]
        speak(word_wanted)
        speak(f"I repeat {word_wanted}")

        words.remove(word_wanted)

        entry.delete(0,END)
    else:
        print("Dictation Over!")
        root.destroy()

def write_to_file():
    with open("wrong.txt",APPEND) as f:
        for element in wrong_words:
            word = element
            user_wrote = wrong_words[element]
            f.write(f"\n{word}\t|\t{user_wrote}")

# Tkinter
root = Tk()
root.title("Dictation App")
root.geometry("400x400")

entry = Entry(root,font=('Calibri',18))
entry.pack(pady=20)

next_btn = Button(root,text="Next!",command=check,font=('Calibri',18))
next_btn.pack(pady=10)

next_word()

root.mainloop()

write_to_file()