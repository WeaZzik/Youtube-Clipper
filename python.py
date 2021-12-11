import youtube_dl
import os
import time
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import *
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def main():
    root = Tk() 
    root.title('Youtube Clipper by WeaZzik')
    root.resizable(width=FALSE, height=FALSE)
    root.geometry('{}x{}'.format(600, 60))

    LINKTXT = Label(root, text="V0.13")
    LINKTXT.grid(row=0, column=0)
    LINK = Entry(root, width=50)
    LINK.grid(row=1, column=3)

    TIME1TXT = Label(root, text="T1:")
    TIME1TXT.grid(row=1, column=4)
    TIME1 = Entry(root, width=8)
    TIME1.grid(row=1, column=5)
    TIME1.insert(END, '0')

    TIME2TXT = Label(root, text="T2:")
    TIME2TXT.grid(row=1, column=6)
    TIME2 = Entry(root, width=8)
    TIME2.grid(row=1, column=7)
    TIME2.insert(END, '120')

    STXT = Label(root, text="        ")
    STXT.grid(row=1, column=8)

    def wait():
        FileName = time.strftime("%d_%m_%Y-%H_%M")
        T1 = TIME1.get()
        T2 = TIME2.get()
        if T1.isnumeric() == False or T2.isnumeric() == False:
            showwarning('Erreur', "Erreur dans le ou les temps saisis")
            root.destroy()
            main()
        t1 = int(T1)
        t2 = int(T2)
        link = LINK.get()
        linktest = "https://www.youtube.com/watch?v=5Or7GgXvYu8"
    
        if not os.path.exists("CLIPS"):
            os.mkdir("CLIPS")
        
        ydl_opts = {'outtmpl': 'CLIPS/Output.mp4'}
    
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        except:
            #showwarning('Erreur', "Erreur dans l'URL fournis")
            root.destroy()
            main()
        
        ffmpeg_extract_subclip("CLIPS/Output.mp4", t1, t2, targetname="CLIPS/Output2.mp4")
        os.remove("CLIPS/Output.mp4")
        os.rename("CLIPS/Output2.mp4", "CLIPS/"+FileName+".mp4")
    
    CONFIRM = Button(root, text = 'Confirm', command = wait).grid(row=1, column=9)
    
    mainloop() 
main()