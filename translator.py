from tkinter import *
from googletrans import Translator
from PIL import ImageTk, Image
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os

root = Tk()
root.geometry('450x438')
root.title("Translator")
root.iconbitmap("1.ico")
root.configure(background="#1278B3")

frm = Frame(root, bg="#fff")
frm.pack(padx=0, pady=0)

fr = Frame(root, relief=RIDGE, bg="#1278B3")
fr.pack(padx=0, pady=10, ipadx=150)


def translating():
    word = entry.get()
    translator = Translator()
    translated_sentence = translator.translate(word, src='en', dest='ru')
    output.insert(END, translated_sentence.text + "\n")

    entry.delete(0, END)


def reset():
    output.delete('1.0', END)


def speak():
    text = output.get('1.0', END)
    tts = gTTS(text=text, lang="ru")
    filename = "sound1.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)


def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            print("Recognizing....")
            said = r.recognize_google(audio)
            entry.insert(0, said)
        except:
            output.insert(END, "Error")
    return said


image1 = ImageTk.PhotoImage(Image.open("5.png"))
lbl = Label(frm, image=image1)
lbl.pack(padx=0, pady=0)

lbl1 = Label(fr, text="Detect language", font="times 15 bold", fg="#fff", bg="#1278B3", borderwidth=5)
lbl1.grid(row=0, column=0)

clicked = StringVar()
clicked.set("English")

option1 = OptionMenu(fr, clicked, "English", "Russian", "Turkish", "Spanish", "German", "Italian", "French", "Polish")
option1.grid(row=0, column=1)

lbl_txt = Label(fr, text="==>>", bg="#1278B3", fg="#fff")
lbl_txt.grid(row=0, column=2)

clicked2 = StringVar()
clicked2.set("Russian")

option2 = OptionMenu(fr, clicked2, "English", "Russian", "Turkish", "Spanish", "German", "Italian", "French", "Polish")
option2.grid(row=0, column=3, columnspan=4)

entry = Entry(fr, width=43, bg="#eee", font="times 15 bold")
entry.grid(row=1, column=0, columnspan=4, pady=5, padx=4, ipady=43)

output = Text(fr, width=43, height=8, pady=6, padx=5, wrap=WORD, bd=2, bg="#eee", font="times")
output.grid(row=2, column=0, columnspan=4, pady=5, padx=2, ipadx=43)

name = Label(fr, text="Made by Mekan Jumayev 2020", bg="white", fg="#102132")
name.grid(row=3, column=2, pady=5, columnspan=4, padx=10)

btn = Button(fr, text="Translate", fg="red", bg="#fff", font="bold", command=translating)
btn.grid(row=3, column=0, ipadx=20)

btn_reset = Button(fr, text="Reset", fg="red", bg="#fff", font="bold", command=reset)
btn_reset.grid(row=3, column=1)

img1 = ImageTk.PhotoImage(Image.open("01.png"))
btn_en = Button(fr, image=img1, command=record)
btn_en.grid(row=1, column=3, sticky=E + S)

img2 = ImageTk.PhotoImage(Image.open("0.png"))
btn_ru = Button(fr, image=img2, command=speak)
btn_ru.grid(row=2, column=3, sticky=E + S, ipadx=3)

root.mainloop()
