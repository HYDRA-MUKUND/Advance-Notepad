

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
import pyttsx3
import os
import speech_recognition as sr

root = Tk()
root.geometry('1100x560')
root.title('NotePad')
r = sr.Recognizer()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(root, bd=1, yscrollcommand=scrollbar.set, font='lucida 13')
file = None
text.pack(expand=True, fill=BOTH)

scrollbar.config(command=text.yview)


def helpwindow():

    messagebox.showinfo('Help', 'This is Help Box..!!')


def copy():

    text.event_generate('<<Copy>>')


def cut():

    text.event_generate('<<Cut>>')


def paste():

    text.event_generate('<<Paste>>')


def selectall():

    text.event_generate('<<SelectAll>>')


def newFile():

    global file
    root.title('Untitled - Notepad')
    file = None
    text.delete(1.0, END)


def openFile():

    global file
    file = askopenfilename(defaultextension='.txt',
                           filetypes=[('All Files', '*.*'),
                           ('Text Documents', '*.txt')])
    if file == '':
        file = None
    else:
        root.title(os.path.basename(file) + ' - Notepad')
        text.delete(1.0, END)
        f = open(file, 'r')
        text.insert(1.0, f.read())
        f.close()


def texttospeechone():
    engine = pyttsx3.init()
    voicesf = engine.getProperty('voices')
    engine.setProperty('rate', 168)

    engine.setProperty('voice', voicesf[0].id)
    texts = text.get(1.0, END)
    if text.compare('end-1c', '==', '1.0'):
        engine.say('Sorry nothing is present in notepad body please type something and then try me'
                   )
        engine.runAndWait()
    else:
        engine.say(texts)
        engine.runAndWait()


def texttospeechtwo():
    enginetwo = pyttsx3.init()
    voicesd = enginetwo.getProperty('voices')
    enginetwo.setProperty('rate', 168)
    enginetwo.setProperty('voice', voicesd[1].id)
    texts = text.get(1.0, END)
    if text.compare('end-1c', '==', '1.0'):
        enginetwo.say('Sorry nothing is present in notepad body please type something and then try me'
                      )
        enginetwo.runAndWait()
    else:
        enginetwo.say(texts)
        enginetwo.runAndWait()


def speechtotext():

    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            textt = " " + r.recognize_google(audio)
            text.insert(END, textt)
        except:
            engine = pyttsx3.init()
            voicesf = engine.getProperty('voices')
            engine.setProperty('rate', 168)
            engine.setProperty('voice', voicesf[0].id)
            engine.say('sorry unable to recognize your voice')
            engine.runAndWait()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',
                                 defaultextension='.txt',
                                 filetypes=[('All Files', '*.*'),
                                 ('Text Documents', '*.txt')])
        if file == '':
            file = None
        else:

            # Save as a new file

            f = open(file, 'w')
            f.write(text.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + ' - Notepad')
            print('File Saved')
    else:

        # Save the file

        f = open(file, 'w')
        f.write(text.get(1.0, END))
        f.close()


mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)

m1.add_command(label='  New', command=newFile)

m1.add_command(label='  Open...', command=openFile)

m1.add_command(label='  Save...', command=saveFile)
m1.add_separator()
m1.add_command(label='  Exit', command=quit)
mainmenu.add_cascade(label='File', menu=m1)

m2 = Menu(mainmenu, tearoff=0)

m2.add_command(label='Cut               ->   Ctrl-X', command=cut)
m2.add_separator()
m2.add_command(label='Copy            ->   Ctrl-C', command=copy)
m2.add_separator()
m2.add_command(label='Paste            ->   Ctrl-V', command=paste)
m2.add_separator()
m2.add_command(label='SelectAll      ->   Ctrl-A', command=selectall)
mainmenu.add_cascade(label='Edit', menu=m2)

m3 = Menu(mainmenu, tearoff=0)

m3.add_command(label='Get Help', command=helpwindow)

mainmenu.add_cascade(label='Help', menu=m3)
m4 = Menu(mainmenu, tearoff=0)

m4.add_command(label=" Listen in Men's Sound..",
               command=texttospeechone)
m4.add_command(label=" Listen in Women's Sound..",
               command=texttospeechtwo)
m4.add_command(label=' Voice Typing..', command=speechtotext)
mainmenu.add_cascade(label='Advance', menu=m4)
root.config(menu=mainmenu)

root.mainloop()
